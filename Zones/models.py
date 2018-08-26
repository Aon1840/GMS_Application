from django.db import models
from Floors.models import Floor
# Create your models here.

class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_name = models.CharField(max_length=10, blank=False, null=False)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.zone_name

    class Meta:
        ordering = ('-zone_id',)
