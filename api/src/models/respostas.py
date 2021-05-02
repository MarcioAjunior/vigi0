from mongoengine import (
    Document,
    ListField,
    ReferenceField,
    StringField
)  


class Respostas(Document) :
    resposta = StringField(required=True)
