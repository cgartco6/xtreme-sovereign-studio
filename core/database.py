from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, PRIMARY KEY=True)
    customer_email = Column(String)
    product_name = Column(String)
    amount_paid = Column(Float)
    file_path = Column(String) # Path to the generated ZIP/PDF
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine('sqlite:///xtreme_studio.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
