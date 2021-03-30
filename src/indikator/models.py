from django.db   import models
from django.urls import reverse

from django.core.validators import MaxLengthValidator # wird benötigt um die maximale Textlänge in einer Textarea zu validieren

class Indikator(models.Model):
  '''
    Klasse des Indikator Models.
    Besteht aus den Felder "name", "beschreibung", "berechnung_pseudo_code" und "eigene_skala"
  '''
  name                      = models.CharField(max_length = 100) # name darf max. 100 Zeichen haben
  beschreibung              = models.TextField(validators=[MaxLengthValidator(1000)]) # beschreibung darf max. 1000 Zeichen haben
  berechnung_pseudo_code    = models.TextField(validators=[MaxLengthValidator(2000)]) # berechnung_pseudo_code darf max. 2000 Zeichen haben
  eigene_skala              = models.BooleanField() 
  
  def get_absolute_url(self):
    """
      Jeder Indikator verweist auf die eigene Detail-Ansicht.
      """
    return reverse("indikator:indikator-details", kwargs = {"id" : self.id})


class IndikatorPlotKonfig(models.Model):
  '''
  Klasse des IndikatorPlotKonfig Models.
  Besteht aus den Felder "isin", "von_datum", "bis_datum" und "indikatorID"
  '''
  von_datum   = models.DateField()
  bis_datum   = models.DateField()
  isin        = models.CharField(max_length = 12, blank = True, null = True)  # Die ausgewählte ISIN
  indikatorId = models.IntegerField(null = True, blank = True)

  def get_absolute_url(self):
    """
    Wird als "Success-url" bei erfolgreichem Ausfüllen des Forms verwendet.
    """
    return reverse("indikator:indikator-graph", kwargs={"id" : self.indikatorId})
  
    