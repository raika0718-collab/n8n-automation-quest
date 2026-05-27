# n8n Automation Quest

> ゲーム感覚でn8nを学べる、無料ワークフローテンプレートシリーズ。

```
あなたは自動化ギルドの新人技師。
失われた情報監視システムを復旧せよ。
```

---

## Quest 01: AIニュース監視システムを復旧せよ

RSSフィードを取得し、AIが要約・重要度判定を行い、Google Sheetsに記録してDiscordへ通知するシステムを構築します。

```
RSS取得 → AI要約 → 重要度判定 → Sheets保存 → Discord通知
```

### クリア条件

- [ ] RSS Feedからニュースを取得できる
- [ ] OpenAI APIが記事を3行で要約できる
- [ ] 重要度スコアが100点満点で出力される
- [ ] Google Sheetsにデータが保存される
- [ ] スコア70点以上でDiscordに通知が届く

---

## 必要なもの

| サービス | 取得場所 |
|---------|----------|
| n8n（Cloud推奨） | https://n8n.io |
| OpenAI APIキー | https://platform.openai.com/api-keys |
| Googleアカウント | https://accounts.google.com |
| Discord Webhook URL | Discord サーバー設定 > 連携サービス |

---

## クイックスタート

1. `docs/SETUP_GUIDE.md` で各サービスの準備
2. `docs/IMPORT_GUIDE.md` でワークフローをn8nへインポート
3. `docs/QUEST_GUIDE.md` に沿って各ノードを設定
4. テスト実行してクリア！

---

## ファイル構成

```text
n8n-automation-quest/
├─ workflows/
│  └─ quest-01-ai-news-monitor.json   ← インポートするファイル
├─ docs/
│  ├─ SETUP_GUIDE.md                  ← 事前準備
│  ├─ IMPORT_GUIDE.md                 ← インポート手順
│  ├─ QUEST_GUIDE.md                  ← クエスト攻略ガイド
│  └─ ERROR_GUIDE.md                  ← エラー対処法
├─ samples/
│  └─ sample_output.md                ← 期待出力サンプル
└─ scripts/
   └─ preflight.py                    ← 公開前チェック
```

---

## 次のクエスト（予告）

| Quest | テーマ |
|-------|--------|
| Quest 02 | AI動画ネタ収集システム |
| Quest 03 | AI投稿自動生成システム |
| Quest 04 | AI営業リード監視システム |
| Quest 05 | AIエージェント司令システム |

---

## ライセンス

MIT License — 自由に使用・改変・再配布できます。

---

## 作者

[あなたのX/GitHub IDをここに]
