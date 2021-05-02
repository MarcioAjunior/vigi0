from mongoengine import (
    Document,
    StringField,
    EmailField
)

class Users(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
    name = StringField(required=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
