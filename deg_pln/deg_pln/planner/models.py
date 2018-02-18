from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=8)
    pre_req1 = models.CharField(max_length=32)
    pre_req2 = models.CharField(max_length=32)
    pre_req3 = models.CharField(max_length=32)
    taken = models.BooleanField()
    elig = models.BooleanField()
    
    def __str__(self):
        return self.name

    '''def get_taken(self):
        if(taken == True):
            return self.name'''
