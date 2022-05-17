from flask import request
from flask_restful import Resource
from repository.utils import EdadMedia
from flask_expects_json import expects_json
from schema import entrada


class ApiEdad(Resource):
    @expects_json(entrada)
    def get(self):
        try:
            entidad = request.json["entidad"]
            edad = EdadMedia.get(entidad)
            if edad:
                return {"info": {"entidad": entidad, "edad media poblacional": edad}}
            return {"error": "no se encontró la entidad."}, 404
        except Exception as e:
            return {"error": str(e)}, 500
    
