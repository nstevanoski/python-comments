import json
import random
import time
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

def getComments(client: TelegramClient, channel: str, message_id: int):
    async def crawl_comments():
        async for message in client.iter_messages(channel, reply_to=message_id):
            full_comment_obj = message.to_dict()  # in JSON-Format
            users.append(message.from_id.to_dict());
            # print(full_comment_obj)

    with client:
       client.loop.run_until_complete(crawl_comments())

def sendMessage(client: TelegramClient):
    async def sMessage():
        messages = [
            "Hey, I really like your comments on the channel and your way of thinking. i want to invite you to this private Q channel,\nIf you are one of Us, click on the link bellow, Request to Join and i will tell to the admin to ACCEPT your REQUEST.\n\n👇👇👇\n**https://t.me/+uNbRKfySZfE2ODY0**", 
            "Hello fellow patriot, I have noticed that you are commenting all the time against the dark schemes of the Elites... I really think that you will fit in this private channel just for real Patriots and Freedom Fighters. Click on the link to join to this secret channel, i will tell the admin to approve your membership.\n\n👇👇👇\n**https://t.me/+uNbRKfySZfE2ODY0**", 
            "Hey i am feeling your anger too, i can see from your comments on different channels that you have had enough of the Dark Scenario. We all have had enough from this Satanic elites.\n\nPlease join us on this Private Channel, i will tell to the admin to approve your request.\n\nWWG1WGA\nIf you know, you know.\n\n👇👇👇\n**https://t.me/+uNbRKfySZfE2ODY0**"
        ];
        await client.send_message(1735607573, random.choice(messages))
        time.sleep(30)
        print('Sleeping 30s..')

    with client:
       client.loop.run_until_complete(sMessage())

# Call functions

# getComments(client, 'whip347', 74053);
sendMessage(client);
# print(json.dumps(users)); 


