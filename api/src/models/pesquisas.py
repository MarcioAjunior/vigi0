from mongoengine import Document, StringField 

from models.perguntas import Perguntas

class Pesquisas(Document):
    title = StringField(required=True)
    obs = StringField(required=True)
