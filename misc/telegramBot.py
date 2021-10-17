import requests as requests
import random

url = "https://api.telegram.org/bot1181286101:<KEY>"


# create func that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# create function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text,'parse_mode':'HTML'}
    response = requests.post(url + "sendMessage", data=params)
    return response

def returnHTML(url):
    r = requests.get(url, allow_redirects=True)
    # print(r.content)

    return(str(r.content))

# create main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello":
                send_message(get_chat_id(update), 'Hello Welcome to our bot.')
        
            else:
                send_message(get_chat_id(update), " you")
            update_id += 1

            if get_message_text(update).lower() == "google":
                st = returnHTML('http://www.google.com')
                
                send_message(get_chat_id(update), st)
# call the function to make it reply
# main()
url = "<URL>"

r = requests.get(url, allow_redirects=True)
print(r)
