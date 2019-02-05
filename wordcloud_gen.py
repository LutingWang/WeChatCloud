from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud
# from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import os

Unwanted = ["custom", "link", "SystemMessages", "weixinhongbao", "wc", "username",
            "CDATA", "profile", "nickname", "wxid", "memberlist", "member", "type",
            "content", "templete", "group", "char", "plain"]
Unwanted += ["这个", "微信", "表情", "一下", "不是", "没有", "一个"]
users = [path for path in os.listdir('.') if os.path.isdir(path)]


def extract(folder):
    if not os.path.exists("./"+folder+"/msg.htm"):
        return ''
    html = open("./"+folder+"/msg.htm", encoding="utf8").read()
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find_all("span", class_="MsgHistory")
    his = '\n'.join([line.string if line.string is not None else '' for line in content])
    return ' '.join([word for word in jieba.cut(his) if word not in Unwanted])


for username in users:
    cut = ''
    for folder in os.listdir("./"+username+"/"):
        cut += extract("./"+username+"/"+folder)
    if not cut:
        continue
    img = Image.open("mask.png")
    img_array = np.array(img)
    cloud = WordCloud(background_color='white', width=1000, height=800, scale=2, mask=img_array, font_path="font.ttf")
    cloud.generate_from_text(cut)
    cloud.to_file(username+".png")
