# -*- coding: utf-8 -*-
from flask import Flask, g
from .models import Contact, Message
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('mysql+mysqldb://scott:tiger@localhost:5432/mydatabase')

@app.route('/receive', methods=['POST'])
def sms():
    transmitted = dt.datetime.now()
    f = request.form
    msg = Message(sid=f['MessageSid'],
                  datecreated=None,  # This is for outgoing
                  dateupated=None,  # This is for outgoing
                  datesent=None,  # This is for outgoing
                  accountsid=f['AccountSid'],
                  fromnumber=f['From'],
                  tonumber=f['To'],
                  body=f['body'],
                  nummedia=int(f['NumMedia']),
                  numsegments=int(f['NumSegments']),
                  status=f['SmsStatus']
                  errorcode=f.get('SmsErrorCode', None),  # Will we ever get one like this?
                  errormessage=f.get('SmsErrorMessage', None),
                  direction='inbound',  # safe to assume here
                  price=f.get('Price', None),  # unconfirmed
                  price=f.get('Price', None),  # unconfirmed
                  apiversion=f['ApiVersion'],
                  uri=f.get('Uri', None),  # unconfirmed
                  subresourceuri=f.get('SubresourceUri', None),  #unconfirmed
                  )
