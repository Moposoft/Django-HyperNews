import json
from datetime import datetime

with open("../news.json", "r") as f:
    news = json.load(f)

print(news)
days = set([x["created"].split()[0] for x in news])
print(days)
d = [{"date": x, "news": [{'text': y['text'], 'link': y['link']} for y in news if y["created"].split()[0] == x]} for x in days]
print(d)