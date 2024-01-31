import openai
import config

def generate_gpt4_response(message):
    """
    GPT-4 APIを使用して応答を生成する。

    :param message: ユーザーからの質問またはコメント
    :return: GPT-4によって生成された応答テキスト
    """
    try:
        # GPT-4 APIを呼び出すためのリクエストを構築
        response = openai.ChatCompletion.create(
            model="gpt-4.0-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant."},
                {"role": "user", "content": message},
            ],
            api_key=config.OPENAI_API_KEY  # APIキーの指定
        )

        # 応答からテキストを抽出
        response_text = response.choices[0].message['content']
        return response_text

    except Exception as e:
        # 例外が発生した場合、エラーメッセージを返す
        return f"エラーが発生しました: {str(e)}"

