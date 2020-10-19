from datetime import date, timedelta
from django.db import models
from django.conf import settings
from .client import Client
from .book import Book
from .Interest import Interest


class Reserve(models.Model):
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=False, on_delete=models.CASCADE)
    reserve_date = models.DateField(auto_now_add=True)

    def days_late(self):
        days_late = (date.today() - (self.reserve_date + timedelta(days=int(settings.DAYS_LENT)))).days
        days_late = 0 if days_late < 0 else days_late
        return days_late

    def calculate(self, strategy):
        # Procura a faixa de juros sendo menor ou igual ao dias de atraso, ordenado descendente
        interest = Interest.objects.filter(days__lte=self.days_late()).order_by('-days').first()
        if interest:
            return strategy(interest)
        return 0

    def calculate_fine(self, interest):
        return (float(settings.VALUE_LENT) * (interest.fine / 100))

    def calculate_interest(self, interest):
        return (float(settings.VALUE_LENT) * (self.days_late() * interest.interest / 100))

    @ property
    def fine(self):
        return self.calculate(self.calculate_fine)

    @ property
    def interest(self):
        return self.calculate(self.calculate_interest)

    class Meta:
        ordering = ['client']
