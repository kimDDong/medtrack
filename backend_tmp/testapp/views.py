from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
# Bookmark 테이블의 데이터를 가져오기 위해 models.py에서 Bookmark 클래스를 import
from .models import Bookmark, user_personal_info, medication_info, daily_intake_info, login_info

# 새로 import 하는 모듈
from django.db import connection

from .testform import BookForm, gaip, login

from django.views.decorators.csrf import csrf_exempt

import pymysql


#Test Function
# 모듈 import
import requests
import pprint
from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
#Test Function

# Create your views here.
def BookmarkListView(request):
    # books = Book.objects.all()
    try:
        cursor = connection.cursor()

        strSql = "SELECT id, name, url FROM testapp_bookmark"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        books = []
        for data in datas:
            row = {'id': data[0],
                   'name': data[1],
                   'url': data[2]}

            books.append(row)

    except:
        connection.rollback()
        print("Failed selecting in BookListView")


    return render(request, 'bookmark_list.html', {'bookmarks': books})

def BookmarkDetailView(request, id):
    # book1 = get_object_or_404(Book, code=code)
    # book2 = Book.objects.get(code=code)

    try:
        cursor = connection.cursor()

        strSql = "SELECT id, name, url FROM testapp_bookmark WHERE id = (%s)"
        result = cursor.execute(strSql, (id,))
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        book = {'id': datas[0][0],
                'name': datas[0][1],
                'url': datas[0][2]}
    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    return render(request, 'bookmark_detail.html', {'bookmark': book})

#Test
def TestView(request):
    # book1 = get_object_or_404(Book, code=code)
    # book2 = Book.objects.get(code=code)

    if request.method == 'POST':
        form = BookForm(request.POST)

        # 유효성 검사
        if form.is_valid():
            std = Bookmark()
            std.name = form.cleaned_data['name']
            std.url = form.cleaned_data['url']
            std.name, std.url = test(std.name, std.url)
            std.save()
            return render(request, 'bookmark_list.html')

        # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = BookForm()

    return render(request, 'form_create.html', {'form': form})

#Test
@csrf_exempt
def TestView2(request):
    # book1 = get_object_or_404(Book, code=code)
    # book2 = Book.objects.get(code=code)

    if request.method == 'POST':
        form = gaip(request.POST)
        if form.is_valid() :
            form = user_personal_info()
            form.user_id = request.POST.get('user_id')
            form.password = request.POST.get('password')
            form.name = request.POST.get('name')
            form.social_number = request.POST.get('social_number')
            form.phone_number = request.POST.get('phone_number')
            form.address = request.POST.get('address')
            form.preferred_hospital = request.POST.get('preferred_hospital')

            form.save()
            return render(request, 'index.html')
    form = user_personal_info()
    return render(request, 'signup.html', {'signup': form})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        try :
            # print(user_personal_info.objects.get(user_id=user_id))
            data = user_personal_info.objects.get(user_id=user_id)
        except user_personal_info.DoesNotExist:
            form = login_info()
            return render(request, 'index.html', {'login': form})
        if data.password == password :
            return HttpResponse(f'로그인 성공! {user_id} 님 환영합니다!')
        else :
            return HttpResponse(f'로그인 실패')
    form = login_info()
    return render(request, 'index.html', {'login': form})


def test(EN, IN) :
    # 인증키 입력
    encoding = "tMFsc357luCM9XvhWaRtDu%\2FsdcZltWIJtB1gKDA4%2Bf5ApOQ%2BnX2cTzAYF6ILAQEa5KsE%\2FxrLirrfhQ24lXtLFQ%3D%3D"
    decoding = 'tMFsc357luCM9XvhWaRtDu/sdcZltWIJtB1gKDA4+f5ApOQ+nX2cTzAYF6ILAQEa5KsE/xrLirrfhQ24lXtLFQ=='

    # url 입력
    url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'
    params = {'serviceKey': decoding,
              # 'pageNo' : '100',
              'numOfRows': '100',
              'entpName' : EN,
              'itemName' : IN,
              # 'startCreateDt' : '2020',
              # 'endCreateDt' : '20211103'
              }

    response = requests.get(url, params=params)

    # xml 내용
    content = response.text

    # 깔끔한 출력 위한 코드
    pp = pprint.PrettyPrinter(indent=4)
    # print(pp.pprint(content))
    # print(content)

    # bs4 사용하여 item 태그 분리

    xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
    rows = xml_obj.findAll('item')
    print(len(rows))
    # print()
    print(rows)
    # """
    # 컬럼 값 조회용
    # columns = rows[0].find_all()
    # print(columns)
    # """

    # 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
    row_list = []  # 행값
    name_list = []  # 열이름값
    value_list = []  # 데이터값

    # xml 안의 데이터 수집
    for i in range(0, len(rows)):
        columns = rows[i].find_all()
        # 첫째 행 데이터 수집
        for j in range(0, len(columns)):
            if i == 0:
                # 컬럼 이름 값 저장
                name_list.append(columns[j].name)
            # 컬럼의 각 데이터 값 저장
            value_list.append(columns[j].text)
        # 각 행의 value값 전체 저장
        row_list.append(value_list)
        # 데이터 리스트 값 초기화
        value_list = []

    # xml값 DataFrame으로 만들기
    result = pd.DataFrame(row_list, columns=name_list)
    # print()
    # print()
    # print()
    # print()
    # print()
    # print(name_list)
    # print(result.iloc[0])
    # print(result.iloc[0]['entpName'])
    return result.iloc[0]['entpName'], result.iloc[0]['itemName']
    # entpName = 업체명
    # itemName = 제품명
    # itemSeq = 품목기준코드
    # efcyQesitm = 문항1(효능)
    # usemethodQesitm = 문항2(사용법)
    # atpnWarnQesitm = 문항3(주의사항 경고)
    # atpnQesitm = 문항4(주의사항)
    # intrcQesitm = 문항5(상호작용)
    # seQesitm = 문항6(상호작용)
    # depositMethodQesitm = 만항7(보관법)
    # openDe = 공개일자
    # updateDe = 수정일자

    # DataFrame CSV 파일로 저장
    # result.to_csv('result.csv', encoding='utf-8-sig')