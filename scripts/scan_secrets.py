"""
scan_secrets.py -- ワークフローJSON内の秘密情報を検出
"""
import json
import re
import sys
from pathlib import Path

PATTERNS: list[tuple[str, re.Pattern]] = [
    ("API Key", re.compile(r"(?i)(api[_\-]?key|apikey)\s*[:=]\s*\S+")),
    ("Bearer Token", re.compile(r"(?i)bearer\s+[A-Za-z0-9\-._~+/]+=*")),
    ("Cookie", re.compile(r"(?i)cookie\s*[:=]\s*\S+")),
    ("Email", re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")),
    ("Password", re.compile(r"(?i)(password|passwd|pwd)\s*[:=]\s*\S+")),
    ("Client Secret", re.compile(r"(?i)client[_\-]?secret\s*[:=]\s*\S+")),
    ("Access Token", re.compile(r"(?i)access[_\-]?token\s*[:=]\s*\S+")),
    ("Refresh Token", re.compile(r"(?i)refresh[_\-]?token\s*[:=]\s*\S+")),
    ("OpenAI Key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("Google API Key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("Slack Token", re.compile(r"xox[baprs]-[0-9A-Za-z\-]+")),
    ("Discord Webhook (actual)", re.compile(
        r"https://discord(?:app)?\.com/api/webhooks/\d+/[A-Za-z0-9\-_]+"
    )),
]

IGNORE_VALUES = {
    "YOUR_API_KEY", "CHANGE_ME", "PLACEHOLDER", "YOUR_TOKEN",
    "INSERT_HERE", "YOUR_KEY", "EXAMPLE", "DUMMY",
    "REPLACE_WITH_YOUR_CREDENTIAL_ID", "REPLACE_WITH_YOUR",
}


def scan(path: str) -> list[str]:
    p = Path(path)
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return [f"読み込みエラー: {e}"]

    findings = []
    raw = json.dumps(data, ensure_ascii=False)
    for name, pattern in PATTERNS:
        for match in pattern.finditer(raw):
            matched = match.group(0)
            if any(ignore in matched.upper() for ignore in IGNORE_VALUES):
                continue
            findings.append(f"{name}: {matched[:80]}")

    return findings


def main():
    if len(sys.argv) < 2:
        print("使い方: python scan_secrets.py <workflow.json>")
        sys.exit(1)

    findings = scan(sys.argv[1])
    if findings:
        print(f"[FAIL] {len(findings)}件の秘密情報を検出しました:")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("[PASS] 秘密情報は検出されませんでした")
        sys.exit(0)


if __name__ == "__main__":
    main()
