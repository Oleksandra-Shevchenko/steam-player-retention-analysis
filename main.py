
import requests
import pandas as pd
import time
from tqdm import tqdm

time.sleep(60)  # safety delay to avoid violating the rate limit
all_url = "https://steamspy.com/api.php?request=all"
app_data = requests.get(all_url).json()
app_ids = list(app_data.keys())

all_games = []
DELAY_SECONDS = 1  
MAX_RETRIES = 3


for appid in tqdm(app_ids):
    for attempt in range(MAX_RETRIES):
        try:
            url = f"https://steamspy.com/api.php?request=appdetails&appid={appid}"
            resp = requests.get(url)
            game = resp.json()
            all_games.append(game)
            break
        except Exception as e:
            print(f"⚠️ erroe {appid}: {e}")
            time.sleep(2)
    time.sleep(DELAY_SECONDS)

df = pd.DataFrame(all_games)
df.to_csv("steamspy_full_dataset.csv", index=False, encoding="utf-8-sig")
