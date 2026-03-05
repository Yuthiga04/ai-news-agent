from scraper.scraper import scrape_bbc
from database.db import save_article, get_today_articles
from ai.summarizer import summarize_news

# collect news
news = scrape_bbc()

for article in news:
    save_article(article["title"], article["url"], article["source"])

# fetch headlines
articles = get_today_articles()

# clean headlines
cleaned = []
for a in articles:
    title = a.split("\n")[0]   # keep only first line
    cleaned.append(title)

text = "\n".join(cleaned)

print(text)   # debug

summary = summarize_news(text)

print("\nDaily Summary:\n")
print(summary)