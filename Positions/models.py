from django.db import models
from Zones.models import Zone
# Create your models here.

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=10, blank=False, null=False)
    is_available = models.BooleanField(blank=False, default=1)
    x_position = models.FloatField(blank=False, null=False, default=0.0)
    y_position = models.FloatField(blank=False, null=False, default=0.0)
    width_scope = models.FloatField(blank=False, null=False, default=0.0)
    height_scope = models.FloatField(blank=False, null=False, default=0.0)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    timeChange = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position_name

    class Meta:
        ordering = ('position_id',)
