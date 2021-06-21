
파이썬으로 주식정보사이트 만들기.
2021541012 윤재락
2021541001 강태원
2021541008 김태진

----필수 설치 요소----
anaconda 32bit 설치 > https://baessi.tistory.com/125
maria DB 설치 > https://mariadb.org/download/ 10.5.9 version
heildsql 설치

--- 주의사항 ---
 
---
pip install Django # 장고설치
pip install jsonfield # json 설치
pip install bs4 # beautifulSoup 설치
pip install pandas # DataFrame 기본인 pandas 설치
pip install pymysql # sql DB를 활용하기 위한 모듈
pip install pykrx # 각종 주식 정보가 있는 pystock api 설치
----
설치후 오류 예상
1. detail 부분 쿼리 오류 -> view의 날자 3,10,17,24 > 를 수치 조정하여 최근 업데이트 6/18 로 조정 ex) 오늘이 21일이면 3,10,17,24  22일이면 4,11,18,25
2. news 부분 에러 -> 실행하는 컴퓨터에 config_secret 파일이 있어야 함. -> 네이버 API 를 다운받고 폴더안에 파일생성후 집어넣고 실행.
안될 시 문의
jrakmom971106@gmail.com
micro.kante@gmail.com