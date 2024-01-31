# LINE Bot with GPT-4 Integration

このプロジェクトは、LINEの公式アカウントとOpenAIのGPT-4 APIを統合したチャットボットです。

## 機能

- LINEからのメッセージを受信し、GPT-4を使用して応答します。
- 特定のユーザーの質問にカスタマイズされた回答を生成します。

## 前提条件

このプロジェクトを実行するには、以下が必要です：

- Python 3.6以上
- LINEの公式アカウント
- OpenAIのAPIキー

## セットアップ手順

1. 依存関係のインストール:
pip install -r requirements.txt

2. `config.py` ファイルに必要なAPIキーを設定します。

3. アプリケーションを実行します:
python main.py

## 使用方法

1. LINEアプリで、ボットのLINE公式アカウントにメッセージを送信します。
2. 自動的に応答が返されます。

## ライセンス

[MIT License](LICENSE)

## コントリビューション

プルリクエストやフィードバックは大歓迎です。貢献に関する詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。
