from django.db import models


# Create your models here.
class Banci(models.Model):
    nume = models.CharField(max_length=45, null=True, default=None)
    adresa = models.CharField(max_length=45, null=True, default=None)

    def __str__(self):
        return f"{self.nume}"


class Angajati(models.Model):
    banca = models.ForeignKey(Banci, on_delete=models.CASCADE)
    nume = models.CharField(max_length=45, null=True, default=None)
    prenume = models.CharField(max_length=45, null=True, default=None)
    adresa = models.CharField(max_length=45, null=True, default=None)
    functie = models.CharField(max_length=45, null=True, default=None)
    salariu = models.FloatField(null=True, default=None)

    def __str__(self):
        return f"{self.nume} {self.prenume}"


class Sucursale(models.Model):
    banca = models.ForeignKey(Banci, on_delete=models.CASCADE)
    nume = models.CharField(max_length=45, null=True, default=None)
    localitate = models.CharField(max_length=45, null=True, default=None)
    cartier = models.CharField(max_length=45, null=True, default=None)
    datadeschidere = models.DateField(null=True, default=None)

    def __str__(self):
        return f"{self.nume} {self.localitate}"