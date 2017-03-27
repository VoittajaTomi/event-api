from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from database import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event_title = Column(String(120))
    venue_name = Column(String(120))
    url = Column(Text)
    address = Column(Text)
    description = Column(Text)
    contact_details = Column(Text)
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    whole_day = Column(Boolean)
    family_event = Column(Boolean)
    fee = Column(Boolean)



    def __init__(self, event_title=None, venue_name=None, url=None, address=None, description=None, contact_details = None, starttime = None, endtime = None, family_event = None, fee=None, whole_day=None):

        self.event_title = event_title
        self.venue_name = venue_name
        self.address = address
        self.starttime = starttime
        self.endtime = endtime
        self.contact_details = contact_details


    def __repr__(self):
        return '<Event %s>' % (self.event_title)

