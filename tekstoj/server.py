# -*- coding: utf-8 -*-
from flask import Flask, g
from .models import Contact, Message
from sqlalchemy import creat_engine

app = Flask(__name__)
engine = create_engine('mysql+mysqldb://scott:tiger@localhost:5432/mydatabase')

@app.route('/sms', methods=['POST'])
def sms():
    transmitted = dt.datetime.now()
    f = request.form
    contact_number = f['From']
    message_sid = f['MessageSid']
    account_sid = f['AccountSid']
    messaging_service_sid = f.get('MessagingServiceSid', '')
    body = f['Body']
    num_media = int(f['NumMedia'])
    outbound = 0


