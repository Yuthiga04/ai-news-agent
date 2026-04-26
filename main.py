# from scraper.scraper import scrape_bbc
# from database.db import save_article, get_today_articles
# from ai.summarizer import summarize_news
# from mail.mailer import send_email

# # Step 1: collect news
# news = scrape_bbc()

# for article in news:
#     save_article(article["title"], article["url"], article["source"])

# # Step 2: fetch headlines
# articles = get_today_articles()

# # Step 3: clean headlines
# cleaned = []
# for a in articles:
#     title = a.split("\n")[0]
#     cleaned.append(title)

# text = "\n".join(cleaned)

# print("Collected Headlines:")
# print(text)

# # Step 4: summarize with AI
# summary = summarize_news(text)

# print("\nDaily Summary:\n")
# print(summary)

# # Step 5: send email
# send_email(summary)

# print("\nEmail sent successfully.")

from scraper.scraper import scrape_bbc
from scraper.reuters_scraper import scrape_reuters
from scraper.cnn_scraper import scrape_cnn

from database.db import save_article, get_today_articles
from ai.summarizer import summarize_news
from mail.mailer import send_email

# collect from multiple sources
news = []

news.extend(scrape_bbc())
news.extend(scrape_reuters())
news.extend(scrape_cnn())

# store with duplicate filtering
for article in news:
    save_article(article["title"], article["url"], article["source"])

# fetch
articles = get_today_articles()

# clean
cleaned = [a.split("\n")[0] for a in articles]

text = "\n".join(cleaned)

# summarize
summary = summarize_news(text)

# send email
send_email(summary)