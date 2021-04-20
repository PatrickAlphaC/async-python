import aiohttp
import asyncio
import os
import time
# To work with the .env file
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
URL = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
SYMBOLS = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'GOOGL']
results = []


def get_tasks(session):
    tasks = []
    for symbol in SYMBOLS:
        tasks.append(session.get(URL.format(symbol, API_KEY), ssl=False))
    return tasks


async def run_tasks():
    session = aiohttp.ClientSession()
    # tasks = get_tasks(session)
    tasks = [session.get(URL.format(symbol, API_KEY), ssl=False) for symbol in SYMBOLS]

    # Can't do this!!
    # for symbol in symbols:
    #     tasks.append(session.get(url.format(symbol, api_key)))
    responses = await asyncio.gather(*tasks)
    for response in responses:
        results.append(await response.json())
    await session.close()

print("Timer started...")
start = time.time()
# asyncio.run(run_tasks())
loop = asyncio.get_event_loop()
results = loop.run_until_complete(run_tasks())
loop.close()
end = time.time()
total_time = end - start
print(
    f"Time to make {len(SYMBOLS)} API calls with tasks, it took: {total_time}")
