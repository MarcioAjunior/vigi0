from mongoengine import (
    Document,
    ListField,
    ReferenceField,
    StringField
)   

from models.pesquisas import Pesquisa

class Perguntas(Document):
    pesquisa = ReferenceField(Pesquisa)
    title = StringField(required=True)
    respostas = ListField(ReferenceField() default = [])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
