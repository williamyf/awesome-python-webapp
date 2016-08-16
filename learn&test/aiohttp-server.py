from aiohttp import web

async def handle(req):
	name = req.match_info.get('name', 'Anonymous')
	text = 'hello, '+name
	return web.Response(body=text.encode('utf-8'))

app = web.Application()
app.router.add_route('GET', '/{name}', handle)
web.run_app(app)