# -*- coding: utf-8 -*-
from flask import Flask, g, request, jsonify
from models import Contact, Message, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from twilio import twiml


#These will be configurable, non-committed, things later
DB_USER = 'tekstoj-server'  # This user has rights to edit
DB_PASS = 'server-secret'
DB_NAME = 'tekstoj'  # The database we will connect to

app = Flask(__name__)
db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(DB_USER,
                                                     DB_PASS,
                                                     DB_NAME)
def get_session():
    if not hasattr(g, 'Session'):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        g.Session = sessionmaker(bind=engine)
    return g.Session()


@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/receive', methods=['POST'])
def sms():
    session = get_session()
    f = request.form
    msg = Message(sid=f['MessageSid'],
                  datecreated=None,  # This is for outgoing
                  dateupdated=None,  # This is for outgoing
                  datesent=None,  # This is for outgoing
                  accountsid=f['AccountSid'],
                  fromnumber=f['From'],
                  tonumber=f['To'],
                  body=f['Body'],
                  nummedia=int(f['NumMedia']),
                  numsegments=int(f['NumSegments']),
                  status=f['SmsStatus'],
                  errorcode=f.get('SmsErrorCode', None),  # Will we ever get one like this?
                  errormessage=f.get('SmsErrorMessage', None),
                  direction='inbound',  # safe to assume here
                  price=f.get('Price', None),  # unconfirmed
                  priceunit=f.get('PriceUnit', None),  # unconfirmed
                  apiversion=f['ApiVersion'],
                  uri=f.get('Uri', None),  # unconfirmed
                  subresourceuri=f.get('SubresourceUri', None))  #unconfirmed
    session.add(msg)
    session.commit()
    session.close()
    return str(twiml.Response())

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
