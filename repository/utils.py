import requests
from config.config import URL_ENTIDAD, url_edad


class CodigoEntidad:
    @classmethod
    def get(cls, entidad):
        url = URL_ENTIDAD
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()["datos"]
            for ent in datos:
                if ent["nom_agee"] == entidad:
                    return ent["cve_agee"]
            return None


class EdadMedia:
    @classmethod
    def get(cls, entidad):
        codigo = CodigoEntidad.get(entidad)
        if codigo:
            url = url_edad(codigo)
            response = requests.get(url)
            if response.status_code == 200:
                return int(float(response.json()["Series"][0]["OBSERVATIONS"][0]["OBS_VALUE"]))
        return None


