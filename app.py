from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import random


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('XKPBjOTDI9dxcSO5On2+bds/rPqX0W3j5atzg1E7S/1pfzoCly8rT1c8pfs3EPIRnK5duxqzV8+JnBwf2fXPBtj76+xXnYpVc+F8O+qYH9Hx62iSQ1kMdyGBiiu3ebbUsHCDWVJlqUAHyXyHmUCzXQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('8442ec7ac073dddd983212061210a09b')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
  #  flag = 1
#   if flag ==1 :
    #if '最新合作廠商' in msg:
    #   message = imagemap_message()
    #   line_bot_api.reply_message(event.reply_token, message)
    if '哈哈' in msg or '笑死' in msg or 'xd' in msg or 'Xd' in msg or 'XD' in msg or 'xD' in msg:
        s_List=['哈哈','笑死','呵呵',msg]
        message = TextSendMessage(text=random.choice(s_List))
        line_bot_api.reply_message(event.reply_token, message)
    elif '我不是學霸' in msg or '我很爛' in msg or '我爛' in msg:
        s_List=['是的類排一','是的肋排一','再說笑話阿']
        message = TextSendMessage(text=random.choice(s_List))
        line_bot_api.reply_message(event.reply_token, message)
    elif '好喝' in msg :
        message = TextSendMessage(text='好喝')
        line_bot_api.reply_message(event.reply_token, message)
    elif '學霸' in msg or '貓咪' in msg:
        s_List=['貓咪','學霸','肋排一','學爸爸',msg]
        message = TextSendMessage(text=random.choice(s_List))
        line_bot_api.reply_message(event.reply_token, message)
    elif '玩' in msg :
        message = TextSendMessage(text='企鵝遊戲可以玩了')
        line_bot_api.reply_message(event.reply_token, message)
    elif '彩蛋' in msg  :
        s_List=['企鵝還有彩蛋喔','自己去找找彩蛋喔']
        message = TextSendMessage(text=random.choice(s_List))
        line_bot_api.reply_message(event.reply_token, message)
    elif '怎麼走路' in msg :
        message = TextSendMessage(text='像企鵝一樣蹲著走')
        line_bot_api.reply_message(event.reply_token, message)
    elif '企鵝遊戲' in msg :
        message = TextSendMessage(text='企鵝遊戲可以玩了喔~')
        line_bot_api.reply_message(event.reply_token, message)
    elif '探究' in msg :
        message = TextSendMessage(text='來探究企鵝遊戲阿，看誰可以整理好，最接近我寫的規則')
        line_bot_api.reply_message(event.reply_token, message)
    elif '讀書' in msg :
        s_List=['我都不讀的','我都沒讀','我就梅毒']
        message = TextSendMessage(text=random.choice(s_List))
        line_bot_api.reply_message(event.reply_token, message)
    elif '機器人狀態' in msg:
            message = TextSendMessage(text='現在狀態是開啟的' )
            line_bot_api.reply_message(event.reply_token, message)
        



#   else :
#    if '開啟機器人' in msg:
#        flag = 1
#        message = TextSendMessage(text='flag=' + flag+'開啟好了' )
#        line_bot_api.reply_message(event.reply_token, message)
#    elif '機器人狀態' in msg:
#        if flag==0:
#            message = TextSendMessage(text='flag=' + flag+'現在狀態是開啟的' )
#            line_bot_api.reply_message(event.reply_token, message)
#        else :
#            message = TextSendMessage(text='flag=' + flag+'現在狀態是關閉的' )
#          line_bot_api.reply_message(event.reply_token, message)









        #elif '註冊會員' in msg:
        #   message = Confirm_Template()
        #   line_bot_api.reply_message(event.reply_token, message)
        #elif '旋轉木馬' in msg:
        #   message = Carousel_Template()
        #   line_bot_api.reply_message(event.reply_token, message)
        #elif '圖片畫廊' in msg:
        #    message = test()
        #    line_bot_api.reply_message(event.reply_token, message)
        #elif '功能列表' in msg:
        #    message = function_list()
        #    line_bot_api.reply_message(event.reply_token, message)
        #else:
        #    message = TextSendMessage(text='抱歉不支援喔')
        #    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
