import asyncio
from pyppeteer import launch

async def main():
    post = 0
    while post < 353:
        browser = await launch()
        page = await browser.newPage()
        await page.goto('http://127.0.0.1:5000/post/' + str(post))
        await page.screenshot({'path': 'done/' + str(post) + '.png', 'clip': {'x': 0, 'y': 0, 'width': 500, 'height': 530}})
        await browser.close()
        print(post)
        post += 1

asyncio.get_event_loop().run_until_complete(main())