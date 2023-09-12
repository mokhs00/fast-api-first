from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from dto.sample import CreateSampleRequest
from models import Sample

router = APIRouter()


@router.get("/")
def list_samples(
        db: Session = Depends(get_db)
):
    sample_list = db.query(Sample).all()
    return {
        "sample_list": sample_list
    }


@router.post("/")
def create(
        req: CreateSampleRequest,
        db: Session = Depends(get_db)
):
    sample = Sample(value=req.value)

    db.add(sample)
    db.commit()
    db.refresh(sample)

    return sample
