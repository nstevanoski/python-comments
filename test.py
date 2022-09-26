import json
from telethon import TelegramClient, sync

api_id = 9312723
api_hash = 'e99afd73a5e31cb8285fd224d0370026';

client = TelegramClient('xxx', api_id, api_hash).start()

users = [];

def get_comments(client: TelegramClient, channel: str, message_id: int):
    async def crawl_comments():
        async for message in client.iter_messages(channel, reply_to=message_id):
            # print(message.text)  # only comment
            full_comment_obj = message.to_dict()  # in JSON-Format
            # print(full_comment_obj)
            # y = json.dumps(message.from_id.to_dict());

            users.append(message.from_id.to_dict());

    with client:
       client.loop.run_until_complete(crawl_comments())



get_comments(client, 'whip347', 74053)
    
print(json.dumps(users));