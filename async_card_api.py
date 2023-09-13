import json
import asyncio
import aiohttp


VALID_STATUSES = [200, 301, 302, 307, 404]
api_link = "https://api.scryfall.com/cards/named?fuzzy="
deck_list = ['Mana Crypt', "Mox Amber", "Mox Opal", "Sol Ring"]


async def req_json(session, api_link):
    try:
        async with session.get(api_link, timeout=500) as resp:
            await resp.json()
            # asyncio.sleep is used to restrict requests to < 10 per sec, per skcryfall api guidelines.
            await asyncio.sleep(.12)
            if resp.status in VALID_STATUSES:
                async with session.get(resp.url, timeout=500) as json_resp:
                    print(json.loads(await json_resp.read()))
    except Exception as e:
        print(f"Exception: {e}")


async def main():
    tcp_connection = aiohttp.TCPConnector(limit=250)
    header = {"Authorization": "Basic bG9naW46cGFzcw=="}
    async with aiohttp.ClientSession(connector=tcp_connection, headers=header, trust_env=True) as session:
        try:
            tasks = [asyncio.create_task(req_json(session, api_link=api_link+card)) for card in deck_list]
            for task in tasks:
                await task
        except Exception as e:
            print(f"Exception: {e}")
        await asyncio.sleep(0)


asyncio.run(main())

