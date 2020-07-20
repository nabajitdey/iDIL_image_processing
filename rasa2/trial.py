import requests

# sender = input("What is your name?\n")

bot_message = ""
while True:
    message = input("What's your message?\n")

    print("Sending message now...")

    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message, "sender":"me"})

    print("Bot says, ")
    print(r)
    print(r.json())
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")
