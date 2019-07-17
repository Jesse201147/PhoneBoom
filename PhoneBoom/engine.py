# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019-07-10 9:44
import asyncio
import itertools
import traceback

from PhoneBoom.config import *
from logzero import logger
from pyppeteer import launch

headless = True
browser = None
numbers = range(3)
async def init(headless=headless):
    global browser
    logger.info('start task init Browser')
    browser = await launch({'headless': headless})
    logger.info('Browser inited')


async def main(num, website, url, jscode, **kws):
    global browser
    logger.info(f'start task: {website}--{num}')
    context = await browser.createIncognitoBrowserContext()
    try:
        page = await context.newPage()
        await page.goto(url)
        await asyncio.sleep(0.5)
        await page.evaluate(jscode.format(num))
        await asyncio.sleep(0.2)
        logger.info(f'task: {website}--{num} succeed')
    except:
        # print(traceback.format_exc())
        logger.error(f'task: {website}--{num} failed')
    finally:
        await asyncio.sleep(10)
        await context.close()


async def close():
    global browser
    logger.info('task finished close Browser')
    await browser.close()
    logger.info('Browser closed')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(asyncio.wait([init(), ]))
    run_queues = list(itertools.chain(*[[main(num=number, **i) for i in website] for number in numbers]))
    asyncio.get_event_loop().run_until_complete(asyncio.wait(run_queues))
    asyncio.get_event_loop().run_until_complete(asyncio.wait([close(), ]))
