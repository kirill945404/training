import requests
import schedule
from telegram import Bot
from telegram.error import TelegramError
import asyncio

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
TELEGRAM_BOT_TOKEN = '7258574628:AAEW9Q5hagEhgGbnKzq2nN8qFdOF6doW5rY'
# Замените 'YOUR_CHAT_ID' на ваш chat_id
TELEGRAM_CHAT_ID = '-4186337014'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_telegram_message(message):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except TelegramError as e:
        print(f'Failed to send message: {e}')

async def call_curl():
    url = 'https://soccerlife.ru/base.php?mode=trainingBase'
    headers = {
        'authority': 'soccerlife.ru',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'uid=XhriMWX50zS47+5wXpyuAg==; _ym_uid=1710871352534798389; _ym_d=1710871352; login=52herz; lang=ru; device=0; sid=6lgsso0igl3eve6ha48mh33c4m; accounts=Yld0NFNWcHExdkkrWGRlM0RLYVkvdVlIWDhOd3F6MmVxbDdCSXR4OGViaFFCdDBobkl2aWovOElYMWNkYnBReVhjZlpZRUFNUkVoSDVUNG9pVGlPOGhOellPRnFuZmRpOGpwUkFhZ3F4RVdxdWsyVStUV1dHTnByS083N0lvV1VOSVNvL1l6ZDFaa1BWOC81MXpKNGZEMVFRaWh4N21zbXl4OUdGUDFaaUFwVTQ0bTluMHBPbHh2ZnkyR1QvSUFSOjpsu5BtBeoi4RzIDfAi%2BIbT; password=UGtHNnI0RmROaXQyb3lya2NSaHBZdWxaYWRkVkFHUkY2T1E4WnY4Mk5mNEVhTWV6bzRGaXlwNFRYWU9XMUI0WlVsYmZ6ZmF5NkJ0RUE1czhWSGozd01hQXhQcndURVF1RmlvYWh6dENxZzJOcFRKOWRBWWRDam5TUytzdjF4VU4weHFYQlVzRWN2R3RsVmxRdlIvMG9RRkNLWWRBUnFCQnd4YnBqMkxQQ1pLS3NUYk5WN2szMzdsMFZ0eFNibVNFOjoPULJx9RHCXylSd%2FlJ870l; poly2=0; hostname=soccerlife.ru; _ym_isad=1; screen=1536x864',
        'origin': 'https://soccerlife.ru',
        'referer': 'https://soccerlife.ru/base.php?mode=trainingBase',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "YaBrowser";v="24.4", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
        'tt_plan[]': ['7', '8'],
        'teamid': '825',
        'update': '1'
    }

    try:
        # Выполняем POST-запрос
        response = requests.post(url, headers=headers, data=data)

        # Формируем сообщение
        message = (
            'Curl command executed successfully.\n'
            f'Status Code: {response.status_code}\n'
            f'Response: {response.text}'
        )

        # Отправляем сообщение в Telegram
        await send_telegram_message(message)

    except Exception as e:
        error_message = f'An error occurred: {e}'
        await send_telegram_message(error_message)

async def main():
    # Выполняем curl при запуске программы
    await call_curl()

    # Планируем выполнение задания каждый день в определенное время
    schedule.every().day.at("16:51").do(lambda: asyncio.create_task(call_curl()))

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
