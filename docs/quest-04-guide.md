# Quest 04: AI営業監視システムを構築せよ ★★★★

```
ギルドは新たな市場を探している。
価値ある商人を発見せよ。
```

**新要素:** Schedule Trigger / HTTP Request連鎖 / CRM風Sheets管理

---

## 完成するもの

```
6時間ごと自動実行
  ↓
HackerNews 新着20件取得
  ↓
上位5件の詳細取得（HTTP連鎖）
  ↓
ストーリーのみフィルタ（IF）
  ↓
OpenAI: AI需要ポテンシャル分析
  ↓
IF: 需要スコア >= 70
  ↓
Google Sheets: 営業台帳（CRM）保存
  ↓
Discord: 有望リード通知
```

---

## Quest 1: 市場を探索せよ

**ノード:** Schedule Trigger

### 確認ポイント

- [ ] 「Quest 1: 市場巡回スケジューラ」をダブルクリック
- [ ] Interval: 6時間ごとに設定されているか確認
- [ ] 必要に応じて「1日1回」などに変更可能
- [ ] Quest 01はRSS Trigger（受動的）だったが、こちらはSchedule Trigger（能動的）
  - 違いを理解する

**ポイント:** Schedule Triggerは「決まった時間に自動で動く」タイプのトリガーです。

---

## Quest 2: 企業情報を収集せよ

**ノード:** HTTP Request × 2（連鎖）

### 確認ポイント

- [ ] 「Quest 2: HN新着取得」のURLを確認
  - `https://hacker-news.firebaseio.com/v0/newstories.json`
  - これで記事IDの配列が返ってくる
- [ ] 「ID抽出」Codeノードで上位5件のIDに絞られているか確認
- [ ] 「Quest 2: ストーリー詳細取得」のURLを確認
  - `https://hacker-news.firebaseio.com/v0/item/{{ $json.story_id }}.json`
  - 動的URLで各記事の詳細を取得している
- [ ] 5件がそれぞれ並列処理されることを確認

**ポイント:** HTTPリクエストを連鎖させることで、
「IDを取得 → 詳細を取得」の2段階APIアクセスが実現できます。

---

## Quest 3: AIに需要分析をさせよ

**ノード:** OpenAI

### 確認ポイント

- [ ] 「Quest 3: AI需要分析」のプロンプトを確認
  - 業務効率化・データ処理・意思決定支援の観点でスコア評価
- [ ] 「スコア抽出」Codeノードで `demand_score` と `reason` が取れているか確認
- [ ] ストーリーのみフィルタ（IFノード）を通過したデータが処理されているか確認

---

## Quest 4: 有望な相手だけを残せ

**ノード:** IF

### 確認ポイント

- [ ] 「Quest 4: 見込み判定 (>=70)」の条件を確認
- [ ] True側（スコア70以上）だけが営業台帳に保存される
- [ ] テスト実行して何件が70以上だったか確認

---

## Quest 5: 営業台帳を完成させよ

**ノード:** Google Sheets（CRM）+ Discord

### 確認ポイント

- [ ] シート名「営業台帳」に保存される列を確認
  - Date / Title / URL / HN_Score / DemandScore / Reason / AI_Proposal / Status
- [ ] **Status列が「未接触」になっている** → 実際の営業管理に使える
- [ ] Discord通知で「有望リード発見」メッセージが届くか確認
- [ ] Google SheetsでStatusを手動で「検討中」「済み」に変えてCRMとして使える

**ポイント:** Sheets + Status列でCRM（顧客管理）の基本形が完成します。

---

## クリア条件

- [ ] HackerNewsから新着情報を自動取得できる
- [ ] AIが需要スコアと理由を生成できる
- [ ] 70点以上のリードだけが台帳に保存される
- [ ] Discord通知が届く
- [ ] Sheetsで営業ステータスを管理できる

---

## 注意事項

- このシステムは情報収集・分析のみです
- 実際の営業活動（メール送信・DM等）は手動で行ってください
- 本番の営業ツールとして使う場合はStatus管理を徹底してください
