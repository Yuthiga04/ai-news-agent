from playwright.sync_api import sync_playwright

def scrape_aljazeera():
    articles = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://www.aljazeera.com/", timeout=60000)
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(3000)

            items = page.query_selector_all("a")

            for item in items:
                title = item.inner_text().strip()
                link = item.get_attribute("href")

                if title and len(title) > 30:
                    if link and not link.startswith("http"):
                        link = "https://www.aljazeera.com" + link

                    articles.append({
                        "title": title,
                        "url": link,
                        "source": "Al Jazeera"
                    })

                if len(articles) >= 10:
                    break

            browser.close()

    except Exception as e:
        print("Al Jazeera scraping failed:", e)

    return articles