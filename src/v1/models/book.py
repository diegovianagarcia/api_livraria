from django.db import models


class Book(models.Model):
    STATUS_LENT = 'lent'
    STATUS_AVAILABLE = 'available'
    STATUS_CHOICE = ((STATUS_LENT, 'lent'),
                     (STATUS_AVAILABLE, 'available'))

    title = models.CharField(max_length=20, null=False)
    status = models.CharField(max_length=10, editable=False, null=False, default=STATUS_AVAILABLE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
