# エラー対処ガイド

## OpenAI エラー

### `401 Unauthorized` / `Invalid API key`

**原因:** APIキーが未設定または間違い

**対処:**
1. 「Quest 2: AI解析」ノードをダブルクリック
2. Credentials欄のAPIキーを確認・再入力
3. https://platform.openai.com/api-keys でキーが有効か確認

---

### `429 Too Many Requests` / Rate limit exceeded

**原因:** APIの利用制限に達した

**対処:**
1. しばらく待ってから再実行（通常1〜2分）
2. OpenAIダッシュボードでクォータ残量を確認
3. gpt-4o-miniの場合、無料枠が切れている可能性あり

---

### AI出力のパースに失敗する（スコアが0になる）

**原因:** AIが指定フォーマット以外で返答した

**対処:**
1. 「Quest 2: AI解析」ノードのプロンプトを確認
2. `出力形式（必ずこの形式で）:` の指示が含まれているか確認
3. AI出力パースノードで実際のAI出力を確認して形式を調整

---

## Google Sheets エラー

### `403 The caller does not have permission`

**原因:** スプレッドシートへのアクセス権限がない

**対処:**
1. Credentials欄でGoogleアカウントを再認証
2. スプレッドシートがGoogleアカウントと同じアカウントのものか確認

---

### `Requested entity was not found`

**原因:** スプレッドシートIDまたはシート名が違う

**対処:**
1. Document IDをURLから再コピー（`/d/` と `/edit` の間の文字列）
2. シート名が「AIニュース監視ログ」と完全一致しているか確認（スペース・全角に注意）

---

## Discord エラー

### Webhookに通知が届かない

**原因:** Webhook URLが間違い、または重要度スコアが70未満

**対処:**
1. IFノードでscoreの値を確認（70未満だと通知しない仕様）
2. Webhook URLをDiscordサーバーで再生成して再設定
3. Discordチャンネルのウェブフック設定で「ウェブフックをテスト」を試す

---

## RSS エラー

### `Could not connect` / RSSが取得できない

**原因:** Feed URLが無効またはサイトがダウン

**対処:**
1. ブラウザでRSS URLを直接開いてXMLが表示されるか確認
2. TechCrunch以外のRSSを試す（NHK: `https://www.nhk.or.jp/rss/news/cat0.xml`）

---

## それでも解決しない場合

n8nの「Execution」ログで詳細なエラーを確認してください。
左メニューの「Executions」から直近の実行ログを開けます。
