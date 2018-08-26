from django.db import models
from Zones.models import Zone
# Create your models here.

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=10, blank=False, null=False)
    is_available = models.BooleanField(blank=False, default=1)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.position_name

    class Meta:
        ordering = ('-position_id',)
