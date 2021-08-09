from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#from quickstart import *
#from drive_list import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import random
#======python的函數庫==========
#os.system("python drive_list.py")
#os.system("python quicksart.py")
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
    print('使用者 ID: '+ event.source.user_id)
    #print('群組 ID: '+ event.source.grup_id)
  #  flag = 1
#   if flag ==1 :
    #if '最新合作廠商' in msg:
    #   message = imagemap_message()
    #    
    if '呵呵' in msg or '哈哈' in msg or '笑死' in msg or '好笑' in msg or 'xd' in msg or 'Xd' in msg or 'XD' in msg or 'xD' in msg or 'www' in msg or 'WWW' in msg or '草' in msg:
        s_List=['哈哈','笑死','呵呵',msg,'','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '.jpg' in msg :
        if '哼.jpg' in msg :
            web_Rul = "https://imgur.com/8QZv1A6.jpg"
            message = ImageSendMessage(original_content_url = web_Rul,
            preview_image_url = web_Rul )
        elif '渣男.jpg' in msg :
            web_Rul = "https://i.imgur.com/fxzh9PQ.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '怕.jpg' in msg :
            jpg_List = ["https://i.imgur.com/fu7SJKF.jpg",
                        "https://i.imgur.com/v2IhPib.jpg",
                        "https://i.imgur.com/YzmFIix.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '早安.jpg' in msg :
            web_Rul = "https://i.imgur.com/i9g2f8l.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        #elif '老師.jpg' in msg :
        #    jpg_List = ["https://i.imgur.com/fu7SJKF.jpg",
        #                "https://i.imgur.com/v2IhPib.jpg"]
        #   web_Rul = random.choice(jpg_List)
        #    message = ImageSendMessage(original_content_url= web_Rul,
        #    preview_image_url = web_Rul )
        elif ' ' in msg :
            web_Rul = "https://i.imgur.com/dDKRxY8.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '想不到吧.jpg' in msg :
            jpg_List = ["https://i.imgur.com/IqzJJFb.jpg",
                        "https://i.imgur.com/IqzJJFb.jpg",
                        ]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '我覺得可以.jpg' in msg :
            web_Rul = "https://i.imgur.com/QUbckxF.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '讚.jpg' in msg :
            jpg_List = ["https://i.imgur.com/u49tolz.jpg",
                        "https://i.imgur.com/e6IIlN1.jpg",
                        "https://i.imgur.com/DQkaSyz.jpg",
                        "https://i.imgur.com/OJGNyqu.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif 'NONO.jpg' in msg :
            web_Rul = "https://i.imgur.com/jpA7Jri.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '幹.jpg' in msg or '中指.jpg' in msg :
            jpg_List = ["https://i.imgur.com/AlzNS5X.jpg",
                        "https://i.imgur.com/TlT8Sno.jpg",
                        "https://i.imgur.com/vUSPIdU.jpg",
                        "https://images.chinatimes.com/newsphoto/2021-05-16/656/20210516001265.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '小宇宙.jpg' in msg :
            web_Rul = "https://i.imgur.com/m5O1o3D.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )


        elif '吃我雞雞.jpg' in msg :
            web_Rul = "https://i.imgur.com/Xzfsx7A.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '香.jpg' in msg or '香圖.jpg' in msg :
            jpg_List = ["https://cdn.discordapp.com/attachments/743143275837259897/789460684986646548/IMG_20201218_195129.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/858409895363477533/image0.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/859373224533688340/E5CdbIwVUAAmCsI.jpeg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/857398121487269908/E2rvVXSVEAIpmrn.jpeg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/850302174890426368/image0.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/789460685233848340/IMG_20201218_195102.jpg",
                        "https://i.imgur.com/UQAn4bw.jpg",
                        "https://i.imgur.com/6fh6iGB.gif",
                        "https://i.imgur.com/HzbpX4m.jpg",
                        "https://i.imgur.com/dAuaxBH.jpg",
                        "https://i.imgur.com/84SHWcU.jpg",
                        "https://i.kym-cdn.com/photos/images/original/001/862/458/0d7.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/862679693378584626/868610909c71a033d12d96c47cba61c7.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/862887465126985763/201675839_508116630397633_3460278071530176032_n.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/862952095748980797/1625803366336.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/862954098525863976/E5my2pDVgAAK8VM.jpeg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/863464551189315604/FB_IMG_1625901893000.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/864385966901821490/image0.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/865076320307380234/FB_IMG_1626224150989.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/865916871504166982/illust_91240831_20210717_164118.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/870139119844614194/20210729_083727.jpg",
                        "https://i.imgur.com/k0oGi9p.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707689323180132/FB_IMG_1616037082705.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707689486766100/image2.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707721086631996/90665617_p0_master1200.webp",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707721267019776/89427053_p0_master1200.webp",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707721963274332/89687688_p0_master1200.webp",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707722403663912/ExeX6m1UUAM5kSS.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862661375611109386/image0.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862675218714722314/IMG_20201210_172157.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/862254342014238750/unknown.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/765967898555711568/image0.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/765967706482147378/image0.png",
                        "https://cdn.discordapp.com/attachments/692328953402359889/858327852142297108/unknown.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/850223844979245066/FB_IMG_1622621668500.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/848873039692038154/E2swE2JVEAQoJrg.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/847742144500072508/FB_IMG_1622096978164.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/847137439700353064/80016652_p0.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/794421761906442281/IMG_20201229_125453.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/793708115329679410/illust_83580607_20201227_073406.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/783329509906710528/image0.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/780735371666391040/e09ee89822644cf9dd296e4f56fbe393a7b86a01_raw.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/777482291337101312/82991947_p0_master1200.webp",
                        "https://cdn.discordapp.com/attachments/743143275837259897/772071094869164032/image2.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/769722578624446474/image1.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/769722578427576342/image0.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/768135174717571122/1576503978997.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/765967685904236584/image0.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/765837527378296832/Screenshot_2020-10-13-23-34-33-71.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/761375925438775365/80895234_p1_master1200.webp",
                        "https://cdn.discordapp.com/attachments/743143275837259897/760815883836456970/eyjafjalla_arknights_drawn_by_brs_33143752__sample-11afad2d659c2fd33072e374b7862124.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/760814941778214912/istina_arknights_drawn_by_yunweishukuang__sample-621a78a970b391027bbc59ebee625ff0.png",
                        "https://cdn.discordapp.com/attachments/743143275837259897/758624116672036864/image0.jpg",
                        "https://cdn.discordapp.com/attachments/743143275837259897/745847489151762502/illust_80533974_20200820_113119.jpg",
                        "https://drive.google.com/uc?id=" + "1PsqwNiQl_I6xCxyNvbKpAGfAeBgSlXu3",
                        "https://drive.google.com/uc?id=" + "1rhqmFp39ay6aQUAxjlZFTY24DPOeIWuN",
                        "https://drive.google.com/uc?id=" + "1KZo3aySsy7e8PzOtYl0CX13mNHf2gB0e",
                        "https://drive.google.com/uc?id=" + "1ggunE0E-mmBMqqFxdIDvCJjbZvOjHKi_",
                        "https://drive.google.com/uc?id=" + "1Ht66Svb6sXw6Z2K9j01ONjO37LTSxJLo",
                        "https://drive.google.com/uc?id=" + "1TPQdFIzXnI_0UGwzlWReupIxaJinfY8T",
                        "https://drive.google.com/uc?id=" + "1qAvnGx8lsT5-mV9ukr7ePTS-Fgxq05RI",
                        "https://drive.google.com/uc?id=" + "1PpFY0OeT5MY4LMHIlWlJ4jupfIy6tgvh"]
                        #https://drive.google.com/uc?id=" + "
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url = web_Rul,
            preview_image_url = web_Rul )
        elif "紳士.jpg" in msg:
            jpg_List = ["https://cdn.discordapp.com/attachments/862658693820973096/862660004044341298/20210708_014702.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862662010138001418/IMG_20210627_152255.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862663766549463040/IMG_20201229_070542.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862665851605483520/20201119_221657.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862672571232419860/86955325_p0.png",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862673631254675486/IMG_20201007_003316.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862673686318153748/90970784_p2.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862674453577465866/yande.re_805120_areola_business_suit_cameltoe_loli_mankai_kaika_no_bra_open_shirt_pantsu_pantyhose_p.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862676227336699914/IMG_20200928_085913.jpg",
                        "https://media.discordapp.net/attachments/856180296662908938/856207531319230484/-klbw3Q5-98cwKdToS8o-7o.gif",
                        "https://cdn.discordapp.com/attachments/862658693820973096/862937373406658580/IMG_20210709_135845.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863037207228710942/IMG_20210709_174942.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274228361723914/unknown-2.png",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274326958145546/75699465_p0_master1200.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274334118084648/77750170_p0_master1200.png",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274338407677962/79198695_p0_master1200.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274338878357554/80250175_p0_master1200.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274370352939038/119706411_193001702387730_3399709390101747262_o.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274434042527784/1594271277783.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274557220585502/IMG_20200722_230913.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863274608425697330/illust_83875461_20200823_111252.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/863789745624711188/91124119_p0.png",
                        "https://cdn.discordapp.com/attachments/862658693820973096/864088897423540294/88563264_p1.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/864141662464245800/91197950_p0.png",
                        "https://cdn.discordapp.com/attachments/862658693820973096/866547585175126016/illust_91131647_20210719_130959.png",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707686764654602/FB_IMG_1617025710928.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707687276380160/FB_IMG_1617071001306.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707687695781948/FB_IMG_1617627565937.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707687897112676/FB_IMG_1617627559632.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707688354312212/1b993175228ab73d.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/868707721732558868/188476760_3021679828157087_9001482823598655401_n.jpg",
                        "https://cdn.discordapp.com/attachments/862658693820973096/869517778149847080/FB_IMG_1627379535139.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )

        elif '劉馨榆.jpg' in msg :
            jpg_List = ["https://cdn.discordapp.com/attachments/793784117928919050/861619698818088970/received_339849674181465.jpeg",
                        "https://cdn.discordapp.com/attachments/793784117928919050/839423776290635805/received_211455113824280.jpeg",
                        "https://cdn.discordapp.com/attachments/793784117928919050/839357667730391057/received_148720903877578.jpeg",
                        "https://cdn.discordapp.com/attachments/793784117928919050/826371760898179082/received_143738594240712.jpeg",
                        "https://cdn.discordapp.com/attachments/793784117928919050/826371760613621830/received_1163974684041119.jpeg",
                        "https://cdn.discordapp.com/attachments/793784117928919050/810682770745065502/post_149540338_427429501818867_6961117537140636923_n.jpg",
                        "https://cdn.discordapp.com/attachments/793784117928919050/805361583614197790/FB_IMG_1546526649884.jpg",
                        "https://cdn.discordapp.com/attachments/793784117928919050/805361583424405524/FB_IMG_1546526749457.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        

    elif '@非洲'in msg :
        message = TextSendMessage(text='')
    elif '梅毒' in msg or '沒讀' in msg:
        message = TextSendMessage(text='企鵝就沒讀')

    elif '愛你喔' in msg or '愛你喔 啾咪' in msg:
        s_List=['好甲，我對流星雨是一心一意的','不要誘惑我，我對流星雨是一心一意的','再說笑話阿']
        message = TextSendMessage(text=random.choice(s_List))

    elif '我不是學霸' in msg or '我很爛' in msg :
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
         
   # elif '探究' in msg :
   #     message = TextSendMessage(text='來探究企鵝遊戲阿，看誰可以整理好，最接近企鵝寫的規則')
    elif '來首歌' in msg or '給我一首歌的時間' in msg or '音樂' in msg :
        s_List=['https://www.youtube.com/watch?v=mHmB5mhkuP0',
                'https://www.youtube.com/watch?v=1N5mD2qle7A',
                'https://www.youtube.com/watch?v=AMmDgBXwq9A',
                'https://www.youtube.com/watch?v=Q9L1EqUkQNk',
                'https://www.youtube.com/watch?v=fzQ6gRAEoy0',
                'https://www.youtube.com/watch?v=L2LB12IxLDU',
                'https://www.youtube.com/watch?v=zQ2LfW-DWDc',
                'https://www.youtube.com/watch?v=hpI5vMxYJ_k',
                'https://www.youtube.com/watch?v=N-YuSKeFMxY',
                'https://www.youtube.com/watch?v=uT3SBzmDxGk',
                'https://www.youtube.com/watch?v=-LZxk09LNaM',
                'https://www.youtube.com/watch?v=qAkM8QGLbuo',
                'https://www.youtube.com/watch?v=-x8OXQiwFK4',
                'https://www.youtube.com/watch?v=a-TY-Nbqd_w',
                'https://www.youtube.com/watch?v=yk18LbDnDQU',
                'https://www.youtube.com/watch?v=JqN4_mufE2U',
                'https://www.youtube.com/watch?v=Xj3gU3jACe8',
                'https://www.youtube.com/watch?v=AN0rQR0RlOM',
                'https://www.youtube.com/watch?v=BoAxgDfEIyY',
                'https://www.youtube.com/watch?v=L_REt-KZKCM',
                'https://www.youtube.com/watch?v=dPjdmPAhJWs',
                'https://www.youtube.com/watch?v=gJGlfgEgmDY',
                'https://www.youtube.com/watch?v=sVZpHFXcFJw',
                'https://www.youtube.com/watch?v=_mkiGMtbrPM',
                'https://www.youtube.com/watch?v=fB8TyLTD7EE',
                'https://www.youtube.com/watch?v=YAXTn0E-Zgo',
                'https://www.youtube.com/watch?v=SX_ViT4Ra7k',
                'https://www.youtube.com/watch?v=DuMqFknYHBs',
                'https://www.youtube.com/watch?v=TQ8WlA2GXbk',
                'https://www.youtube.com/watch?v=PDSkFeMVNFs',
                'https://www.youtube.com/watch?v=a2GujJZfXpg',
                'https://www.youtube.com/watch?v=EQ94zflNqn4',
                'https://www.youtube.com/watch?v=-uzuhqQIaTM',
                'https://www.youtube.com/watch?v=a23945btJYw',
                'https://www.youtube.com/watch?v=kUNMc4DLHG0',
                'https://www.youtube.com/watch?v=1_lap6dzSUc',
                'https://www.youtube.com/watch?v=h_wb3LfOMw4',
                'https://www.youtube.com/watch?v=45g3i7P_e7I',
                'https://www.youtube.com/watch?v=68FK7Caserg',
                'https://www.youtube.com/watch?v=z2Thn9ysDTo',
                'https://www.youtube.com/watch?v=xA3px-brPWo',
                'https://www.youtube.com/watch?v=CaksNlNniis',
                'https://www.youtube.com/watch?v=Yw7It7rufZM',
                'https://www.youtube.com/watch?v=HrmuxLlkkOg']
        message = TextSendMessage(text=random.choice(s_List))
        
    elif '讀書' in msg :
        s_List=['我都不讀的','我都沒讀','我就梅毒']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '機器人狀態' in msg:
        message = TextSendMessage(text='現在狀態是開啟的' )
         
    elif '團長' in msg :
        message = TextSendMessage(text='團長唱歌不好聽' )
         
    elif '懷念他'in msg or '上香' in msg or'\|/' in msg:
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
        
        s_List=['晚安呀',
                '晚安哦(•ө•)♡',
                '晚安ㄛ(*´ω｀*)',
                '晚安呀ฅ^•ﻌ•^ฅ',
                '晚安呀(◍•ᴗ•◍)✧*。',
                '晚安呦',
                '晚安囉',
                '晚安呀(´∩｡• ᵕ •｡∩`)',
                '晚安',
                '晚安V●ᴥ●V',
                '晚安呀( ╹▽╹ ) ',
                '晚安ㄛ(*´ω｀*)']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '¿?' in msg :
        message = TextSendMessage(text='¿?是在69 --陳永宸')
         
    elif '義大利麵' in msg :
        message = TextSendMessage(text='有的話，我用鼻孔表演吃義大利麵 --陳永宸')

    elif '冷知識' in msg :
        s_List=['我們身體內一半的 蘿̶莉̶    血小板是從肺製造的',
                '北極熊的毛是透明的，毛是黑色的',
                '科技海綿的原料是三聚氰胺做的喔，不過不要碰到熱水就沒事了。',
                '數據是自然數據，沒有人維修改的，雜亂無章的數據，譬如國家人口、YT影片觀看次數，數據的開頭數字出現機率最高的數字是1喔',
                'Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu這個地方在紐西蘭喔',
                '淡水這個地名的官方使用過的羅馬拼音有三種，Danshui、Tamsui、Tamshui，沒有使用過Dansui',
                'floccinaucinihilipilification是輕蔑的意思',
                '世界歷史上曾消失過十天為1752年5/30~6/8',
                '人類和野生虎鯨的互動致死率是0',
                '現在俄羅斯方塊移動方塊的最快的技巧是rolling',
                '我有一張傳說中拔掉會讓電腦性能倍增的顯卡... GT 210',
                '你知道嗎?GT710的性能比GT720強',
                '你知道組電腦也講風水嗎?',
                '鳳梨在中世紀，被貴族視為可以顯示身份地位的水果，甚至有出租鳳梨服務',
                '頂級的紳士帽子，是用河貍毛氈做的，甚至印地安人為了河貍資源打架，導致各部落人口大量下降',
                '蘇聯人曾經用氫彈滅火、蓋水壩，跟惠惠的工藝不相上下',
                '喝可樂，對肝臟的傷害與喝酒等價',
                '糖的成癮性，比酒比菸比標準成癮物還要強',
                '龍蝦以前是在美洲是奴隸窮人才會吃的食材',
                '鑽石的價格，就是行銷強大力量的展現',
                '美國50年代，有1/3的醫生每天至少抽一包菸',
                '在希臘舉行的奧運，是要裸體參賽的',
                '🔐 😮‍💨是所以關我屁事的意思，🔐 (所以)😮‍(關我)💨(屁事)',
                '我現在像是置身在金星一樣，太陽從西邊升起，而且度日如年'
                '座頭鯨有事沒事就會去用胸鰭拍打虎鯨']
        message = TextSendMessage(text=random.choice(s_List))

    elif '佳句' in msg or '名言' in msg :
        s_List=['有的話，我用鼻孔表演吃義大利麵 --陳永宸',
                '干，你馬子喔---陳占棟',
                '有交無類，有交錢就不分類---陳永宸',
                '陳永宸:\n只要有格子都是稿紙。\n2021/4/1',
                '陳永宸：\n婆蘿們教....\n2021/4/15']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif 'flag' in msg :
        s_List=['有的話，我用鼻孔表演吃義大利麵 --陳永宸',
                'Flag:\n31018陳肋排一如果北模58、59、60的話，就要請全班喝紅茶屋']
        message = TextSendMessage(text=random.choice(s_List))
         

    elif '好油'in msg or '好香'in msg or '真香'in msg  or '舔'in msg or 'peko'in msg :
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
    elif 'FBI' in msg or '蘿莉' in msg:
       # line_bot_api.reply_message(event.reply_token, message='圖片支援')
        web_Rul = "https://i.imgur.com/Ej6FIVL.jpg"
        message = ImageSendMessage(original_content_url= web_Rul,
                                   preview_image_url = web_Rul )
    elif '非洲' in msg :
        web_Rul = "https://www.youtube.com/watch?v=D0dBptGRTvc"
        message = TextSendMessage(text=web_Rul)
            
    line_bot_api.reply_message(event.reply_token, message)
    


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
