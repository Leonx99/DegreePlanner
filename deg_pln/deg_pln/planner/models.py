import uuid
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32, blank = True, default='')
    code = models.CharField(max_length=9, blank = True, default='')
    pre_req1 = models.CharField(max_length=9, blank = True, default='')
    pre_req2 = models.CharField(max_length=9, blank = True, default='')
    pre_req3 = models.CharField(max_length=9, blank = True, default='')
    co_req = models.CharField(max_length=9, blank = True, default='')
    taken = models.BooleanField(default=False)
    elig = models.BooleanField(default=False)
    score_import = models.IntegerField(default = 0)
    score_like = models.IntegerField(default = 0)

    
    def __str__(self):
        return self.name + ' - ' + self.code

class Classification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32, blank = True, default='')
    code = models.CharField(max_length=9, blank = True, default='')

class Classmapping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    classId = models.CharField(max_length=38, blank = True, null = False)
    Value = models.CharField(max_length=64, blank = True, default='')