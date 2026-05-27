# Quest 02: AI動画ネタ収集システムを構築せよ ★★

```
情報都市では、毎日大量の動画が生まれている。
ギルドは「伸びるネタ」を発見できる技師を求めている。
```

**新要素:** HTTP Request / Merge / データ統合

---

## 完成するもの

```
RSS(TechCrunch)
  +
Reddit /r/technology
  ↓ データ統合
OpenAI: バズネタ変換 + スコア
  ↓
Google Sheets: 動画ネタ帳
  ↓ スコア70以上
Discord: 高スコアネタ報告
```

---

## Quest 1: 情報源を回収せよ

**ノード:** RSS Feed Trigger + HTTP Request

### 確認ポイント

- [ ] 「Quest 1: RSS接続」がTechCrunchのRSSを監視している
- [ ] 「Quest 1: Reddit取得」が Reddit API に接続している
  - URL: `https://www.reddit.com/r/technology/hot.json?limit=5`
  - 認証不要（公開API）
- [ ] RSS接続ノードから2方向に矢印が出ているか確認
  - 上の矢印 → 記事データ抽出ノード
  - 下の矢印 → Reddit取得ノード

**ポイント:** 1つのトリガーから複数のノードに分岐できます（fan-out）。

---

## Quest 2: 話題を統合せよ

**ノード:** Merge

### 確認ポイント

- [ ] 「Quest 2: データ統合」ノードをダブルクリック
- [ ] Mode が「Append」になっているか確認
- [ ] 入力が2本（RSS側 + Reddit側）繋がっているか確認
- [ ] 「コンテキスト構築」Codeノードで統合データを確認
  - RSS記事 + Redditトレンド上位3件が1つのアイテムになっている

**ポイント:** Mergeノードの「Append」は全アイテムを結合します。
「Combine」は位置合わせで結合、「Multiplex」は全組み合わせを生成します。

---

## Quest 3: AIに動画ネタ化させよ

**ノード:** OpenAI

### 確認ポイント

- [ ] 「Quest 3: AI動画ネタ化」ノードをダブルクリック
- [ ] OpenAI APIキーが設定されているか確認
- [ ] プロンプトを確認 — 記事タイトル + Redditトレンドの両方を活用
- [ ] 出力形式「タイトル: / フック: / 概要: / スコア:」を確認
- [ ] テスト実行してAI出力を確認

---

## Quest 4: 価値あるネタだけを残せ

**ノード:** IF

### 確認ポイント

- [ ] 「Quest 4: スコア判定 (>=70)」ノードをダブルクリック
- [ ] 条件: `score >= 70` になっているか確認
- [ ] True側（上）→ Discord報告に繋がっているか
- [ ] False側（下）→ 何も繋がっていない（通知しない）

---

## Quest 5: ギルドへ報告せよ

**ノード:** Google Sheets + Discord

### 確認ポイント

- [ ] 「Quest 5: ネタ帳保存」のシート名が「動画ネタ帳」になっているか
- [ ] 列: Date, VideoTitle, Hook, Summary, Score, SourceURL
- [ ] Discord Webhook URLを設定
- [ ] テスト実行 → Sheetsに記録 + スコア70以上でDiscord通知

---

## クリア条件

- [ ] RSSとRedditの両方からデータを取得できる
- [ ] Mergeノードで統合できる
- [ ] AIが「タイトル/フック/概要/スコア」形式で出力している
- [ ] Sheetsに動画ネタが記録される
- [ ] スコア70以上でDiscordに通知が届く

---

## カスタムクエスト

- RSSを日本語ニュースサイトに変える（NHK, ITmedia等）
- Redditのサブレディットを変える（r/artificial, r/MachineLearning等）
- スコア閾値を変えて通知頻度を調整
- フックのスタイルをプロンプトで変更（疑問型、衝撃事実型等）
