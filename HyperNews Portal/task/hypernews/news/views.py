from django.conf import settings
from django.views import View
from django.shortcuts import render
import json
from datetime import datetime


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/index.html')


class NewsView(View):
    def get(self, request, link, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as f:
            news = json.load(f)
        content = {}
        for x in news:
            if x["link"] == link:
                content = x
                print(x)
                break
        context = {
            "title": content["title"],
            "text": content["text"],
            "created": content["created"],
        }
        return render(request, 'news/news.html', context)


class NewsIndexView(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as f:
            news = json.load(f)
        sorted(news, key=lambda x: datetime.strptime(x['created'], '%Y-%m-%d %H:%M:%S'), reverse=False)
        news_list = [{"date": x, "news": [{'title': y['title'], 'link': y['link']} for y in news if y["created"].split()[0] == x]}
                     for x in set([x["created"].split()[0] for x in news])]
        context = {
            "list": news_list
        }
        return render(request, 'news/news_index.html', context)