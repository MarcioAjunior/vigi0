from mongoengine import (
    Document,
    ListField,
    ReferenceField,
    StringField
)   

from models.perguntas import Perguntas

class Pesquisa(Document):
    title = StringField(required=True)
    perguntas = ListField(ReferenceField(Perguntas))


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
