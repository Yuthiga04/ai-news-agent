from playwright.sync_api import sync_playwright

def scrape_ndtv():
    articles = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://www.ndtv.com/latest", timeout=60000)
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(3000)

            items = page.query_selector_all("a")

            for item in items:
                title = item.inner_text().strip()
                link = item.get_attribute("href")

                if title and len(title) > 30:
                    articles.append({
                        "title": title,
                        "url": link,
                        "source": "NDTV"
                    })

                if len(articles) >= 10:
                    break

            browser.close()

    except Exception as e:
        print("NDTV scraping failed:", e)

    return articles