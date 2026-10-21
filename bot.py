import time
import requests

TOKEN = "8630253994:AAHpaMF9DnGQ6ZdudE-EYb3i7Lt1EHLOv4"
URL = f"https://api.telegram.org/bot{TOKEN}/"

def main():
    offset = None
    print("Bot is starting on Render...")
    while True:
        try:
            url = URL + "getUpdates?timeout=30"
            if offset:
                url += f"&offset={offset}"
            res = requests.get(url, timeout=35).json()
            
            if "result" in res:
                for update in res["result"]:
                    offset = update["update_id"] + 1
                    if "message" in update and "text" in update["message"]:
                        chat_id = update["message"]["chat"]["id"]
                        text = update["message"]["text"]
                        
                        if text == "/start":
                            reply_text = "Welcome to Free Fire Like Bot! Send your UID to get likes."
                            requests.get(URL + f"sendMessage?chat_id={chat_id}&text={reply_text}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    main()
