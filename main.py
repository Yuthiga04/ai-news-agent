from scraper.scraper import scrape_bbc
from database.db import save_article, get_today_articles
from ai.summarizer import summarize_news
from mail.mailer import send_email

# Step 1: collect news
news = scrape_bbc()

for article in news:
    save_article(article["title"], article["url"], article["source"])

# Step 2: fetch headlines
articles = get_today_articles()

# Step 3: clean headlines
cleaned = []
for a in articles:
    title = a.split("\n")[0]
    cleaned.append(title)

text = "\n".join(cleaned)

print("Collected Headlines:")
print(text)

# Step 4: summarize with AI
summary = summarize_news(text)

print("\nDaily Summary:\n")
print(summary)

# Step 5: send email
send_email(summary)

print("\nEmail sent successfully.")