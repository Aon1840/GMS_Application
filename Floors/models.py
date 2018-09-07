from django.db import models
from Buildings.models import Building
# Create your models here.

class Floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    floor_name = models.CharField(max_length=10, blank=False, null=False)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.floor_name

    class Meta:
        ordering = ('floor_id',)