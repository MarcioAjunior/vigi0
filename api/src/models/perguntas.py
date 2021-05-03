from mongoengine import (
    Document,
    ListField,
    ReferenceField,
    StringField
)   

from models.respostas import Respostas

class Perguntas(Document):
    title = StringField(required=True)
    respostas = ListField(ReferenceField(Respostas))
