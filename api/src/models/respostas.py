from mongoengine import (
    Document,
    ListField,
    ReferenceField,
    StringField
)  
from models.perguntas import Perguntas

class Resposatas(Document) :
    pergunta = ReferenceField(Perguntas)
    resposta = StringField(required=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
