# squarecloud unofficial API module

#=================================== Imports ======================================#
import asyncio
import aiohttp

from . import square_erro
#===================================================================================#

"""
    modulo que contem as funções que faz todas as requisições a API
    ================================================================
    * R_GET --> faz requisições com o metado GET a api
    * R_POST --> faz requisições com o metado POST a api
"""

class square_connection():
    def __init__(self, url, key_api):
        self.url = url
        self.key_api = key_api
        self.loop = asyncio.get_event_loop()
           
    def R_GET(self):
        return self.loop.run_until_complete(self._R_GET())
    
    def R_POST(self):
        return self.loop.run_until_complete(self._R_POST())
    
    async def _R_GET(self):
        async with aiohttp.ClientSession() as session:
            params = {"Authorization": f"{self.key_api}"}
            async with session.get(self.url, headers=params) as resp: 
                return await resp.json()
            
    async def _R_POST(self):
        async with aiohttp.ClientSession() as session:
            params = {"Authorization": f"{self.key_api}"}
            async with session.post(self.url, headers=params) as resp: 
                return await resp.json()