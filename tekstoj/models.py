import bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    """
    An Account represents the data associated with the over-arching account
    for an organization and Twilio account.
    """

    sid   = db.Column(db.String(34), primary_key=True)
    token = db.Column(db.String(32))
    name  = db.Column(db.String(255), nullable=False)

    def __init__(self, sid, name, token=None):
        self.sid = sid
        self.name = name
        self.token = token


class User(db.Model):
    """
    """

    key          = db.Column(db.Integer,
                             primary_key=True,
                             autoincrement=True)
    name         = db.Column(db.String(255), nullable=False)
    accountsid   = db.Column(db.String(34), nullable=False)
    salt         = db.Column(db.String(29), nullable=False)
    hash         = db.Column(db.String(60), nullable=False)
    admin        = db.Column(db.Integer, nullable=False)

    def __init__(self, name, password, twilio_sid, admin=0):
        self.name = name
        self.twilio_sid = twilio_sid
        self.twilio_token = twilio_token
        self.salt = bcrypt.gensalt()
        self.hash = bcrypt.hashpw(password.encode('utf-8') + self.salt)
        self.admin = admin


class Message(db.Model):
    messagesid     = db.Column(db.String(34), primary_key=True)
    accountsid     = db.Column(db.String(34), nullable=False)
    #messagingservicesid
    fromnumber     = db.Column(db.String(12), nullable=False)
    tonumber       = db.Column(db.String(12), nullable=False)
    body           = db.Column(db.Text, nullable=False)
    nummedia       = db.Column(db.Integer, nullable=False)
    numsegments    = db.Column(db.Integer, nullable=False)
    #I think status is not null, "undelivered" longest val
    status         = db.Column(db.String(11), nullable=False)
    errorcode      = db.Column(db.String(5))
    errormessage   = db.Column(db.Text)  # The error mapping may as well be its own table
    direction      = db.Column(db.String(14), nullable=False)  # 'outbound-reply' is longest value
    price          = db.Column(db.String(16))  # safe limit, who knows
    priceunit      = db.Column(db.String(3))
    #apiversion looks like "2010-04-01", I added 2 to length
    apiversion     = db.Column(db.String(12), nullable=False)
    uri            = db.Column(db.Text)
    subresourceuri = db.Column(db.Text)
    datecreated    = db.Column(db.String(32))
    dateupdated    = db.Column(db.String(32))
    datesent       = db.Column(db.String(32))

    def __init__(self,
                 messagesid,
                 accountsid,
                 fromnumber,
                 tonumber,
                 body,
                 nummedia,
                 numsegments,
                 status,
                 direction,
                 apiversion,
                 #These below may be None/NULL
                 uri=None,
                 subresourceuri=None,
                 price=None,
                 priceunit=None,
                 #only present for errored messages
                 errorcode=None,
                 errormessage=None,
                 #These attributes exist for outbound
                 datecreated=None,
                 dateupdated=None,
                 datesent=None):
        self.messagesid = messagesid
        self.accountsid = accountsid
        self.fromnumber = fromnumber
        self.tonumber = tonumber,
        self.body = body,
        self.nummedia = nummedia,
        self.numsegments = numsegments,
        self.status = status,
        self.direction = direction,
        self.apiversion = apiversion,
        #These attributes below may be None/NULL
        self.uri = uri
        self.subresourceuri = subresourceuri=None,
        self.price = price
        self.priceunit = priceunit
        self.errorcode = errorcode
        self.errormessages = errormessage
        self.datecreated = datecreated
        self.dateupdated = dateupdated
        self.datesent = datesent
