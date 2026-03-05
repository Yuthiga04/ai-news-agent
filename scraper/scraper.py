from playwright.sync_api import sync_playwright


def scrape_bbc():
    articles = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.bbc.com/news", timeout=60000)

        # Wait for article cards to load
        page.wait_for_selector("a[data-testid='internal-link']")

        items = page.query_selector_all("a[data-testid='internal-link']")

        for item in items:
            title = item.inner_text().strip()
            link = item.get_attribute("href")

            # Skip navigation items
            if not title or len(title) < 30:
                continue

            if link and not link.startswith("http"):
                link = "https://www.bbc.com" + link

            articles.append({
                "title": title,
                "url": link,
                "source": "BBC"
            })

            # limit to 10 real articles
            if len(articles) >= 10:
                break

        browser.close()

    return articles