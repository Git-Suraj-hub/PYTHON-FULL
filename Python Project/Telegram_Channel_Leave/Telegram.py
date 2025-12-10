from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.types import InputPeerUser

api_id = 22106475  # replace with your new API ID
api_hash = '2297294187d21640248018cda48052c6'  # replace with your new API Hash

with TelegramClient('Telegram12', api_id, api_hash) as client:
    me = client.get_me()
    print(f"Logged in as: {me.first_name} (@{me.username})")

    # Leave all groups and channels
    left_count = 0
    for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                client(LeaveChannelRequest(dialog.entity))
                print(f"✅ Left: {dialog.name}")
                left_count += 1
            except Exception as e:
                print(f"⚠️ Error with {dialog.name}: {e}")

    print(f"\n✅ Left {left_count} groups/channels.")

    # Delete all private chat history
    delete_count = 0
    for dialog in client.iter_dialogs():
        if dialog.is_user and not dialog.entity.bot:
            try:
                client(DeleteHistoryRequest(peer=dialog.entity, max_id=0, revoke=True))
                print(f"🗑️ Deleted chat: {dialog.name}")
                delete_count += 1
            except Exception as e:
                print(f"⚠️ Error deleting {dialog.name}: {e}")

    print(f"\n✅ Deleted {delete_count} private chats.")
