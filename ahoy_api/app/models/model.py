from sqlalchemy import Boolean, Column, Integer, String , Float,DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base


class Analysis(Base):
    __tablename__ = "analysis_data"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime, nullable=True)
    average_rating = Column(Float,nullable=True)
    total_count = Column(Integer,nullable=True)
    max_rating = Column(Float,nullable=True)
    min_rating = Column(Float,nullable=True)