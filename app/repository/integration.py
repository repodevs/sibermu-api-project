import httpx
from datetime import datetime


class RepositoryIntegration:
    def get_cuaca(self, adm4: str = "34.71.07.1002"):
        """
        Get weather forecast data from BMKG API use adm4 https://kodewilayah.id/ e.g: 34.71.07.1002
        """
        api_url = f"https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={adm4}"

        res = httpx.get(api_url)
        if res.status_code != 200:
            return {
                "status": "error",
                "message": "Failed to fetch data from BMKG API",
            }
        res_json = res.json()

        data = res_json.get("data", [[]])[0]
        list_cuaca = data.get("cuaca", [[]])[0]
        lokasi = data.get("lokasi", {})
        lokasi_full = f'{lokasi.get("desa")}, {lokasi.get("kotkab")}'

        cuaca = []
        for item in list_cuaca:
            local_datetime = item.get("local_datetime")
            hari = datetime.strptime(local_datetime, "%Y-%m-%d %H:%M:%S").strftime("%A %H:%M") if local_datetime else None

            cuaca.append({
                "tanggal": local_datetime,
                "hari": hari,
                "suhu_udara": item.get("t"),
                "kelembapan_udara": item.get("hu"),
                "keterangan": item.get("weather_desc"),
                "image": item.get("image"),
            })

        resp = {
            "lokasi": lokasi_full,
            "cuaca": cuaca,
        }
        return resp

integration = RepositoryIntegration()
