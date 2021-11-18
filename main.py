from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import aiohttp
import bs4
from tortoise.contrib.fastapi import register_tortoise
from config.settings import get_settings
from config.db import DB_CONFIG
import api_views
import uvicorn


settings = get_settings()


app = FastAPI(title=settings.APP_NAME)
app.include_router(router=api_views.router)


def convert_sources(content: str):
    soup = bs4.BeautifulSoup(content)
    frontend_host = 'http://localhost:3000'
    for script in soup.findAll('script'):
        if script.get('src', '').startswith('/'):
            script['src'] = frontend_host + script['src']
    for link in soup.findAll('link'):
        if link.get('href', '').startswith('/'):
            link['href'] = frontend_host + link['href']
    for rel in soup.findAll('link', {'rel': 'manifest'}):
        rel.decompose()
    return str(soup)


@app.get('/{full_path:path}')
async def root(request: Request, full_path: str):
    async with aiohttp.ClientSession() as sesh:
        async with sesh.get('http://localhost:3000') as response:
            content = await response.text()
            content = convert_sources(content)
            return HTMLResponse(content)


register_tortoise(
    app,
    config=DB_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)
