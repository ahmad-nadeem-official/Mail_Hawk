import os
import google.generativeai as genai
from simplegmail import message, Gmail
from simplegmail.query import construct_query



genai.configure()


gmail = Gmail()

def get_mail():
    # Unread messages in your inbox
    messages = gmail.get_unread_inbox()

    # Starred messages
    messages = gmail.get_starred_messages()

    # Print them out!
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Preview: " + message.snippet)     
        print("Message Body: " + message.plain)  # or message.html


get_mail()

 