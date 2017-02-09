from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'

    number = Column(String(11), primary_key=True)
    name   = Column(String(255))
    fixed  = Column(Integer)  # 1 means user-defined, static, name, 0 else
    unread = Column(Integer)  # 1 means there are unread messages

    def __repr__(self):
        return '<Contact(number={}, name={}, fixed={}, unread={})>'.format(self.number, self.name, self.fixed, self.unread)


#Reference
#https://www.twilio.com/docs/api/rest/message
#String(32) seems safe for RFC 2882 strings, which I think are 31 characters
class Message(Base):
    __tablename__ = 'messages'

    sid          = Column(String(34), primary_key=True)
    datecreated  = Column(String(32))
    dateupdated  = Column(String(32))
    datesent     = Column(String(32))
    accountsid   = Column(String(34))
    #messagingservicesid
    fromnumber   = Column(String(11))
    tonumber     = Column(String(11))
    body         = Column(Text)
    nummedia     = Column(Integer)
    numsegments  = Column(Integer)
    status       = Column(String(11))  # 'undelivered' is longest value
    errorcode    = Column(String(5))
    errormessage = Column(Text)  # The error mapping may as well be its own table
    direction    = Column(String(14))  # 'outbound-reply' is longest value
    price        = Column(String(16))  # safe limit, who knows
    princeunit   = Column(String(3))
    apiversion   = Column(String(12))  # like '2010-04-01', with extra 2
    uri          = Column(Text)
    subresourceuri = Column(Text)

    def __repr__(self):
        return '<Message(sid={}, fromnumber={}, tonumber={}, body={})>'.format(self.sid, self.fromnumber, self.tonumber, self.body)
