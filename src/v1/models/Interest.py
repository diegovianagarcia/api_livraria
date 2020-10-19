from django.db import models


class Interest(models.Model):
    days = models.IntegerField(null=False)
    fine = models.FloatField(null=False)
    interest = models.FloatField(null=False)

    class Meta:
        ordering = ['days']
