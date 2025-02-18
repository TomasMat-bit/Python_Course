from sqlalchemy import Column, create_engine, Integer, String, Float
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()

class Projektas(Base):
    __tablename__ = 'projektai'

    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    kaina = Column(Float)

    def __str__(self):
        return f'{self.id} {self.pavadinimas} {self.kaina}'

Base.metadata.create_all(engine)

print('------------------------------------------------------------------------------------------------------')




