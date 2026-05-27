# インポートガイド

ワークフローをn8nに読み込む手順。

---

## ステップ 1: ワークフローをインポートする

1. n8nを開く
2. 左メニューの「Workflows」をクリック
3. 右上の「+ Add workflow」または「New workflow」をクリック
4. 画面右上の「...」メニューを開く
5. 「Import from file」を選択
6. `workflows/quest-01-ai-news-monitor.json` を選択してインポート

インポートが成功すると、6つのノードが表示されます。

---

## ステップ 2: OpenAI 認証情報を設定する

1. 「Quest 2: AI解析」ノードをダブルクリック
2. 「Credential to connect with」フィールドの「+ Add new credential」をクリック
3. 「API Key」フィールドに OpenAI APIキーを入力
4. 「Save」をクリック

---

## ステップ 3: Google Sheets 認証情報を設定する

1. 「Quest 3: Sheets保存」ノードをダブルクリック
2. 「Credential to connect with」の「+ Add new credential」をクリック
3. 「Sign in with Google」でGoogleアカウントを連携
4. 認証が完了したら「Save」をクリック
5. 「Document ID」フィールドに自分のスプレッドシートIDを入力

---

## ステップ 4: Discord Webhook を設定する

1. 「Quest 4: Discord通知」ノードをダブルクリック
2. 「Webhook URI」フィールドに Discord Webhook URLを貼り付け
3. 「Save」をクリック

---

## ステップ 5: 動作確認

1. ワークフロー上部の「Save」ボタンで保存
2. 「Quest 1: RSS接続」ノードを右クリック → 「Execute node」で単体テスト
3. ニュースデータが取得できたら「Test workflow」で全体実行
4. Google Sheetsにデータが記録されたか確認
5. スコア70以上のニュースがあれば Discordに通知が届くか確認

---

## 自動実行を有効にする

動作確認ができたら、ワークフロー右上のトグルをONにして自動実行を有効化します。
15分ごとに自動でニュースをチェックします。
