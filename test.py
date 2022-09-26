import json
from telethon import TelegramClient

api_id = 9312723
api_hash = 'e99afd73a5e31cb8285fd224d0370026';

# if os.path.isfile('numbers_log.txt'):
#     with open('numbers_log.txt', 'r') as r:
#         data = r.readlines()
#     api_id = data[0]
#     api_hash = data[1]

# else:
#     api_id = input('Enter api_id: ')
#     api_hash = input('Enter api_hash: ')
#     with open('numbers_log.txt', 'w') as a:
#         a.write(api_id + '\n' + api_hash)

# client = TelegramClient('x2', api_id, api_hash)

client = TelegramClient('xxx', api_id, api_hash).start()
users = [];

def get_comments(client: TelegramClient, channel: str, message_id: int):
    async def crawl_comments():
        async for message in client.iter_messages(channel, reply_to=message_id):
            full_comment_obj = message.to_dict()  # in JSON-Format
            users.append(message.from_id.to_dict());

            print(full_comment_obj)

    with client:
       client.loop.run_until_complete(crawl_comments())

get_comments(client, 'whip347', 74053)
# print(json.dumps(users)); 