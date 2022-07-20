import requests
from urllib.parse import urlencode
import time
import random
import sys


def mail_to(receiver,subject,content):
    url = 'http://webserver.cuffs.cf/sendmail'
    data = {
        "mailto": receiver,
        "subject": subject,
        "content": content,
    }
    requests.post(url=url,data=data)

def daka(stu_id,name,receiver):
    headers = {
        'Host': 'www.informationofdum.com',
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wx8a86613d14cbe10c/10/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data = {
        "jsonnumber": 1120201413,
        "jsonname": 武照林,
        "jsonclass": "2020级硕士研究生中队",
        "morning": "36.2℃",
        "afternoon": "36.2℃",
        "night": "36.2℃",
        "jsonbody": 1,
        "jsonbodychangeinfo": "",
        "textarea": "在家",
        "textprople": "母亲",
        "jsontouch": 1,
        "jsontouchchangeinfo": 0,
        "jsonisolate": 1,
        "jsonisolatechangeinfo": 0,
        "latitude": 41.24548,
        "longitude": 119.40134, 
#         "latitude": 38.869938,
#         "longitude": 121.527683, 1
    }
    url = 'https://www.informationofdum.com/DMU_WEB/student_5/info/?'
    url += urlencode(data)
    response = requests.get(url,headers=headers)
    print(response)
    print(response.text)
    time.sleep(random.randint(0,180))  # 避免大家同时请求邮件服务器
    if len(receiver) != 0:
        mail_to(receiver, f"{name}=>{stu_id}=>信仰不息=>打卡成功！", str(response) + '\n' + response.text)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        daka(sys.argv[1], sys.argv[2], '')
    elif len(sys.argv) == 4:
        daka(sys.argv[1], sys.argv[2], sys.argv[3])
