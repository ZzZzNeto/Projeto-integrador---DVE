from django.db import models
from simple_history.models import HistoricalRecords

class BaseModel(models.Model):
    history = HistoricalRecords()
    
    class Meta:
        abstract = True

