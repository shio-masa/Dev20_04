import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('<channel access token>')

def lambda_handler(event, context):
    line_body = json.loads(event['body'])
    for linereq in line_body['events']:
        print(json.dumps(linereq))
        reply_token = linereq['replyToken']
        resp_message = ''
        if 'text' in linereq['message']:
            message = linereq['message']['text']
            if 'こんにちは' in message:
                resp_message = 'こんにちは'
            elif 'おはようございます' in message:
                resp_message = 'おはようございます'
            if resp_message == '':
                resp_message = 'メッセージが分かりませんでした'
            print(resp_message)
            try:
                line_bot_api.reply_message(reply_token, TextSendMessage(text=resp_message))
            except LineBotApiError as e:
            	print(e.error)

    return {
        'statusCode': 200
    }

