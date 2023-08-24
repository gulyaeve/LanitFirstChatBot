# import asyncio
import logging

import aiohttp


class BaseAPI:
    def __init__(self, base_link: str, base_token: str = ""):
        self._link = base_link
        self._token = base_token
        if self._token:
            self.headers = {
                "Authorization": f"Bearer {self._token}",
                "Accept": "*/*",
            }
        else:
            self.headers = {
                "Accept": "*/*",
            }

    async def get_json(self, route: str, params: dict | None = None):
        if params is None:
            params = {}
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(
                    url=f"{self._link}{route}",
                    params=params,
                    verify_ssl=False,
                ) as resp:
                    logging.info(f"{resp.status} {self._link}{route}")
                    return await resp.json()
        except aiohttp.ClientConnectionError:
            logging.warning(f"Api is unreachable {self._link}{route}")
        except Exception as e:
            logging.warning(f"Api is unreachable: {e}")

    async def get_data(self, route: str, params: dict | None = None):
        if params is None:
            params = {}
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(
                    url=f"{self._link}{route}",
                    params=params,
                    verify_ssl=False,
                ) as resp:
                    logging.info(f"{resp.status} {self._link}{route}")
                    return await resp.read()
        except aiohttp.ClientConnectionError:
            logging.warning(f"Api is unreachable {self._link}{route}")
        except Exception as e:
            logging.warning(f"Api is unreachable: {e}")


# async def test():
#     cat_api = BaseAPI("https://cataas.com")
#     cat_pic = await cat_api.get_data("/cat")
#     print(cat_pic)
#
#
# if __name__ == '__main__':
#     asyncio.run(test())


