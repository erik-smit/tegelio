from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from random import randrange

router = APIRouter()


@router.get("/", response_model=schemas.Wijsheid)
def read_wijsheid(
) -> Any:
    """
    Retrieve wijsheid.
    """

    messages = [
        "wijsheid 1",
        "wijsheid 2",
        "wijsheid 3"
        ]

    message = messages[randrange(start=0, stop=len(messages))]

    return {"msg": message}
