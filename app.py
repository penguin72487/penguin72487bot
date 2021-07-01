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
    #    
    if '呵呵' in msg or '哈哈' in msg or '笑死' in msg or 'xd' in msg or 'Xd' in msg or 'XD' in msg or 'xD' in msg:
        s_List=['哈哈','笑死','呵呵',msg,'','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '.jpg' in msg :
        if '哼.jpg' in msg :
            web_Rul = "https://imgur.com/8QZv1A6" + ".jpg"
            message = ImageSendMessage(original_content_url = web_Rul,
            preview_image_url = web_Rul )
        elif '渣男.jpg' in msg :
            message = ImageSendMessage(original_content_url = "https://imgur.com/fxzh9PQ" + ".jpg",
            preview_image_url = "https://imgur.com/fxzh9PQ" +".jpg" )

             
    elif '我不是學霸' in msg or '我很爛' in msg or '我爛' in msg:
        s_List=['是的類排一','是的肋排一','再說笑話阿']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '好喝' in msg :
        message = TextSendMessage(text='好喝')
         
    elif '學霸' in msg or '貓咪' in msg:
        s_List=['貓咪','學霸','肋排一','學爸爸',msg]
        message = TextSendMessage(text=random.choice(s_List))
         
    #elif '玩' in msg :
    #    message = TextSendMessage(text='企鵝遊戲可以玩了')
    #     
    #elif '彩蛋' in msg  :
     #   s_List=['企鵝還有彩蛋喔','自己去找找彩蛋喔']
     #   message = TextSendMessage(text=random.choice(s_List))
     #    
    elif '怎麼走路' in msg :
        message = TextSendMessage(text='像企鵝一樣蹲著走')
         
    elif '企鵝遊戲' in msg :
        message = TextSendMessage(text='企鵝遊戲可以玩了喔~')
         
    elif '探究' in msg :
        message = TextSendMessage(text='來探究企鵝遊戲阿，看誰可以整理好，最接近企鵝寫的規則')
         
    elif '讀書' in msg :
        s_List=['我都不讀的','我都沒讀','我就梅毒']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '機器人狀態' in msg:
        message = TextSendMessage(text='現在狀態是開啟的' )
         
    elif '團長' in msg :
        message = TextSendMessage(text='團長唱歌不好聽' )
         
    elif '\|/' in msg:
        message = TextSendMessage(text='\|/' )
         
    elif '節奏樂隊' in msg :
        message = TextSendMessage(text='企鵝跟流星雨遇見的方' )
         
    elif '渣男' in msg :
        message = TextSendMessage(text='對不起，企鵝也當過渣男' )
         
    elif '五等分'  in msg :
        message = TextSendMessage(text='企鵝是買五月股的' )
         
    elif '在下求稿' in msg :
        message = TextSendMessage(text='在地下城尋求邂逅是否搞錯了甚麼?' )
         
    elif '許迎萱' in msg :
        message = TextSendMessage(text='我再說一次，企鵝對她沒感覺' )
         
    elif '偷看' in msg :
        message = TextSendMessage(text='企鵝在打定音的時候，都喜歡偷看美女，至於美女是誰就不多說了')
         
    elif '宙斯' in msg or '貝爾爺爺' in msg :
        s_List=['誇獎女生的時候，要誇獎到她害羞地說不出話為止',
                '偷窺可是是男人的浪漫啊! 是浪浪浪浪...浪漫啊!',
                '唯有賭上性命的人，才能稱之為英雄。\n保護同伴，拯救女人，賭上自己吧!遇到挫折也沒關係，受到打擊也無訪，盡情哭泣吧!\n失敗為成功之母。貫徹自己的願望，喊出自己的想法。\n如此一來，那才是這是世上最頂天立地的英雄。']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '空白' in msg :
        message = TextSendMessage(text='')
         
    elif '月色' in msg :
        message = TextSendMessage(text='蛤甚麼?你今天月色真美')
         
    elif '晚安' in msg :
        message = TextSendMessage(text=' 晚安哦(•ө•)♡')
         
    elif '¿?' in msg :
        message = TextSendMessage(text='¿?是在69 --陳永宸')
         
    elif '義大利麵' in msg :
        message = TextSendMessage(text='有的話，我用鼻孔表演吃義大利麵 --陳永宸')
          
    elif '佳句' in msg or '名言' in msg :
        s_List=['有的話，我用鼻孔表演吃義大利麵 --陳永宸','干，你馬子喔---陳占棟',
                '有交無類，有交錢就不分類---陳永宸',
                '陳永宸:\n只要有格子都是稿紙。\n2021/4/1',
                '陳永宸：\n婆蘿們教....\n2021/4/15']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif 'flag' in msg :
        s_List=['有的話，我用鼻孔表演吃義大利麵 --陳永宸',
                'Flag:\n31018陳肋排一如果北模58、59、60的話，就要請全班喝紅茶屋']
        message = TextSendMessage(text=random.choice(s_List))
         

    elif '好油'in msg or '好香'in msg or '舔'in msg or 'peko'in msg :
        s_List=['要不要peko茶',
                '我要配cola',
                '好油喔peko']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '梗圖' in msg :
        message = TextSendMessage(text='鯊鯊好可愛')
         
    elif '白嫖仔' in msg :
        message = TextSendMessage(text='好香')
         
    elif '怠惰' in msg or '懶' in msg or '算了' in msg :
        s_List=['怠惰怠惰怠惰','你還真是怠惰呢']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '流星雨' in msg or '劉馨榆' in msg:
        s_List=['企鵝喜歡的','企鵝喜歡看']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '機器人自我介紹' in msg :
        message = TextSendMessage(text='我是怠惰司教，貝特魯吉烏斯·羅曼尼康帝，自從醒來以後，就在企鵝王底下工作了')
         
    elif '顏藝滿分' in msg :
        message = TextSendMessage(text='顏藝滿分')
    line_bot_api.reply_message(event.reply_token, message)
    

    
        





#   else :
#    if '開啟機器人' in msg:
#        flag = 1
#        message = TextSendMessage(text='flag=' + flag+'開啟好了' )
#         
#    elif '機器人狀態' in msg:
#        if flag==0:
#            message = TextSendMessage(text='flag=' + flag+'現在狀態是開啟的' )
#             
#        else :
#            message = TextSendMessage(text='flag=' + flag+'現在狀態是關閉的' )
#           









        #elif '註冊會員' in msg:
        #   message = Confirm_Template()
        #    
        #elif '旋轉木馬' in msg:
        #   message = Carousel_Template()
        #    
        #elif '圖片畫廊' in msg:
        #    message = test()
        #     
        #elif '功能列表' in msg:
        #    message = function_list()
        #     
        #else:
        #    message = TextSendMessage(text='抱歉不支援喔')
        #     

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
