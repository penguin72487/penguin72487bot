from __future__ import print_function
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



#======�o�̬O�I�s���ɮפ��e=====
from message import *
from new import *
from Function import *
#from quickstart import *
#from drive_list import *
#======�o�̬O�I�s���ɮפ��e=====

#======python����Ʈw==========
import tempfile, os
import datetime
import time
import random
#======python����Ʈw==========
#os.system("python drive_list.py")
#os.system("python quicksart.py")

#======�n�Jgoogle drive api==========

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



# ��ť�Ҧ��Ӧ� /callback �� Post Request
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


# �B�z�T��
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print('�ϥΪ� ID: '+ event.source.user_id)
    #print('�s�� ID: '+ event.source.grup_id)
  #  flag = 1
#   if flag ==1 :
    #if '�̷s�X�@�t��' in msg:
    #   message = imagemap_message()
    #    
    if '����' in msg or '����' in msg or '����' in msg or '�n��' in msg or 'xd' in msg or 'Xd' in msg or 'XD' in msg or 'xD' in msg or 'www' in msg or 'WWW' in msg or '��' in msg:
        s_List=['����','����','����',msg,'','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        message = TextSendMessage(text=random.choice(s_List))
    elif '�o��'in msg: #�\����հ�

        message = TextSendMessage(text='')
        
    elif '.jpg' in msg :
        if '��.jpg' in msg :
            web_Rul = "https://imgur.com/8QZv1A6.jpg"
            message = ImageSendMessage(original_content_url = web_Rul,
            preview_image_url = web_Rul )
        elif '��k.jpg' in msg :
            web_Rul = "https://i.imgur.com/fxzh9PQ.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '��.jpg' in msg :
            jpg_List = ["https://i.imgur.com/fu7SJKF.jpg",
                        "https://i.imgur.com/v2IhPib.jpg",
                        "https://i.imgur.com/YzmFIix.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '���w.jpg' in msg :
            web_Rul = "https://i.imgur.com/i9g2f8l.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        #elif '�Ѯv.jpg' in msg :
        #    jpg_List = ["https://i.imgur.com/fu7SJKF.jpg",
        #                "https://i.imgur.com/v2IhPib.jpg"]
        #   web_Rul = random.choice(jpg_List)
        #    message = ImageSendMessage(original_content_url= web_Rul,
        #    preview_image_url = web_Rul )
        elif ' ' in msg :
            web_Rul = "https://i.imgur.com/dDKRxY8.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '�Q����a.jpg' in msg :
            jpg_List = ["https://i.imgur.com/IqzJJFb.jpg",
                        "https://i.imgur.com/IqzJJFb.jpg",
                        ]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '��ı�o�i�H.jpg' in msg :
            web_Rul = "https://i.imgur.com/QUbckxF.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '�g.jpg' in msg :
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
        elif '�F.jpg' in msg or '����.jpg' in msg :
            jpg_List = ["https://i.imgur.com/AlzNS5X.jpg",
                        "https://i.imgur.com/TlT8Sno.jpg",
                        "https://i.imgur.com/vUSPIdU.jpg",
                        "https://images.chinatimes.com/newsphoto/2021-05-16/656/20210516001265.jpg"]
            web_Rul = random.choice(jpg_List)
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '�p�t�z.jpg' in msg :
            web_Rul = "https://i.imgur.com/m5O1o3D.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )


        elif '�Y������.jpg' in msg :
            web_Rul = "https://i.imgur.com/Xzfsx7A.jpg"
            message = ImageSendMessage(original_content_url= web_Rul,
            preview_image_url = web_Rul )
        elif '��.jpg' in msg or '����.jpg' in msg :
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
        elif "�Ԥh.jpg" in msg:
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

        elif '�B�ɷ�.jpg' in msg :
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
        

    elif '@�D�w'in msg :
        message = TextSendMessage(text='')
    elif '���r' in msg or '�SŪ' in msg:
        message = TextSendMessage(text='���Z�N�SŪ')

    elif '�R�A��' in msg or '�R�A�� ��}' in msg:
        s_List=['�n�ҡA�ڹ�y�P�B�O�@�ߤ@�N��','���n���b�ڡA�ڹ�y�P�B�O�@�ߤ@�N��','�A�����ܪ�']
        message = TextSendMessage(text=random.choice(s_List))

    elif '�ڤ��O���Q' in msg or '�ګ���' in msg :
        s_List=['�O�����Ƥ@','�O���رƤ@','�A�����ܪ�']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�n��' in msg :
        message = TextSendMessage(text='�n��')
         
    elif '���Q' in msg or '�߫}' in msg:
        s_List=['�߫}','���Q','�رƤ@','�Ǫ���',msg]
        message = TextSendMessage(text=random.choice(s_List))
         
    #elif '��' in msg :
    #    message = TextSendMessage(text='���Z�C���i�H���F')
    #     
    #elif '�m�J' in msg  :
     #   s_List=['���Z�٦��m�J��','�ۤv�h���m�J��']
     #   message = TextSendMessage(text=random.choice(s_List))
     #    
    elif '��򨫸�' in msg :
        message = TextSendMessage(text='�����Z�@���۵ۨ�')
         
    elif '���Z�C��' in msg :
        message = TextSendMessage(text='���Z�C���i�H���F��~')
         
   # elif '���s' in msg :
   #     message = TextSendMessage(text='�ӱ��s���Z�C�����A�ݽ֥i�H��z�n�A�̱�����Z�g���W�h')
    elif '�ӭ��q' in msg or '���ڤ@���q���ɶ�' in msg or '����' in msg :
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
        
    elif 'Ū��' in msg :
        s_List=['�ڳ���Ū��','�ڳ��SŪ','�ڴN���r']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�����H���A' in msg:
        message = TextSendMessage(text='�{�b���A�O�}�Ҫ�' )
         
    elif '�Ϊ�' in msg :
        message = TextSendMessage(text='�Ϊ��ۺq���nť' )
         
    elif '�h���L'in msg or '�W��' in msg or'\|/' in msg:
        message = TextSendMessage(text='\|/' )

    elif '�`���ֶ�' in msg :
        message = TextSendMessage(text='���Z��y�P�B�J������' )
         
    elif '��k' in msg :
        message = TextSendMessage(text='�藍�_�A���Z�]��L��k' )
         
    elif '������'  in msg :
        message = TextSendMessage(text='���Z�O�R����Ѫ�' )
         
    elif '�b�U�D�Z' in msg :
        message = TextSendMessage(text='�b�a�U���M�D�۰m�O�_�d���F�ƻ�?' )
         
    elif '�\�︩' in msg :
        message = TextSendMessage(text='�ڦA���@���A���Z��o�S�Pı' )
         
    elif '����' in msg :
        message = TextSendMessage(text='���Z�b���w�����ɭԡA�����w���ݬ��k�A�ܩ���k�O�ִN���h���F')
         
    elif '�z��' in msg or '�����ݷ�' in msg :
        s_List=['�ؼ��k�ͪ��ɭԡA�n�ؼ���o�`�ۦa�����X�ܬ���',
                '���s�i�O�O�k�H��������! �O��������...������!',
                '�ߦ���W�ʩR���H�A�~��٤����^���C\n�O�@�P��A�@�Ϥk�H�A��W�ۤv�a!�J�����]�S���Y�A���쥴���]�L�X�A�ɱ����_�a!\n���Ѭ����\�����C�e���ۤv���@��A�ۥX�ۤv���Q�k�C\n�p���@�ӡA���~�O�o�O�@�W�̳��ѥߦa���^���C']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�ť�' in msg :
        message = TextSendMessage(text='')
         
    elif '���' in msg :
        message = TextSendMessage(text='��ƻ�?�A���Ѥ��u��')
        
    elif '�B��' in msg :
        s_List=["�j�N",
                "�N",
                "���N",
                "�p�N",
                "���N",
                "��",
                "�A�T�w?�ܥ���"]
        message = TextSendMessage(text=random.choice(s_List))

    elif '�ߦw' in msg :
        
        s_List=['�ߦw�r',
                '�ߦw�@(???)?',
                '�ߦw��(*?�s?*)',
                '�ߦw�r?^???^?',
                '�ߦw�r(?????)?*�C',
                '�ߦw��',
                '�ߦw�o',
                '�ߦw�r(?��?? ? ??��`)',
                '�ߦw',
                '�ߦwV��?��V',
                '�ߦw�r( ?��? ) ',
                '�ߦw��(*?�s?*)']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '??' in msg :
        message = TextSendMessage(text='??�O�b69 --���îf')
         
    elif '�q�j�Q��' in msg :
        message = TextSendMessage(text='�����ܡA�ڥλ�ժ�t�Y�q�j�Q�� --���îf')

    elif '�N����' in msg :
        s_List=['�ڭ̨��餺�@�b�� ��?��?    ��p�O�O�q�ͻs�y��',
                '�_��������O�z�����A��O�¦⪺',
                '��ޮ�������ƬO�T�E���i������A���L���n�I������N�S�ƤF�C',
                '�ƾڬO�۵M�ƾڡA�S���H���ק諸�A���õL�����ƾڡAĴ�p��a�H�f�BYT�v���[�ݦ��ơA�ƾڪ��}�Y�Ʀr�X�{���v�̰����Ʀr�O1��',
                'Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu�o�Ӧa��b�æ�����',
                '�H���o�Ӧa�W���x��ϥιL��ù���������T�ءADanshui�BTamsui�BTamshui�A�S���ϥιLDansui',
                'floccinaucinihilipilification�O�������N��',
                '�@�ɾ��v�W�������L�̤Ѭ�1752�~5/30~6/8',
                '�H���M���ͪ��H�����ʭP���v�O0',
                '�{�b�Xù��������ʤ�����̧֪��ޥ��Orolling',
                '�ڦ��@�i�ǻ����ޱ��|���q���ʯ୿�W����d... GT 210',
                '�A���D��?GT710���ʯ��GT720�j',
                '�A���D�չq���]��������?',
                '����b���@���A�Q�Q�ڵ����i�H��ܨ����a�쪺���G�A�Ʀܦ��X������A��',
                '���Ū��Ԥh�U�l�A�O�Ϊe�����ְ����A�ƦܦL�a�w�H���F�e���귽���[�A�ɭP�U�����H�f�j�q�U��',
                'Ĭ�p�H���g�βB�u�����B�\����A��f�f���u�����ۤW�U',
                '�ܥi�֡A��xŦ���ˮ`�P�ܰs����',
                '�}�����}�ʡA��s��Ҥ�зǦ��}���٭n�j',
                '�s���H�e�O�b���w�O�����a�H�~�|�Y������',
                '�p�۪�����A�N�O��P�j�j�O�q���i�{',
                '����50�~�N�A��1/3����ͨC�Ѧܤ֩�@�]��',
                '�b��þ�|�檺���B�A�O�n�r����ɪ�',
                '? ???�O�ҥH���ڧ��ƪ��N��A? (�ҥH)??(����)?(����)',
                '�ڲ{�b���O�m���b���P�@�ˡA�Ӷ��q����ɰ_�A�ӥB�פ�p�~'
                '�y�Y�H���ƨS�ƴN�|�h�ί��_�祴���H']
        message = TextSendMessage(text=random.choice(s_List))

    elif '�Υy' in msg or '�W��' in msg :
        s_List=['�����ܡA�ڥλ�ժ�t�Y�q�j�Q�� --���îf',
                '�z�A�A���l��---���e��',
                '����L���A������N������---���îf',
                '���îf:\n�u�n����l���O�Z�ȡC\n2021/4/1',
                '���îf�G\n�C�ڭ̱�....\n2021/4/15']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif 'flag' in msg :
        s_List=['�����ܡA�ڥλ�ժ�t�Y�q�j�Q�� --���îf',
                'Flag:\n31018���رƤ@�p�G�_��58�B59�B60���ܡA�N�n�Х��Z�ܬ�����']
        message = TextSendMessage(text=random.choice(s_List))
         

    elif '�n�o'in msg or '�n��'in msg or '�u��'in msg  or '�Q'in msg or 'peko'in msg :
        s_List=['�n���npeko��',
                '�ڭn�tcola',
                '�n�o��peko']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '���' in msg :
        message = TextSendMessage(text='�T�T�n�i�R')
         
    elif '�չ�J' in msg :
        message = TextSendMessage(text='�n��')
         
    elif '��k' in msg or '�i' in msg or '��F' in msg :
        s_List=['��k��k��k','�A�ٯu�O��k�O']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�y�P�B' in msg or '�B�ɷ�' in msg:
        s_List=['���Z���w��','���Z���w��','���Z���w�B�ɷ�']
        message = TextSendMessage(text=random.choice(s_List))
         
    elif '�����H�ۧڤ���' in msg :
        message = TextSendMessage(text='�ڬO��k�q�СA���S�|�N�Q���Pù�ҥ��d�ҡA�۱q���ӥH��A�N�b���Z�����U�u�@�F')     

    elif '�C������' in msg :
        message = TextSendMessage(text='�C������')

    elif 'FBI' in msg or '�ڲ�' in msg:
       # line_bot_api.reply_message(event.reply_token, message='�Ϥ��䴩')
        web_Rul = "https://i.imgur.com/Ej6FIVL.jpg"
        message = ImageSendMessage(original_content_url= web_Rul,
                                   preview_image_url = web_Rul )
    elif '�D�w' in msg :
        web_Rul = "https://www.youtube.com/watch?v=D0dBptGRTvc"
        message = TextSendMessage(text=web_Rul)
            
    line_bot_api.reply_message(event.reply_token, message)
    


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
