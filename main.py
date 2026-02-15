import requests
import random
import os
from datetime import datetime

# GitHub'daki gizli anahtarı alıyoruz
webhook_url = os.environ['DISCORD_WEBHOOK']

# Şehirler ve İhtimaller
durumlar = ["Güneşli ☀️", "Parçalı Bulutlu ⛅", "Sağanak Yağışlı 🌧️", "Sisli 🌫️", "Fırtınalı ⛈️", "Rüzgarlı 🍃"]

# Yeni Atheria (Başkent - Daha iyi hava)
atheria_durum = random.choice(durumlar[:4]) 
atheria_derece = random.randint(18, 28)

# Velen (Orman - Daha kötü hava)
velen_durum = random.choice(durumlar[2:])
velen_derece = random.randint(10, 19)

# Demirçiğ (Sanayi - Soğuk)
demircig_durum = random.choice(durumlar[3:])
demircig_derece = random.randint(-2, 12)

# Mesaj Verisi
data = {
    "username": "Kraliyet Meteoroloji",
    "avatar_url": "https://cdn-icons-png.flaticon.com/512/1163/1163661.png",
    "embeds": [{
        "title": "📜 ATHERIS KRALLIĞI GÜNLÜK HAVA RAPORU",
        "description": "**Kraliyet Rasathanesi anlık verileri sunar:**",
        "color": 3447003,
        "fields": [
            {
                "name": "🏰 Yeni Atheria (Başkent)",
                "value": f"Durum: **{atheria_durum}**\nSıcaklık: **{atheria_derece}°C**\n*Başkentte ticaret canlı.*",
                "inline": False
            },
            {
                "name": "🌲 Velen Bölgesi",
                "value": f"Durum: **{velen_durum}**\nSıcaklık: **{velen_derece}°C**\n*Orman yollarında dikkat.*",
                "inline": False
            },
            {
                "name": "⚙️ Demirçiğ Sanayi",
                "value": f"Durum: **{demircig_durum}**\nSıcaklık: **{demircig_derece}°C**\n*Madenlerde çalışma sürüyor.*",
                "inline": False
            }
        ],
        "footer": {
            "text": f"Rapor Zamanı: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        }
    }]
}

requests.post(webhook_url, json=data)
