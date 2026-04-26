from playwright.sync_api import sync_playwright

def scrape_reuters():
    articles = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.goto("https://www.reuters.com/world/", timeout=60000)

        # wait properly for page load
        page.wait_for_load_state("domcontentloaded")
        
        # small delay (important for GitHub)
        page.wait_for_timeout(3000)

        items = page.query_selector_all("a[href]")

        for item in items:
            title = item.inner_text().strip()
            link = item.get_attribute("href")

            if title and len(title) > 30:
                if link and not link.startswith("http"):
                    link = "https://www.reuters.com" + link

                articles.append({
                    "title": title,
                    "url": link,
                    "source": "Reuters"
                })

            if len(articles) >= 10:
                break

        browser.close()

    return articles