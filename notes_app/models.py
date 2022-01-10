from django.db import models
from django.db.models.fields import DateTimeField, TextField

class Note(models.Model):
    body = TextField()
    created_at = DateTimeField(auto_now_add=True)    
    updated_at = DateTimeField(auto_now=True)