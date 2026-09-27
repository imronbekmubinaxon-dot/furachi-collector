import os
import logging
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

# =========================================================
# CONFIG
# =========================================================

API_ID = int(os.getenv("TELEGRAM_API_ID", "0"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

if not API_ID:
    raise RuntimeError("TELEGRAM_API_ID topilmadi!")

if not API_HASH:
    raise RuntimeError("TELEGRAM_API_HASH topilmadi!")


# Hozircha faqat BITTA kanal
CHANNELS = [
    "@logistika_fura",
]


# =========================================================
# LOGGING
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("furachi-collector")


# =========================================================
# TELEGRAM CLIENT
# =========================================================

client = TelegramClient(
    "furachi_collector",
    API_ID,
    API_HASH
)


# =========================================================
# NEW MESSAGE
# =========================================================

@client.on(events.NewMessage(chats=CHANNELS))
async def new_message_handler(event):

    message = event.message

    text = message.raw_text or ""

    if not text.strip():
        return

    chat = await event.get_chat()

    username = getattr(chat, "username", None)

    print()
    print("=" * 60)
    print("🚛 YANGI YUK XABARI")
    print("=" * 60)

    print(f"Channel: @{username}" if username else "Channel: unknown")
    print(f"Message ID: {message.id}")
    print(f"Date: {message.date}")
    print("-" * 60)

    print(text)

    print("=" * 60)
    print()


# =========================================================
# START
# =========================================================

async def main():

    print()
    print("=" * 60)
    print("FURACHI TELEGRAM COLLECTOR")
    print("=" * 60)

    print("Kanallar:")

    for channel in CHANNELS:
        print(f"  - {channel}")

    print()
    print("Telegram'ga ulanmoqda...")

    await client.start()

    me = await client.get_me()

    print()
    print("✅ Telegram ulanish muvaffaqiyatli!")

    if me:
        print(f"Account: {me.first_name}")
        print(f"Username: @{me.username}" if me.username else "Username: yo'q")

    print()
    print("📡 Collector ishlayapti...")
    print("Yangi xabar kutilmoqda.")
    print()

    await client.run_until_disconnected()


if __name__ == "__main__":

    import asyncio

    asyncio.run(main())
