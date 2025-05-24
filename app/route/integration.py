from fastapi import APIRouter

from app.repository.integration import integration as integrationRepo
from app import dto


router = APIRouter(prefix="/cuaca", tags=["integration"])


@router.get("/{adm4}",
    response_model=dto.CuacaResponse,
    description="Get weather forecast data from BMKG API use adm4 https://kodewilayah.id/ e.g: 34.71.07.1002"
)
def get_cuaca(adm4: str = "34.71.07.1002"):
    cuaca = integrationRepo.get_cuaca(adm4=adm4)
    return cuaca
