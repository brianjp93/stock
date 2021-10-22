from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import aiohttp
import bs4

import api_views

app = FastAPI()
app.include_router(router=api_views.router)


def convert_sources(content: str):
    soup = bs4.BeautifulSoup(content)
    frontend_host = 'http://localhost:3000'
    for script in soup.findAll('script'):
        if script.get('src', '').startswith('/'):
            script['src'] = frontend_host + script['src']
    return str(soup)


@app.get('/{full_path:path}')
async def root(request: Request, full_path: str):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:3000') as response:
            content = await response.text()
            content = convert_sources(content)
            return HTMLResponse(content)
