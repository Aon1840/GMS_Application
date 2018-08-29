from django.db import models

# Create your models here.
class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return self.building_name

    class Meta:
        ordering = ('building_id',)