import os
import requests
import time

TOKEN = os.getenv("BOT_TOKEN")
API = "https://botapi.rubika.ir/v3"

def send_message(chat_id, text):
    requests.post(
        f"{API}/{TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text}
    )

def main():
    offset = 0
    while True:
        try:
            r = requests.post(
                f"{API}/{TOKEN}/getUpdates",
                json={"offset": offset}
            ).json()

            for update in r.get("data", []):
                offset = update.get("update_id", offset) + 1
                msg = update.get("message", {})
                chat_id = msg.get("chat_id")
                text = msg.get("text", "")

                if not chat_id:
                    continue

                if text == "/start":
                    send_message(chat_id, "سلام شاهتوت! 👑🍇 ربات آماده است.")

                elif text == "/mods":
                    send_message(chat_id, "به بخش مودهای ماینکرفت خوش آمدی! 🍇")

                else:
                    send_message(chat_id, "دستور را متوجه نشدم. /mods را امتحان کن.")

        except Exception as e:
            print(e)

        time.sleep(3)

if __name__ == "__main__":
    main()
