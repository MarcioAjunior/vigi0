import hug
from configMongo import myConnection
from controllers.pesquisasController import allPesquisas
from mongoengine import connect

api = hug.API(__name__)
connect(
   host="mongodb+srv://admin:admin@devunc-marcio.lkpu4.mongodb.net/vigi0",
   alias="default"
         )

#Minhas rotas
@hug.get('/')
def listPesquisas(response):
    """ Retorna todas as pesquisas  """
    return allPesquisas(response)

