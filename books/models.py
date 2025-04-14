from django.db import models

class Editore(models.Model):
    ragione_sociale = models.CharField(max_length=255)
    indirizzo = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

class Libro(models.Model):
    titolo = models.CharField(max_length=255)
    anno_edizione = models.IntegerField(blank=True, null=True)
    editore = models.ForeignKey(Editore, on_delete=models.CASCADE)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('titolo', 'editore', 'autore')
