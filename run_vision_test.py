import asyncio
from playwright.async_api import async_playwright

async def run_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        print("Visiting live URL: https://k3.fedu.vn/case-bui-dung")
        await page.goto("https://k3.fedu.vn/case-bui-dung", wait_until="networkidle")
        await page.screenshot(path="vision_report.png", full_page=True)
        await browser.close()
        print("Screenshot saved to vision_report.png")

asyncio.run(run_test())
