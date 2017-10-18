# -*- coding: utf-8 -*-
import requests

headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"PHPSESSID=q4geis5kk922sdiggd3t935l91; DedeUserID=23640; DedeUserID__ckMd5=0df16f58192ab050; DedeLoginTime=1493262803; DedeLoginTime__ckMd5=9e8589a65d11d12d; Hm_lvt_d9f69e9a282649ed6219a7bc41596401=1493262660; Hm_lpvt_d9f69e9a282649ed6219a7bc41596401=1493262798",
"Host":"www.abcppt.com",
"Referer":"http://www.abcppt.com/sw/",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}
cookies = {"PHPSESSID":"q4geis5kk922sdiggd3t935l91","DedeUserID":"23640","DedeUserID__ckMd5":"0df16f58192ab050","DedeLoginTime":"1493262803","DedeLoginTime__ckMd5":"9e8589a65d11d12d","Hm_lvt_d9f69e9a282649ed6219a7bc41596401":"1493262660","Hm_lpvt_d9f69e9a282649ed6219a7bc41596401":"1493262798"}


response = requests.get("http://www.abcppt.com/sw/qt/18117.html",headers=headers,timeout=5,cookies=cookies)

print response.encoding  # 打印出来的是什么，此处是ISO-8859-1
response.encoding = "utf-8" #这里添加一行
print response.encoding  # 打印出来的是什么，此处是ISO-8859-1
print response.text # 将内容编码成对应的encoding
