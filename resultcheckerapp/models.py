from django.db import models

class ResultModel(models.Model):
    studentname=models.CharField(max_length=300,null=True)
    email=models.CharField(max_length=300,null=True)
    studentID=models.CharField(max_length=10,null=True)
    math=models.CharField(max_length=10,null=True)
    english=models.CharField(max_length=10,null=True)
    science=models.CharField(max_length=10,null=True)
    image=models.FileField(null=True)
    
    
    def __str__(self):
        return self.email
