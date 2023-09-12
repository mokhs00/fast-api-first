from pydantic import BaseModel


class CreateSampleRequest(BaseModel):
    value: str
