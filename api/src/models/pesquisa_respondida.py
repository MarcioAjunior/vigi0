from mongoengine import (
    Document,
    ListField,
    ReferenceField,
    StringField
)  
from models.pesquisas import Pesquisas
from models.respostas import Respostas

class PesquisaRespondida(Document):
    pesquisa = ReferenceField(Pesquisas)
    respostas = ListField(ReferenceField())
