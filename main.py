
import os
import time
import requests

TOKEN = os.getenv("BOT_TOKEN")
API = f"https://botapi.rubika.ir/v3/{TOKEN}"

def send_message(chat_id, text):
    requests.post(
        f"{API}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=30
    )

def main():
    offset_id = None

    while True:
        try:
            data = {"limit": 20}
            if offset_id:
                data["offset_id"] = offset_id

            response = requests.post(
                f"{API}/getUpdates",
                json=data,
                timeout=40
            ).json()

            result = response.get("data", {})
            offset_id = result.get("next_offset_id", offset_id)

            for update in result.get("updates", []):
                if update.get("type") != "NewMessage":
                    continue

                chat_id = update.get("chat_id")
                message = update.get("new_message", {})
                text = message.get("text", "").strip()

                if not chat_id:
                    continue

                if text == "/start":
                    send_message(
                        chat_id,
                        "سلام! 👑 ربات شاهتوت آماده است."
                    )
                elif text == "/mods":
                    send_message(
                        chat_id,
                        "🔥 بخش مودها به‌زودی فعال می‌شود!"
                    )
                elif text == "/help":
                    send_message(
                        chat_id,
                        "دستورات:\n/start\n/mods\n/help"
                    )

        except Exception as error:
            print("Error:", error)
            time.sleep(5)

if __name__ == "__main__":
    main()
          
