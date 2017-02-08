from sqlalchemy import Column, Integer, String
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
class Message(Base):
    __tablename__ = 'messages'

    sid          = Column(String, primary_key=True)
    datecreated  = Column(String)
    dateupdated  = Column(String)
    datesent     = Column(String)
    accountsid   = Column(String)
    #messagingservicesid
    fromnumber   = Column(String)
    tonumber     = Column(String)
    body         = Column(String)
    nummedia     = Column(Integer)
    numsegments  = Column(Integer)
    status       = Column(String)
    errorcode    = Column(String)
    errormessage = Column(String)
    direction    = Column(String)
    price        = Column(String)
    princeunit   = Column(String)
    apiversion   = Column(String)
    uri          = Column(String)
    subresourceuri = Column(String)

    def __repr__(self):
        return '<Message(sid={}, fromnumber={}, tonumber={}, body={})>'.format(self.sid, self.fromnumber, self.tonumber, self.body)
