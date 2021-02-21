from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=schemas.Wijsheid)
def read_wijsheid(
) -> Any:
    """
    Retrieve wijsheid.
    """

    return {"msg": "Word received"}
