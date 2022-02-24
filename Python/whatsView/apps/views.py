import json, os, sys, urllib.request, requests, re

from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import FormView
from requests import request
from bs4 import BeautifulSoup



def index(request):
    return render(request, 'common/main.html')



def make_naver_search_api_url(search_text, start_num, disp_num):
    base_url = 'https://openapi.naver.com/v1/search/blog.json'
    param_query = "?query=" + urllib.parse.quote(search_text)
    param_start = "&start=" + str(start_num)
    param_disp = "&display=" + str(disp_num)

    return base_url + param_query + param_start + param_disp

def get_request_url(request):
    searchValue = request.GET.get('searchValue',"")
    API_URL = make_naver_search_api_url(searchValue, 1, 10)
    config_secret_debug = json.loads(open(settings.SECRET_DEBUG_FILE).read())
    client_id = config_secret_debug['NAVER']['CLIENT_ID']
    client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']

    request = urllib.request.Request(API_URL)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        items = result.get('items')

        context = {
            'items': items
        }
        return render(request, 'searchView/info.html', {'info_items': context[0]})
    else:
        print("---error---")
        return None

def youtube(request):
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': 'AIzaSyAWvSovFGym1Wj9116pOIGF4Fcx4wigK3Y',
        'part': 'snippet',
        'type': 'video',
        'maxResults': '10',
        'regionCode': "KR",
        'q': request.GET.get('searchValue',""),
    }
    response = requests.get(url, params)
    response_dict = response.json()

    context = {
        'youtube_items': response_dict['items']
    }
    return render(request, 'searchView/video.html', {'video_items': context['youtube_items']})

def all(request):
    if request.method == 'GET':
        # naver search value
        # search_text = request.POST.get('searchValue', "")
        search_text = request.GET.get('searchValue')
        API_URL = make_naver_search_api_url(search_text, 1, 40)

        config_secret_debug = json.loads(open(settings.SECRET_DEBUG_FILE).read())
        client_id = config_secret_debug['NAVER']['CLIENT_ID']
        client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']

        naver_request = urllib.request.Request(API_URL)
        naver_request.add_header("X-Naver-Client-Id", client_id)
        naver_request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(naver_request)
        rescode = response.getcode()

        if (rescode == 200):

            #  youtube search value
            url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'key': 'AIzaSyAWvSovFGym1Wj9116pOIGF4Fcx4wigK3Y',
                'part': 'snippet',
                'type': 'video',
                'maxResults': '12',
                'regionCode': "KR",
                'q': search_text,
            }
            response1 = requests.get(url, params)
            response_dict = response1.json()

            response_body = response.read()
            naver_result = json.loads(response_body.decode('utf-8'))
            naver_items = naver_result.get('items')

            context = {
                'items': naver_items,
                'youtube_items': response_dict['items']
            }
            return render(request, 'searchView/all.html', {'info_items':context['items'], 'video_items':context['youtube_items']})
        else:
            print("---error---")
            return None