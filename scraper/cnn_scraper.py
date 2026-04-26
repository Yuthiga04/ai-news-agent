def scrape_cnn():
    articles = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://edition.cnn.com/world")

        page.wait_for_selector("a")

        items = page.query_selector_all("a")

        for item in items:
            title = item.inner_text().strip()
            link = item.get_attribute("href")

            if title and len(title) > 30:
                if link and not link.startswith("http"):
                    link = "https://edition.cnn.com" + link

                articles.append({
                    "title": title,
                    "url": link,
                    "source": "CNN"
                })

            if len(articles) >= 10:
                break

        browser.close()

    return articles