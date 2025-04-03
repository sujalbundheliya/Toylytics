import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import os

async def scrape_amazon():
    os.makedirs("data", exist_ok=True)
    sponsored_data = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.amazon.in", timeout=60000)
        await page.wait_for_timeout(3000)

        search_box = await page.wait_for_selector("input#twotabsearchtextbox")
        await search_box.click()
        await search_box.type("soft toys", delay=150)
        await page.keyboard.press("Enter")

        await page.wait_for_selector('div[data-component-type="s-search-result"]', timeout=15000)

        # Get all Sponsored labels
        sponsored_tags = page.locator("text=Sponsored")
        count = await sponsored_tags.count()
        print(f"✅ Found {count} sponsored labels on the page.")

        for i in range(count):
            try:
                tag = sponsored_tags.nth(i)
                # Go to its parent block (3 levels up to reach full card)
                product_block = tag.locator("xpath=ancestor::div[@data-component-type='s-search-result']")
                if await product_block.count() == 0:
                    continue

                # Extract info inside the block
                title = await product_block.locator('h2 span').inner_text() if await product_block.locator('h2 span').count() > 0 else ""
                brand = await product_block.locator('h5 span').inner_text() if await product_block.locator('h5 span').count() > 0 else "Unknown"

                rating = await product_block.locator('[aria-label*="out of 5 stars"]').get_attribute("aria-label") if await product_block.locator('[aria-label*="out of 5 stars"]').count() > 0 else None
                reviews = await product_block.locator('span[aria-label$="ratings"]').inner_text() if await product_block.locator('span[aria-label$="ratings"]').count() > 0 else "0"

                price_list = product_block.locator('.a-price span.a-offscreen')
                price_count = await price_list.count()
                price = await price_list.nth(0).inner_text() if price_count > 0 else None

                image = await product_block.locator("img").get_attribute("src") if await product_block.locator("img").count() > 0 else ""
                product_url = await product_block.locator('h2 a').get_attribute("href") if await product_block.locator('h2 a').count() > 0 else ""

                sponsored_data.append({
                    "Title": title.strip(),
                    "Brand": brand.strip(),
                    "Reviews": reviews.replace(",", "").strip(),
                    "Rating": rating.split(" ")[0] if rating else None,
                    "Selling Price": price.strip() if price else None,
                    "Image URL": image,
                    "Product URL": f"https://www.amazon.in{product_url}" if product_url else ""
                })

                print(f"✅ Scraped sponsored product #{i + 1}")

            except Exception as e:
                print(f"❌ Error processing sponsored item #{i}: {e}")
                continue

        df = pd.DataFrame(sponsored_data)
        print(f"\n✅ Scraped {len(df)} sponsored items.")
        df.to_csv("data/raw_data.csv", index=False)

asyncio.run(scrape_amazon())
