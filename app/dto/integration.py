from typing import List
from pydantic import BaseModel


class CuacaDetail(BaseModel):
    tanggal: str
    hari: str
    suhu_udara: float
    kelembapan_udara: float
    keterangan: str
    image: str

class CuacaResponse(BaseModel):
    lokasi: str
    cuaca: List[CuacaDetail]

