from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import config
import line_handler

app = Flask(__name__)

# LINE BotのAPIキーの設定
line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名の検証
    signature = request.headers['X-Line-Signature']

    # リクエストボディの取得
    body = request.get_data(as_text=True)

    try:
        # 署名の検証とハンドラの処理
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # ユーザーからのメッセージを取得
    user_message = event.message.text

    # LINEハンドラを通じて応答を生成
    response_message = line_handler.generate_response(user_message)

    # 応答メッセージをLINEに送信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response_message)
    )

if __name__ == "__main__":
    app.run()
