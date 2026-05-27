# セットアップガイド

Quest 01を動かすために必要な4つの準備。

---

## 1. n8n を用意する

**Cloud版（推奨）**

1. https://n8n.io にアクセス
2. 「Get started for free」でアカウント作成
3. ワークスペースが作成されたらOK

**自己ホスト版**

```bash
npm install n8n -g
n8n start
# http://localhost:5678 でアクセス
```

---

## 2. OpenAI APIキーを取得する

1. https://platform.openai.com/api-keys にアクセス
2. 「+ Create new secret key」をクリック
3. キーをコピーして安全な場所に保存

> 利用料の目安: 1記事あたり約0.01〜0.05円（gpt-4o-mini使用時）

---

## 3. Google Sheetsを準備する

1. https://sheets.google.com で新しいスプレッドシートを作成
2. シート名を **「AIニュース監視ログ」** に変更
3. 1行目（ヘッダー）に以下を入力:

| A | B | C | D | E |
|---|---|---|---|---|
| Date | Title | Summary | Score | URL |

4. スプレッドシートのURLから **スプレッドシートID** をコピーする
   - URL例: `https://docs.google.com/spreadsheets/d/【ここがID】/edit`

---

## 4. Discord Webhook URLを取得する

1. Discordで通知を受け取りたいサーバーを開く
2. 通知したいチャンネルの設定 → 「連携サービス」→「ウェブフック」
3. 「新しいウェブフック」を作成
4. 「ウェブフックURLをコピー」

---

## 準備完了チェック

- [ ] n8nにアクセスできる
- [ ] OpenAI APIキーをメモした
- [ ] Sheetsのスプレッドシート IDをメモした
- [ ] Discord Webhook URLをメモした

準備ができたら `IMPORT_GUIDE.md` へ進んでください。
