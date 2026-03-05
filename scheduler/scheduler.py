import schedule
import time

from scraper.scraper import scrape_bbc
from database.db import save_article, get_today_articles
from ai.summarizer import summarize_news
from mail.mailer import send_email


def collect_news():
    news = scrape_bbc()

    for article in news:
        save_article(article["title"], article["url"], article["source"])

    print("News collected")


def daily_summary():
    articles = get_today_articles()

    cleaned = [a.split("\n")[0] for a in articles]

    text = "\n".join(cleaned)

    summary = summarize_news(text)

    send_email(summary)

    print("Daily email sent")


# every 30 minutes → scrape
schedule.every(30).minutes.do(collect_news)

# every day at 9 PM → email summary
schedule.every().day.at("07:00").do(daily_summary)

while True:
    schedule.run_pending()
    time.sleep(1)