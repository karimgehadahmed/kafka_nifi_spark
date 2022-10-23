from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import model
from app.api import deps
from app.schemas.analytical_schema import AnalyticalDB
from typing import List
router = APIRouter()


@router.get("/", response_model=List[AnalyticalDB], status_code=200)
def get_all_data(
    *,
    db: Session = Depends(deps.get_db),
) -> Any:
    analysis_data = db.query(model.Analysis).all()
    
    return analysis_data
