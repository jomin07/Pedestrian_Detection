from django.db import models


class registerr(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class imagess(models.Model):
    u_id=models.CharField(max_length=150)
    image=models.FileField(max_length=200)
    result=models.CharField(max_length=150)
