import openai
import config

def generate_response(user_message):
    """
    LINEから受け取ったユーザーメッセージに基づいて応答を生成する。

    :param user_message: LINEユーザーからのメッセージ
    :return: GPT-4によって生成された応答テキスト
    """
    try:
        # GPT-4 APIを使用して応答を生成
        response = openai.ChatCompletion.create(
            model="gpt-4.0-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
            api_key=config.OPENAI_API_KEY
        )

        # 応答のテキスト部分を抽出
        response_text = response.choices[0].message['content']
        return response_text

    except Exception as e:
        # 例外が発生した場合、エラーメッセージを返す
        return f"エラーが発生しました: {str(e)}"
