from typing import Any, List, Optional
from datetime import datetime
from pydantic import BaseModel


class AnalyticalDB(BaseModel):
    id: int
    date_time: datetime
    average_rating : Optional[float]=0
    total_count: Optional[int]=0
    max_rating: Optional[float]=0
    min_rating: Optional[float]=0

    
    class Config:
        orm_mode = True
