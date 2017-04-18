# -*- coding: utf-8 -*-
import json
import random
import time
from bs4 import BeautifulSoup
from book.db.BookDetailDao import BookDetailDao
from book.util.FileDownLoadThread import FileDownLoadThread


class BookDetailParse(object):
    """
    书籍列表解析
    """

    def __init__(self):
        pass
        self.bookDetailDao = BookDetailDao()
        self.index = 0

    def start(self, html, source_url, book_id):
        if self.bookDetailDao.checkExist(book_id):
            return
        soup = BeautifulSoup(html, "lxml")
        book_name = soup.select("title")
        if book_name and len(book_name) > 0:
            book_name = book_name[0].get_text().replace(u"(豆瓣)", "")
        print "书名：", book_name
        main_info = soup.select("div.grid-16-8 #info")  # 主要的信息
        if main_info and len(main_info) > 0:
            main_info = main_info[0]
            # 作者:出版社:出版年:页数:定价:装帧:ISBN:
            main_info = main_info.get_text().replace(u"\n", "").replace(u" ", "").replace(u" ", "")
        else:
            main_info = ""
        print "主要信息：", main_info

        img_douban = soup.select("div.grid-16-8 #mainpic a.nbg img")  # 图片
        if img_douban and len(img_douban) > 0:
            img_douban = img_douban[0].get("src")
        else:
            img_douban = ""
        print "主图：", img_douban
        img_name = str(time.time()).replace('.', '')
        img_self = "/book_img/"+str(book_id) + "_" + img_name + '.jpg'
        # 开线程下载
        FileDownLoadThread(book_id, img_self, img_douban).start()
        # 根据图片进行下载
        score = soup.select("div.grid-16-8 div.rating_wrap ")  # 评分
        if score and len(score) > 0:
            score = score[0]
            # 评分
            rating_num = score.select("strong.rating_num")
            if rating_num and len(rating_num) > 0:
                rating_num = rating_num[0].get_text()
            else:
                rating_num = ""
            # 评价人数
            rating_people = score.select("a.rating_people")
            if rating_people and len(rating_people) > 0:
                rating_people = rating_people[0].get_text().replace(u"\n", "").replace(u" ", "").replace(u" ", "")
            else:
                rating_people = ""
            # 百分比  [5,4,3,2,1]星占的比例
            rating_pers = score.select("span.rating_per") or []
            rating_per_all = []
            for rating_per in rating_pers:
                rating_per_all.append(rating_per.get_text())

            scoreItem = {
                "rating_num":rating_num,
                 "rating_people":rating_people,
                 "rating_per_all": rating_per_all
            }
            score = json.dumps(scoreItem, encoding="utf8", ensure_ascii=False)
        else:
            score = ""
        print "评分：", score
        # 目录
        mulus = soup.select("div.grid-16-8 #dir_" + str(book_id) + "_full")  # 1154707当前的图书的id  目录
        if mulus and len(mulus) > 0:
            mulus = mulus[0]
            mulus = mulus.get_text(",").replace(u"· · · · · ·     (,收起,)", "").replace(u"\n", "").replace(u" ", "").replace(
                u" ", "").strip(",").split(",")
            mulus = json.dumps(mulus, encoding="utf8", ensure_ascii=False)
        else:
            mulus = ""
        print "目录：",mulus
        # 标签
        tags = soup.select("div.grid-16-8 a.tag ")
        if tags:
            tagList = []
            for tag in tags:
                tagList.append(tag.get_text())
            tags = json.dumps(tagList, encoding="utf8", ensure_ascii=False)
        else:
            tags = ""
        print "标签：",tags
        # 内容简介 (1)内容不多 #link-report > div.intro （2）内容多  #link-report > span.all > div.intro
        neirongjianjie = soup.select("div.grid-16-8 #link-report")
        neirongDetail = ""
        if neirongjianjie:
            # 先判断是否存在#link-report > span.all > div.intro 如果不存在则调用 #link-report > div.intro
            neirongjianjie = neirongjianjie[0]
            neirongDetail = neirongjianjie.select("span.all  div.intro p")
            endDetails = []
            if neirongDetail:
                for detail in neirongDetail:
                    endDetails.append(detail.get_text())
            else:
                neirongDetail = neirongjianjie.select("div.intro p")
                for detail in neirongDetail:
                    endDetails.append(detail.get_text())
            neirongDetail = "\n".join(endDetails)
        neirongjianjie = neirongDetail or ""
        print "内容简介：", neirongjianjie

        # 作者简介 (1)内容不多 #link-report > div.intro （2）内容多  #link-report > span.all > div.intro
        zuozhejianjie = soup.find("span", text=["作者简介"])
        zuozheDetail = ""
        if zuozhejianjie:
            zuozhejianjie = zuozhejianjie.parent
            if zuozhejianjie:
                zuozhejianjie = zuozhejianjie.findNextSibling()
                if zuozhejianjie:
                    zuozheDetail = zuozhejianjie.select("span.all  div.intro p")
                    endDetails = []
                    if zuozheDetail:
                        for detail in zuozheDetail:
                            endDetails.append(detail.get_text())
                    else:
                        zuozheDetail = zuozhejianjie.select("div.intro p")
                        for detail in zuozheDetail:
                            endDetails.append(detail.get_text())
                    zuozheDetail = "\n".join(endDetails)
        zuozhejianjie = zuozheDetail or ""
        print "作者简介：", zuozhejianjie

        # 丛书信息
        congshuxinxi = soup.find_all("h2", text=["丛书信息"])
        congshuDetail = ""
        if congshuxinxi:
            congshuxinxi = congshuxinxi[0].findNextSibling()
            if congshuxinxi:
                congshuDetail = congshuxinxi.get_text().replace(u"\n","").replace(u" ","").strip(u"　").strip(u" ").replace(u" ","")
        congshuxinxi = congshuDetail or ""
        print "丛书信息：", congshuxinxi
        item = {}
        item['book_name'] = book_name or ''
        item['main_info'] = main_info or ''
        item['img_douban'] = img_douban or ''
        item['img_self'] = img_self or ''
        item['score'] = score or ''
        item['mulus'] = mulus or ''
        item['tags'] = tags or ''
        item['neirongjianjie'] = neirongjianjie or ''
        item['zuozhejianjie'] = zuozhejianjie or ''
        item['congshuxinxi'] = congshuxinxi or ''
        item['source_url'] = source_url or ''
        item['book_id'] = book_id or ''

        print "抓取保存的book数据:", book_id, main_info
        self.bookDetailDao.save(item)