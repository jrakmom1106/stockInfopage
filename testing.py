from bs4 import BeautifulSoup
import urllib.request as req
import requests
import lxml
# url = 'https://finance.naver.com/sise/'         #네이버 금융 url 주소
# res = req.urlopen(url).read().decode('cp949')   #utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐, cp949로 변환해야한다.
 
# soup = BeautifulSoup(res, "html.parser")
 
# top10 = soup.select('#popularItemList > li > a')


# for i, e in enumerate(top10,1):
#     print("순위:{}, 이름: {}".format(i,e.string))

url = 'https://finance.naver.com/'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
res = req.urlopen(url).read().decode('cp949')
    #response = requests.get(res,headers=headers)
soup = BeautifulSoup(res,'html.parser')

top = soup.select("#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr > th")
print(top)

toplist = list()
top2 = list()

for tops in top:
    toplist.append(tops.text.strip())
print(toplist)

for i in range(len(toplist)):
    comp = top[i].text.strip()

    item_obj={
        'comp':comp,
    }
    top2.append(item_obj)
comps = top2

print(comps)


'''
<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <a class="navbar-brand" style="font-size:25px;" href="/home">주식정보사이트</a>
    <button class="navbar-toggler ml-auto" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse flex-grow-0" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item ">
                <a class="nav-link" href="#">로그인</a>
            </li>
        </ul>
    </div>
</nav>

<title>코스피 기업정보</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

'''#_topItems1 > tr:nth-child(1) > th