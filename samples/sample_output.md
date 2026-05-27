# サンプル出力

Quest 01が正常に動作したときの出力例。

---

## Google Sheets 保存例

| Date | Title | Summary | Score | URL |
|------|-------|---------|-------|-----|
| 2026-05-27T06:00:00.000Z | OpenAI Launches New Model for Developers | OpenAIが開発者向けの新モデルを発表した。従来比でコストが60%削減され、レスポンス速度が向上。APIは即日利用可能で、スタートアップ向けの無料枠も拡充される。 | 88 | https://techcrunch.com/... |
| 2026-05-27T06:00:00.000Z | Tesla Reports Record Q1 Deliveries | テスラが第1四半期の納車台数で過去最高を記録した。EV市場の競争激化にもかかわらず、モデルYが主力として貢献。株価は発表後に5%上昇した。 | 62 | https://techcrunch.com/... |
| 2026-05-27T06:00:00.000Z | Google Announces AI Coding Assistant Integration | GoogleがIDEに直接統合するAIコーディングアシスタントを発表。GitHub Copilotに対抗する機能で、Gemini 1.5 Proを搭載。VS CodeとJetBrainsに対応予定。 | 91 | https://techcrunch.com/... |

---

## Discord 通知例

スコア70以上の記事のみ通知されます。

```
【重要ニュース】 スコア: 88/100

OpenAI Launches New Model for Developers

OpenAIが開発者向けの新モデルを発表した。従来比でコストが60%削減され、
レスポンス速度が向上。APIは即日利用可能で、スタートアップ向けの無料枠も拡充される。

https://techcrunch.com/2026/05/27/openai-new-model/
```

```
【重要ニュース】 スコア: 91/100

Google Announces AI Coding Assistant Integration

GoogleがIDEに直接統合するAIコーディングアシスタントを発表。
GitHub Copilotに対抗する機能で、Gemini 1.5 Proを搭載。VS CodeとJetBrainsに対応予定。

https://techcrunch.com/2026/05/27/google-ai-coding/
```

---

## スコア判定の目安

| スコア | 判定 | 通知 |
|--------|------|------|
| 90〜100 | 超重要 | Discord通知あり |
| 70〜89 | 重要 | Discord通知あり |
| 50〜69 | 参考 | Sheetsのみ保存 |
| 0〜49 | 低優先 | Sheetsのみ保存 |
