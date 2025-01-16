from pydantic import BaseModel, HttpUrl
from typing import List


class ImageData(BaseModel):
    id: str
    url: HttpUrl
    width: int
    height: int


class ImageResponse(BaseModel):
    data: List[ImageData]


class UploadImage(BaseModel):
    id: str
    url: HttpUrl
    width: int
    height: int
    original_filename: str
    pending: int
    approved: int
