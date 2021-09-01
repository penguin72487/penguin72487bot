from __future__ import print_function
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



#======???裡�?��?��?��??�?�???�容=====
from message import *
from new import *
from Function import *
#from quickstart import *
#from drive_list import *
#======???裡�?��?��?��??�?�???�容=====

#======python?????��?�庫==========
import tempfile, os
import datetime
import time
import random
#======python?????��?�庫==========
#os.system("python drive_list.py")
#os.system("python quicksart.py")

#======??��?�google drive api==========

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('XKPBjOTDI9dxcSO5On2+bds/rPqX0W3j5atzg1E7S/1pfzoCly8rT1c8pfs3EPIRnK5duxqzV8+JnBwf2fXPBtj76+xXnYpVc+F8O+qYH9Hx62iSQ1kMdyGBiiu3ebbUsHCDWVJlqUAHyXyHmUCzXQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('8442ec7ac073dddd983212061210a09b')
"""Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('drive', 'v3', credentials=creds)

# Call the Drive v3 API
results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))



# ?????��?????�???? /callback ??? Post Request
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


# ??????�????
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print('使�?��?? ID: '+ event.source.user_id)
    #print('群�?? ID: '+ event.source.grup_id)
  #  flag = 1
#   if flag ==1 :
    #if '?????��??�?�????' in msg:
    #   message = imagemap_message()
    #    
    if '??��??' in msg or '??????' in msg or '�?�?' in msg or '好�??' in msg or 'xd' in msg or 'Xd' in msg or 'XD' in msg or 'xD' in msg or 'www' in msg or 'WWW' in msg or '???' in msg:
        s_List=['??????','�?�?','??��??',msg,'','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        message = TextSendMessage(text=random.choice(s_List))
    elif '??��??'in msg: #?????�測試�??

        message = TextSendMessage(text='')
        
    elif '.jpg' in msg :
        if '???.jpg' in msg :
            web_Rul = "https://imgur.com/8QZv1A6.jpg"
            message = ImageSendMessage(original_content_url = web_Rul,
            preview_image_url = web_Rul )
        elif '�????.jpg' in msg :
            web_Rul = "https://i.imgur.com/fxzh9PQ.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '???.jpg' in msg :
            jpg_List = ["https://i.imgur.com/fu7SJKF.jpg",
                        "https://i.imgur.com/v2IhPib.jpg",
                        "https://i.imgur.com/YzmFIix.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '??��??.jpg' in msg :
            web_Rul = "https://i.imgur.com/i9g2f8l.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        #elif '???�?.jpg' in msg :
        #    jpg_List = ["https://i.imgur.com/fu7SJKF.jpg",
        #                "https://i.imgur.com/v2IhPib.jpg"]
        #   web_Rul = random.choice(jpg_List)
        #    message = ImageSendMessage(original_content_url= web_Rul,
        #    preview_image_url = web_Rul )
        elif ' ' in msg :
            web_Rul = "https://i.imgur.com/dDKRxY8.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '??��????��??.jpg' in msg :
            jpg_List = ["https://i.imgur.com/IqzJJFb.jpg",
                        "https://i.imgur.com/IqzJJFb.jpg",
                        ]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '???覺�????�以.jpg' in msg :
            web_Rul = "https://i.imgur.com/QUbckxF.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '�?.jpg' in msg :
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
        elif '�?.jpg' in msg or '中�??.jpg' in msg :
            jpg_List = ["https://i.imgur.com/AlzNS5X.jpg",
                        "https://i.imgur.com/TlT8Sno.jpg",
                        "https://i.imgur.com/vUSPIdU.jpg",
                        "https://images.chinatimes.com/newsphoto/2021-05-16/656/20210516001265.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '�?�?�?.jpg' in msg :
            web_Rul = "https://i.imgur.com/m5O1o3D.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )


        elif '????????????.jpg' in msg :
            web_Rul = "https://i.imgur.com/Xzfsx7A.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '�?.jpg' in msg or '�????.jpg' in msg :
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

        elif '???馨�??.jpg' in msg :
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
        

    elif '@???�?'in msg :
        message = TextSendMessage(text='')
    elif '�?�?' in msg or '�?�?' in msg:
        message = TextSendMessage(text='�?�?就�??�?')

    elif '???�????' in msg or '???�???? ??��??' in msg:
        s_List=['好�?��?????�?�??????��?��??�?�???????','�?�?�???????�????�?�??????��?��??�?�???????','???說�??話�??']
        message = TextSendMessage(text=random.choice(s_List))

    elif '???�???�學???' in msg or '???�????' in msg :
        s_List=['??��??�????�?','??��????????�?','???說�??話�??']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '好�??' in msg :
        message = TextSendMessage(text='好�??')
         
    elif '學�??' in msg or '�????' in msg:
        s_List=['�????','學�??','??????�?','學�?��??',msg]
        message = TextSendMessage(text=random.choice(s_List))
         
    #elif '???' in msg :
    #    message = TextSendMessage(text='�?�??????��?�以??��??')
    #     
    #elif '彩�??' in msg  :
     #   s_List=['�?�???????彩�?????','??�己??��?��?�彩??????']
     #   message = TextSendMessage(text=random.choice(s_List))
     #    
    elif '???麼走�?' in msg :
        message = TextSendMessage(text='???�?�?�?�?蹲�??�?')
         
    elif '�?�???????' in msg :
        message = TextSendMessage(text='�?�??????��?�以??��?????~')
         
   # elif '??�究' in msg :
   #     message = TextSendMessage(text='�???�究�?�??????��?��?????誰�?�以??��??好�???????��??�?�?寫�??�????')
    elif '�?�?�?' in msg or '給�??�?�?�??????????' in msg or '??��??' in msg :
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
        
    elif '�????' in msg :
        s_List=['?????��??�????','?????��??�?','???就�??�?']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�???�人??????' in msg:
        message = TextSendMessage(text='??��?��???????��????????' )
         
    elif '??????' in msg :
        message = TextSendMessage(text='?????��?��??�?好�??' )
         
    elif '??�念�?'in msg or '�?�?' in msg or'\|/' in msg:
        message = TextSendMessage(text='\|/' )

    elif '�?�?�????' in msg :
        message = TextSendMessage(text='�?�?�?�??????��??�???????' )
         
    elif '�????' in msg :
        message = TextSendMessage(text='�?�?起�??�?�?�???��??�????' )
         
    elif '�?�????'  in msg :
        message = TextSendMessage(text='�?�???�買�??????��??' )
         
    elif '??��??�?�?' in msg :
        message = TextSendMessage(text='??��?��?????�?�?????????��?��????��?????�??' )
         
    elif '許�?????' in msg :
        message = TextSendMessage(text='??????說�??次�??�?�?�?她�?????�?' )
         
    elif '??��??' in msg :
        message = TextSendMessage(text='�?�???��??�???��????????�???��??歡�?��??�?女�????��?��??女�?�誰就�??�?說�??')
         
    elif '�????' in msg or '�???��?��??' in msg :
        s_List=['�????女�???????????�?�?�??????�她害�????�說�???�話??�止',
                '??�窺??��?��?��?�人???浪漫???! ??�浪浪浪�?...浪漫???!',
                '??��??賭�????��?��??人�???????�稱�???��?��?????\n�?護�??伴�????��??女人�?賭�????�己???!?????��?��??�?�????�?�??????��?????�???�訪�???��????�泣???!\n失�????��?????�?�????貫徹??�己???�????�??????��?�己?????��?????\n�?此�??�?�?????????��????��??�???????天�????��????��?????']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '空�??' in msg :
        message = TextSendMessage(text='')
         
    elif '??????' in msg :
        message = TextSendMessage(text='??��??�??�?�?天�????��??�?')
        
    elif '??????' in msg :
        s_List=["大�??",
                "???",
                "中�??",
                "�????",
                "??��??",
                "???",
                "�?確�???�???????"]
        message = TextSendMessage(text=random.choice(s_List))

    elif '???�?' in msg :
        
        s_List=['???�????',
                '???�????(??�ө�??)???',
                '???�????(*´??�?*)',
                '???�????�?^??��????�^�?',
                '???�????(?????��????��??)???*???',
                '???�????',
                '???�????',
                '???�????(´??�｡??? �? ??�｡??�`)',
                '???�?',
                '???�?V???ᴥ�??V',
                '???�????( ??��?��?? ) ',
                '???�????(*´??�?*)']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '¿?' in msg :
        message = TextSendMessage(text='¿???��??69 --??�永�?')
         
    elif '義大??�麵' in msg :
        message = TextSendMessage(text='??????話�???????�鼻�?表�?????義大??�麵 --??�永�?')

    elif '??��?��??' in msg :
        s_List=['??????身�????��???????? ??�̶�??̶    �?�???��?��????�製??????',
                '???極�?????�???��????????�?�???��????��??',
                '�????海綿???????????��?????氰�?��????????�?�????�?�?碰�?��?�水就�??�?�????',
                '??��????��?��?��?��??�?�????人維修�?��??�????�???��???????��??�?譬�?????家人??????YT影�??�????次�?��????��??????????��?��????��?��????????�??????��?????1???',
                'Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu????????��?��?��??西�?��??',
                '淡水????????��?????�???�使??��?????�?馬�?��?��??�?種�??Danshui???Tamsui???Tamshui�?�????使�?��??Dansui',
                'floccinaucinihilipilification??��??????????????',
                '�????歷�?��????��??失�?????天�??1752�?5/30~6/8',
                '人�??????????????鯨�??�??????�死??????0',
                '??��?��??�???��?��??移�????��????????快�?????巧�?�rolling',
                '??????�?張�?�說中�????????�???��?��?��?��??�????顯�??... GT 210',
                '�???��??????GT710?????��?��??GT720�?',
                '�???��??�???��?��??�?風水????',
                '鳳梨??�中�?�?�?被貴???�???��?�以顯示身份??��?????水�??�??????��????��??鳳梨??????',
                '???�????紳士帽�??�???��?�河�?�?�???????�??????��?��?��??人�?��??河�??�?�??????��??�???��????��?�人???大�??�????',
                '?????�人??��????�氫�?�???��?????水壩�?�??????????工�??�???��??�?',
                '?????��??�?�????????????�害?????????�????',
                '�?????????��?��??�????�???��??�?�??????��?��??�?�?',
                '�???�以?????��?��??洲�?�奴??�窮人�???????????�????',
                '??��?��????��?��??就�?��????�強大�????????�????',
                '�????50年代�????1/3?????��??�?天�?��????��????????',
                '??��????????�????奧�??�???��??裸�?????賽�??',
                '???? ???��?????��?��??以�?????�?�??????????�????? (???�?)???��??(??????)????(�?�?)',
                '?????��?��????�置身�?��?????�?�?�?太�?��??西�?????起�?????�?度�?��??�?'
                '座�?�鯨???�?�?�?就�????��?��?�鰭?????????�?']
        message = TextSendMessage(text=random.choice(s_List))

    elif '佳�??' in msg or '???�?' in msg :
        s_List=['??????話�???????�鼻�?表�?????義大??�麵 --??�永�?',
                '干�??�?馬�?????---??��??�?',
                '???交�?��??�????交�?�就�????�?---??�永�?',
                '??�永�?:\n??��???????��????��?�稿�????\n2021/4/1',
                '??�永宸�??\n�???��?????....\n2021/4/15']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif 'flag' in msg :
        s_List=['??????話�???????�鼻�?表�?????義大??�麵 --??�永�?',
                'Flag:\n31018??��?????�?�???????�?58???59???60???話�??就�??�???��?��??�???��??']
        message = TextSendMessage(text=random.choice(s_List))
         

    elif '好油'in msg or '好�??'in msg or '???�?'in msg  or '???'in msg or 'peko'in msg :
        s_List=['�?�?�?peko???',
                '???�????cola',
                '好油???peko']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�????' in msg :
        message = TextSendMessage(text='�?�?好�?��??')
         
    elif '??��??�?' in msg :
        message = TextSendMessage(text='好�??')
         
    elif '??????' in msg or '???' in msg or '�?�?' in msg :
        s_List=['?????��????��?????','�?????????��????��??']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�???????' in msg or '???馨�??' in msg:
        s_List=['�?�????歡�??','�?�????歡�??','�?�????歡�??馨�??']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�???�人??��??�?�?' in msg :
        message = TextSendMessage(text='?????��????��?��??�?�???�魯????????�·�????�尼康�??�???��?????�?以�??�?就�?��??�????�?�?工�??�?')     

    elif '�????滿�??' in msg :
        message = TextSendMessage(text='�????滿�??')

    elif 'FBI' in msg or '??��??' in msg:
       # line_bot_api.reply_message(event.reply_token, message='????????��??')
        web_Rul = "https://i.imgur.com/Ej6FIVL.jpg"
        message = ImageSendMessage(original_content_url= web_Rul,
                                   preview_image_url = web_Rul )
    elif '???�?' in msg :
        web_Rul = "https://www.youtube.com/watch?v=D0dBptGRTvc"
        message = TextSendMessage(text=web_Rul)
            
    line_bot_api.reply_message(event.reply_token, message)
    


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
