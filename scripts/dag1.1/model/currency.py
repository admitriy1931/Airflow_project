from sqlalchemy import Column, Integer, VARCHAR, Date, Boolean, Float, TIMESTAMP
import sys
sys.path.append("..")

from model.base import Base
class Currency(Base):
    __tablename__ = 'vac'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    vacancy = Column(VARCHAR(50), nullable=False)
    company = Column(VARCHAR(50), nullable=False)
    web_cite = Column (VARCHAR(50), nullable=False)