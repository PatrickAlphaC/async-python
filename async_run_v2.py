import asyncio
import aiohttp
import os
import time

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL','AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []

start = time.time()

def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        # for response in responses:
        #     results.append(await response.json())

asyncio.run(get_symbols())

end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print('You did it!')
