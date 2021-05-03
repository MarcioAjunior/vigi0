import json
from models.pesquisas import Pesquisas


def allPesquisas(response):
    try :
        data = Pesquisas.objects
        arr = [ item.to_dict() for item in data]
        return { "result" : arr }
    except Exception as e :
        print(e)