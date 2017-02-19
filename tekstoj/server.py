# -*- coding: utf-8 -*-
from flask import Flask, g, request, jsonify, render_template, abort
from models import db, Account, Message, User
from twilio import twiml
from util import RequestValidator


#These will be configurable, non-committed, things later
DB_DRIVER = 'mysql+pymysql'
DB_USER = 'tekstoj-server'  # This user has rights to edit
DB_PASS = 'thisisasecret'
DB_NAME = 'tekstoj'  # The database we will connect to


def create_app():
    app = Flask("tekstoj-server")
    base = '{}://{}:{}@localhost/{}?charset=utf8'
    db_uri = base.format(DB_DRIVER, DB_USER, DB_PASS, DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app = create_app()

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/receive', methods=['POST'])
def handle_twilio_posts():
    f = request.form

    account = Account.query.get(f['AccountSid'])

    #Do nothing if we got a message for an unkown account
    if account is None:
        return str(twiml.Response())

    #We only want requests from Twilio, not just anyone, malicious or benign
    validator = RequestValidator(account.token)
    url = 'http://acidburn.jumpingcrab.com:5000/receive'
    signature = request.environ.get('HTTP_X_TWILIO_SIGNATURE')
    if not validator.validate(url, request.form, signature):
        return abort(404)  # Abort on false originator

    msg = Message(f['MessageSid'],
                  f['AccountSid'],
                  f['From'],
                  f['To'],
                  f['Body'],
                  int(f['NumMedia']),
                  int(f['NumSegments']),
                  f['SmsStatus'],
                  'inbound',
                  f['ApiVersion'],
                  
                  #errorcode=f.get('SmsErrorCode', None),
                  #errormessage=f.get('SmsErrorMessage', None),
                  #price=f.get('Price', None),  # unconfirmed
                  #priceunit=f.get('PriceUnit', None),  # unconfirmed
                  uri=f.get('Uri', None),  # unconfirmed
                  subresourceuri=f.get('SubresourceUri', None))  #unconfirmed
    db.session.add(msg)
    db.session.commit()
    return str(twiml.Response())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
