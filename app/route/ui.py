from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.repository.integration import integration as integrationRepo


templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/ui", tags=["ui"])


@router.get("/")
async def read_ui(request: Request, location: str = "34.71.07.1002"):
    if not location:
        location = "34.71.07.1002"
    datas = integrationRepo.get_cuaca(adm4=location)
    lokasi = datas.get("lokasi")
    cuaca = datas.get("cuaca")
    if not cuaca:
        lokasi = "Data tidak ditemukan"
        cuaca = []

    return templates.TemplateResponse("cuaca.html", {"request": request, "location": location, "datas": cuaca, "location_str": lokasi})
