from aiohttp import web
from database import save_gift

routes = web.RouteTableDef()

@routes.get('/api/send_gift')
async def send_gift(request):
    user_id = request.query.get("user_id")
    gift = request.query.get("gift")

    if not user_id or not gift:
        return web.json_response({"error": "Missing parameters"}, status=400)

    save_gift("some_sender", user_id, gift)

    from bot import bot
    try:
        await bot.send_message(user_id, f"🎁 Вы получили подарок: {gift}!")
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

    return web.json_response({"status": "ok"})

@routes.get('/')
async def index(request):
    with open('templates/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

app = web.Application()
app.add_routes(routes)