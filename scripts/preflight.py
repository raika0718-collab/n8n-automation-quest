"""
preflight.py -- 公開前の一括チェック
使い方: python scripts/preflight.py workflows/quest-01-ai-news-monitor.json
"""
import io
import json
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() in ("cp932", "cp1252", "ascii"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent))
from validate_workflow import validate
from scan_secrets import scan

PASS_MARK = "[PASS]"
WARN_MARK = "[WARN]"
FAIL_MARK = "[FAIL]"


def run(path_str: str) -> bool:
    path = Path(path_str)
    results: list[tuple[str, str, str]] = []

    # 1. JSON構文
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        results.append(("JSON構文", PASS_MARK, ""))
    except Exception as e:
        results.append(("JSON構文", FAIL_MARK, str(e)))
        _print(results, path)
        return False

    # 2. n8n形式
    has_nodes = isinstance(data.get("nodes"), list) and len(data["nodes"]) > 0
    has_conn = "connections" in data
    if has_nodes and has_conn:
        results.append(("n8n形式 (nodes/connections)", PASS_MARK, ""))
    else:
        missing = []
        if not has_nodes:
            missing.append("nodes")
        if not has_conn:
            missing.append("connections")
        results.append(("n8n形式 (nodes/connections)", FAIL_MARK, f"不足: {missing}"))

    # 3. credential参照確認（WARN: 購入者が再設定するので必須ではない）
    cred_nodes = [
        n.get("name", "?")
        for n in data.get("nodes", [])
        if n.get("credentials")
    ]
    if cred_nodes:
        results.append(("credential混入なし", WARN_MARK,
                        f"credential参照あり (使用者が再設定必要): {cred_nodes}"))
    else:
        results.append(("credential混入なし", PASS_MARK, ""))

    # 4. secret混入
    findings = scan(path_str)
    if findings:
        results.append(("secretなし", FAIL_MARK,
                        f"{len(findings)}件検出: {findings[0][:60]}"))
    else:
        results.append(("secretなし", PASS_MARK, ""))

    # 5. README
    readme_candidates = [
        Path("README.md"),
        path.parent / "README.md",
        Path("docs/README.md"),
    ]
    has_readme = any(c.exists() for c in readme_candidates)
    results.append(("READMEあり", PASS_MARK if has_readme else WARN_MARK,
                    "" if has_readme else "README.mdが見つかりません"))

    # 6. IMPORT_GUIDE
    has_import = Path("docs/IMPORT_GUIDE.md").exists()
    results.append(("IMPORT_GUIDEあり", PASS_MARK if has_import else WARN_MARK,
                    "" if has_import else "docs/IMPORT_GUIDE.mdが見つかりません"))

    # 7. ERROR_GUIDE
    has_error = Path("docs/ERROR_GUIDE.md").exists()
    results.append(("ERROR_GUIDEあり", PASS_MARK if has_error else WARN_MARK,
                    "" if has_error else "docs/ERROR_GUIDE.mdが見つかりません"))

    _print(results, path)
    return not any(FAIL_MARK in r[1] for r in results)


def _print(results: list, path: Path) -> None:
    print(f"\n=== preflight: {path.name} ===\n")
    for label, status, detail in results:
        line = f"  {status} {label}"
        if detail:
            line += f"\n         -> {detail}"
        print(line)
    print()
    failed = any(FAIL_MARK in r[1] for r in results)
    warned = any(WARN_MARK in r[1] for r in results)
    if failed:
        print("結論: FAIL -- 公開前に要修正の問題があります")
    elif warned:
        print("結論: WARN -- 警告あり。確認推奨です")
    else:
        print("結論: PASS -- 静的チェック完了。n8n Cloudで実機確認してください")


def main():
    if len(sys.argv) < 2:
        print("使い方: python scripts/preflight.py <workflow.json>")
        sys.exit(1)
    ok = run(sys.argv[1])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
