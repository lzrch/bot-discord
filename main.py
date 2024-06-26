import discord
import asyncio

# Masukkan token bot Anda di sini
TOKEN = 'MTI1NTU0NzYzNjA3Mzc2MjgyNw.GrY-Yk.RPxBd83sjEOLPQl9ZmjSGnFEHGgHIMPwHdPOGM'

# Buat daftar pesan yang akan dikirim
messages = [
    "Hi",
    "Hello",
    "Hi buddy",
    "Hello mate"
]

# ID channel di mana pesan akan dikirim
CHANNEL_ID = 1082877494467772477

# Inisialisasi bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_messages():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        for message in messages:
            await channel.send(message)
            await asyncio.sleep(180)  # Tunggu 3 menit (180 detik) sebelum mengirim pesan berikutnya

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(send_messages())

client.run(TOKEN)
