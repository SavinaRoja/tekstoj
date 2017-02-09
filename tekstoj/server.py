# -*- coding: utf-8 -*-
from flask import Flask, g
from models import Contact, Message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#These will be configurable, non-committed, things later
DB_USER = 'tekstoj-server'  # This user has rights to edit
DB_PASS = 'server-secret'
DB_NAME = 'tekstoj'  # The database we will connect to

app = Flask(__name__)
db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(DB_USER,
                                                     DB_PASS,
                                                     DB_NAME)
#g.engine = create_engine(db_url)
#g.Session = sessionmaker(bind=g.engine)

def get_session():
    if not hasattr(g, 'Session'):
        engine = create_engine(db_url)
        g.Session = sessionmaker(bind=engine)
    return g.Session()


@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/receive', methods=['POST'])
def sms():
    #transmitted = dt.datetime.now()
    f = request.form
    print(f)
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
                  status=f['SmsStatus'],
                  errorcode=f.get('SmsErrorCode', None),  # Will we ever get one like this?
                  errormessage=f.get('SmsErrorMessage', None),
                  direction='inbound',  # safe to assume here
                  price=f.get('Price', None),  # unconfirmed
                  priceunit=f.get('PriceUnit', None),  # unconfirmed
                  apiversion=f['ApiVersion'],
                  uri=f.get('Uri', None),  # unconfirmed
                  subresourceuri=f.get('SubresourceUri', None),  #unconfirmed
                  )
    session = get_session()
    session.add(msg)
    session.commit()

if __name__ == '__main__':
  app.run(host='0.0.0.0')
