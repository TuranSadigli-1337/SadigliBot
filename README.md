# SadigliBot 

## Quraşdırma və Başlatma

Python `3.7.3` vəya üstü tələb olunur.

Lazımi paketləri quraşdırın (locally):

```
bash python3 -m pip install -r requirements.txt
```

`.env.sample`-ni `.env ` olaraq kopyalayın

```
cp .env.sample .env

```

`.env` açın və aşağıdakilərə əməl edin:

| Hazır           | Dəyişin:                                                           
|-----------------|-----------------------------------------------------------------------|
| `DISCORD_TOKEN` | Discord bot token                                                     |

Botun Başladılması:

```
python3 bot.py
```

