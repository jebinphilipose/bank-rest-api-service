from django.db import models


# Create your models here.
class Bank(models.Model):
    bank_id = models.BigIntegerField(primary_key=True)
    bank_name = models.CharField(max_length=50)

    def __str__(self):
        return self.bank_name


class Branch(models.Model):
    ifsc = models.CharField(max_length=20, primary_key=True)
    bank_id = models.ForeignKey(Bank,
                                on_delete=models.CASCADE,
                                default=None)
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.ifsc

    class Meta:
        verbose_name_plural = "Branches"
