# # # from requests import Session
# # #
# # # api_key = '67a37e37c32aac4d1a47e51a7c9ce343'
# # #
# # #
# # # # response = requests.get(
# # # #     url='https://api.openweathermap.org/data/2.5/weather',
# # # #     params={
# # # #         'appid': api_key,
# # # #         'lat': 53.893009,
# # # #         'lon': 27.567444,
# # # #         'units': 'metric',
# # # #         'lang': 'ru'
# # # #     }
# # # # )
# # # with Session() as session:  # type: Session
# # #     response = session.get(
# # #             url='https://api.openweathermap.org/data/2.5/weather',
# # #             params={
# # #                 'appid': api_key,
# # #                 'lat': 53.893009,
# # #                 'lon': 27.567444,
# # #                 'units': 'metric',
# # #                 'lang': 'ru'
# # #             }
# # #         )
# # #     print(response.url)
# # #     print(response.headers)
# # #     print(response.cookies)
# # #     print(response.json())
# # #     # response.encoding = 'utf-8'
# # #     print(response.text)
# # #     print(response.status_code)
# # from aiohttp import ClientSession
# # from ujson import dumps, loads
# #
# #
# # async def main():
# #     async with ClientSession(
# #         base_url='https://api.openweathermap.org',
# #         json_serialize=dumps
# #     ) as session:
# #         response = await session.get(
# #             url='/data/2.5/weather',
# #             params={
# #                 'appid': '67a37e37c32aac4d1a47e51a7c9ce343',
# #                 'lat': 53.893009,
# #                 'lon': 27.567444,
# #                 'units': 'metric',
# #                 'lang': 'ru'
# #             }
# #         )
# #         print(response.url)
# #         print(response.headers)
# #         print(response.cookies)
# #         print(await response.text())
# #         print(await response.json(loads=loads))
# #         print(response.status)
# #
# #
# # if __name__ == '__main__':
# #     import asyncio
# #     asyncio.run(main())
# from aiohttp import ClientSession
#
#
# async def main():
#     async with ClientSession() as session:
#         async with session.ws_connect('wss://demo.piesocket.com/v3/channel_123?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self') as wss:
#             while True:
#                 data = await wss.receive()
#
#
# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())
