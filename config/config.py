# Datos para consultar recursos externos

KEY="4adcd6d0-a367-f6cb-7245-0944fe13b533" #  Api Key INEGI 
INDICADOR="070000" #  01 ---> Entidad federativa  0001 ---> Municipio
URL_ENTIDAD="https://gaia.inegi.org.mx/wscatgeo/mgee/"


def url_edad(codigo):
    return f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000010/es/070000{codigo}/true/BISE/2.0/{KEY}?type=json"




