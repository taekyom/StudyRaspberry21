from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
import urllib.request as urq
import urllib.parse as uparse
import json
import datetime

class naverSearch(object):
    #생성자
    def __init__(self):
        print('Naver Search API 생성')
    #네이버 api 요청함수
    def getRequestUrl(self, url):
        req = urq.Request(url)
        req.add_header('X-Naver-Client-Id', 'Qw3f08JPDllAQeFn_mmr')
        req.add_header('X-Naver-Client-Secret', 'hzBeF6akVl')

        #200 : ok, 404 : ERROR, 500 : 
        try:
            res = urq.urlopen(req)
            if res.getcode() == 200: #OK
                print('[{0}] URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')

        except Exception as e:
               print(e)
               return None
    #네이버 검색 api 사용함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(page_start, display, uparse.quote(search_word))
        url = base + node + param #https://openapi.naver.com...
        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)    

    #데이터 처리 함수
    def getPostData(self, post, jsonResult):
        title = post['title']
        desc = post['description']    
        org_link = post['originallink']
        link = post['link']
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')   
        p_date = pDate.strftime('%Y-%m-%d %H:%M:%S') 

        jsonResult.append({})
        pass
        return 

