#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob


##   图片页创建
def HTML():
    html = r'<!DOCTYPE html>'
    html += r'<html>'
    html += r'<head>'
    html += r'<meta charset="utf-8" />'
    html += r'<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    html += r'<title>'
    html += os.getcwd().split("\\")[-1]
    html += r'</title>'
    html += r'<style>'
    html += r'*{padding:0;margin:0;-webkit-box-sizing: border-box;-moz-box-sizing: border-box;box-sizing:border-box;}'
    html += r'body{background:#dbdbdb;}'
    html += r'img{border:none;}'
    html += r'.container{padding-left:10px;padding-right:10px;margin-left:auto;margin-right:auto;text-align:center;}' 
    html += r'.img-responsive{display:inline-block;margin-top:5px;height:auto;max-width:100%;padding:5px;background-color:#ffffff;vertical-align:top;border:1px solid #cccccc;}'
    html += r'</style>'
    html += r'</head>'
    html += r'<body>'
    html += r'<div class="container">'
    return html


def Comic(path):
    img_first = r'<img src="'
    img_end = r'" class="img-responsive" />'
    html_end = r'</div></body></html>'

    with open(path+"/index.html",'w',encoding="utf-8") as f:
        f.write(HTML())
        file = glob.glob("*.[jp][pn]g")
        for i in range(len(file)):
            f.write(img_first+file[i]+img_end)
        f.write(html_end)


## 得到目录 与文件名
path = os.getcwd()
list_path = []
list_img = []
for path,dirs,filename in os.walk(path):
    list_path.append(path)
    if(filename!=[]):
        list_img.append(os.path.join(path,filename[0]))


# 得到目录图片
list_imgs = []
for i in range(len(list_img)):
    if ".jpg" in list_img[i]:
        list_imgs.append(list_img[i])
    elif ".png" in list_img[i]:
        list_imgs.append(list_img[i])


##   导航页创建
def Main():
    html = r'<!DOCTYPE html>'
    html += r'<html>'
    html += r'<head>'
    html += r'<meta charset="utf-8" />'
    html += r'<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    html += r'<title>'
    html += r'导航页面'
    html += r'</title>'
    html += r'<style>'
    html += r'*{padding:0;margin:0;-webkit-box-sizing: border-box;-moz-box-sizing: border-box;box-sizing:border-box;}'
    html += r'body{background:#dbdbdb;text-align:center;}'
    html += r'img{border:none;}'
    html += r'.container{padding-left:10px;padding-right:10px;margin-left:auto;margin-right:auto;}'
    html += r'li{list-style: none;}'
    html += r'.list_img{width: 1024px;height: 200px;margin:50px auto;}'
    html += r'.list_img ul{width: 750px;}'
    html += r'.list_img li{float: left;width:200px;height:200px;margin-right: 50px;text-align: center;font-size: 0;margin-bottom: 50px;}'
    html += r'.list_img li a{display: block;width: 198px;height: 198px;border: 1px solid #ccc;}'
    html += r'.list_img li a:hover{border: 1px solid #f00;}'
    html += r'.list_img li span{display: inline-block;width: 1px;height: 100%;vertical-align:middle;}'
    html += r'.list_img li img{vertical-align: middle;max-width:178px;max-height:178px;}'
    html += r'.title{ font-size:12px;}'
    html += r'</style>'
    html += r'</head>'
    html += r'<body>'
    html += r'<div class="container">'

    html_end = r'</div></body></html>'
    with open("main.html","w",encoding="utf-8") as f:
        f.write(html+r'<ul><div class="list_img">')
        for i in range(len(list_imgs)):
            img = r'<img src="'+list_imgs[i]+r'" />'
            title = list_imgs[i].split("\\")[-2]
            a_href =list_imgs[i].replace(list_imgs[i].split("\\")[-1],"index.html")
            a_img = r'<li><div><a href="'+a_href+r'" >'+r'<span></span>'+img+r'</a></div>'
            a_info = r'<div class="title">'+title+r'</div></li>'
            f.write(a_img+a_info)
        f.write(r'</ul></div>'+html_end)




if __name__=='__main__':
    # 判断是否创建导航页
    if(len(list_path)>1):
        #print("----")
        Main()

    # 创建图片页面
    for i in range(len(list_path)):
        os.chdir(list_path[i])
        reg = glob.glob("*.[jp][pn]g")
        if(reg!=[]):
            Comic(list_path[i])
            #print("=========")


# version 3.2
# 目录完成demo
# 创建标题
# 导航页CSS的实现
