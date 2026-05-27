"""
validate_workflow.py -- n8nワークフローJSONの静的検証
"""
import json
import sys
from pathlib import Path
from collections import Counter


def validate(path: str) -> tuple[str, list[str]]:
    issues: list[str] = []
    warnings: list[str] = []
    p = Path(path)

    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return "FAIL", [f"JSON構文エラー: {e}"]
    except FileNotFoundError:
        return "FAIL", [f"ファイルが見つかりません: {path}"]

    nodes = data.get("nodes")
    if not isinstance(nodes, list) or len(nodes) == 0:
        issues.append("nodes が存在しないか空です")
    else:
        names = [n.get("name", "") for n in nodes]
        dupes = [name for name, count in Counter(names).items() if count > 1]
        if dupes:
            warnings.append(f"ノード名が重複しています: {dupes}")

        for n in nodes:
            if n.get("credentials"):
                warnings.append(
                    f"ノード '{n.get('name')}' にcredential参照があります -- 使用者が再設定必要"
                )

    if "connections" not in data:
        issues.append("connections が存在しません")

    if issues:
        return "FAIL", issues + warnings
    if warnings:
        return "WARN", warnings
    return "PASS", []


def main():
    if len(sys.argv) < 2:
        print("使い方: python validate_workflow.py <workflow.json>")
        sys.exit(1)

    result, messages = validate(sys.argv[1])
    print(f"結果: {result}")
    for msg in messages:
        print(f"  - {msg}")
    sys.exit(0 if result != "FAIL" else 1)


if __name__ == "__main__":
    main()
