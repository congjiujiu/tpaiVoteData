__author__ = 'cong'

import urllib2
import urllib
import re

t = []

class team():
    id = ''
    name = ''
    vote = 0

    def __init__(self,i,n,v):
        self.id = i
        self.name = n
        self.vote = v

def get1():
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=1'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    i = 0
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        i += 1

    i = 0
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[i].vote = int(word)
        i += 1

    i = 0
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[i].name = words_2[0]
        i += 1
    return i

def get2(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=1&page=2'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get3(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=2&keyword='
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get5(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=2&keyword=&page=3'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get4(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=2&keyword=&page=2'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get5(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=2&keyword=&page=3'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get6(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=2&keyword=&page=4'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get7(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=2&keyword=&page=5'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get8(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=3&keyword='
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1
    return k

def get9(l):
    url1 = 'http://tpai.qq.com/race/mobilecreative2015/works?category_id=3&keyword=&page=2'
    html2 = urllib2.urlopen(url1)
    html2 = html2.read()
    html2 = html2.decode('utf-8')

    words1 = re.findall('<span class=\"poll-item-id\">.*?</span>',html2,re.S)
    words2 = re.findall('<span class=\"count-number\">.*?</span>',html2,re.S)
    words3_1 = re.findall('<p class=\"subject\">.*?</p>',html2,re.S)

    k = l
    for word in words1:
        word = word.replace('<span class=\"poll-item-id\">','')
        word = word.replace('</span>','')
        word = word.replace('ID: ','')
        #print word
        te = team(word,' ',' ')
        t.append(te)
        k += 1

    k = l
    for word in words2:
        word = word.replace('<span class=\"count-number\">','')
        word = word.replace('</span>','')
        #print word
        word = word[0:-1]
        t[k].vote = int(word)
        k += 1

    k = l
    for word in words3_1:
        word = word[106:-1]
        words_2 = word.split("\"")
        #print words_2[0]
        t[k].name = words_2[0]
        k += 1

def start():
    l1 = get1()
    l2 = get2(l1)
    l3 = get3(l2)
    l4 = get4(l3)
    l5 = get5(l4)
    l6 = get6(l5)
    l7 = get7(l6)
    l8 = get8(l7)
    get9(l8)

    l = 1
    t.sort(lambda x,y:y.vote-x.vote)
    for x in t:
        print l,x.id,x.name,x.vote
        l+=1


if __name__ == '__main__':
    start()
