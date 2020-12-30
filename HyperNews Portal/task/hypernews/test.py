import json
from datetime import datetime
import random

with open("../news.json", "r") as f:
    news = json.load(f)
link_list = [x["link"] for x in news]
link = random.choice([x for x in range(100000) if x not in link_list])
created = (str(datetime.now()).split(".")[0])
text = 'text'
title = 'title'
news.append({'created': created, 'text': text, 'title': title, 'link': link})
print(news)
print(news[0]['title'])