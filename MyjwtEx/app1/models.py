from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class ProfModel(models.Model):
    UserProf=get_user_model()
    user=models.OneToOneField(UserProf,on_delete=models.CASCADE)
    mob=models.BigIntegerField()
    add=models.CharField(max_length=100)


