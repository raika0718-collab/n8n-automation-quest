# Quest 05: AI帝国を完成させよ ★★★★★

```
複数のAI Workerを統率し、
情報帝国を運営せよ。
```

**新要素:** Execute Workflow / Workflow間連携 / エラー処理 / AI Routing

---

## 完成するもの

```
手動または自動起動
  ↓
Worker01 (Quest05専用: ニュースWorker) 実行
Worker02 (Quest05専用: 動画Worker) 実行 ← 並列
  ↓ Merge: 結果統合
OpenAI: 司令AI (優先度判断)
  ↓
Discord: 帝国日次レポート
Sheets: 司令ログ保存
```

---

## Quest 1: AI Workerを召喚せよ

**ノード:** Manual Trigger + Set（ミッション設定）

### 確認ポイント

- [ ] 「Quest 1: ミッション設定」ノードを確認
- [ ] `mission` / `date` / `mode` フィールドを確認
- [ ] missionの内容を変えると司令AIの判断が変わることを理解する

---

## Quest 2: Workflowを連結せよ

**ノード:** Execute Workflow × 2 + Merge

### ⚠️ 重要: ワークフローIDの設定

Execute Workflowノードには、呼び出し先のワークフローIDが必要です。
Quest 01 / Quest 02 本体は定期監視・保存・通知を行うため、司令部からは副作用のない専用 Worker を呼び出します。

**設定手順:**
1. `quest-05-worker-news-analysis.json` と `quest-05-worker-video-topic.json` をn8nにインポートする
2. `Quest 05 Worker: News Analysis` を開く → URLのID部分をコピー
3. `Quest 05 Worker: Video Topic` も同様にIDをコピー
4. 「Quest 2: Worker01 起動」ノードに News Worker のWorkflow IDを入力
5. 「Quest 2: Worker02 起動」ノードに Video Worker のWorkflow IDを入力

### 確認ポイント

- [ ] 両WorkerがMission Setノードから並列で起動しているか確認
- [ ] 両Workerの結果がMergeノード（Appendモード）で統合されるか確認
- [ ] 「結果集約」Codeノードでニュースと動画ネタが分類されるか確認

**ポイント:** Execute Workflowは「n8nの中でn8nを呼ぶ」機能です。
これにより大きなワークフローを小さなモジュールに分けて管理できます。

---

## Quest 3: 司令AIを構築せよ

**ノード:** OpenAI（司令AI）+ Code（レポート生成）

### 確認ポイント

- [ ] 「Quest 3: 司令AI判断」のプロンプトを確認
  - ニュースサマリー + 動画ネタサマリーを渡している
  - 「注目情報 / 優先workflow / 推奨アクション」を出力させる
- [ ] 「Quest 3: 司令レポート生成」でMarkdownレポートが生成されるか確認
- [ ] 司令AIが `priority_wf` に適切なワークフロー名を返すか確認

---

## Quest 4: 障害に耐えられるようにせよ

**エラー処理の設定**

Quest 05は複数のワークフローを呼ぶため、一部が失敗しても止まらない設計が重要です。

### 設定方法

Execute Workflowノードで:
1. ノードをダブルクリック
2. 「Options」を開く
3. 「Continue On Fail」をONにする

これで、Worker01が失敗してもWorker02は動き続けます。

### 確認ポイント

- [ ] 両Execute WorkflowノードでContinue On FailをONにした
- [ ] Worker01を意図的に失敗させてもWorkflow全体が止まらないことを確認

---

## Quest 5: AI帝国を完成させよ

**ノード:** Discord + Google Sheets

### 確認ポイント

- [ ] Discord WebhookとGoogle Sheetsの設定を完了
- [ ] シート名「司令ログ」に記録されるか確認
- [ ] 全体をテスト実行して日次レポートがDiscordに届くか確認

**最終クリア条件:**

- [ ] Quest 05 専用 News Worker と Video Worker が連携して動く
- [ ] 司令AIが「今日の優先行動」を判断できる
- [ ] Discordに統合レポートが届く
- [ ] Sheetsに司令ログが蓄積される

---

## AI帝国 完成

おめでとうございます。

```
Quest 01: AIニュース監視 ← 単独の定期監視
Quest 02: 動画ネタ収集  ← 単独の定期企画収集
Quest 03: 投稿生成工場  ← 制作
Quest 04: 営業監視      ← 収益
Quest 05: AI司令システム ← 専用Workerを使った統括
```

これらすべてが自動で連携し、
毎日あなたのDiscordに日次レポートを届けます。

あなたは自動化ギルドの一流技師になりました。

---

## 次のステップ

- Schedule Triggerで毎朝自動実行するよう設定する
- Quest 03との連携を追加（動画ネタ → 投稿文を自動生成）
- Quest 04との連携を追加（有望リードを司令AIが優先度付け）
- 有料版: 全Quest統合 + AIによる自律的な意思決定ループ
