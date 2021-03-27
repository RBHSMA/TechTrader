from django  import forms
from .models import Indikator, IndikatorPlotKonfig

class IndikatorModelForm(forms.ModelForm):
    """
        Klasse für das Definieren der Felder des Indikator Formulars.
        Ein IndikatorFormular hat die Felder "name", "beschreibung" und "berechnung_pseudo_code".
        """
    class Meta:
        model   = Indikator
        fields  = ( # Liste aller Felder die von dem Model Indikator verwendet werden
            'name',
            'beschreibung',
            'berechnung_pseudo_code',
            'eigene_skala'
        )        
        widgets =  { # hier werden die Felderarten und css Klassen festgelegt.
            'name'                  : forms.TextInput(attrs = {'class': 'nameFeld'}),
            'beschreibung'          : forms.Textarea(attrs  = {'class': 'textfeld'}),
            'berechnung_pseudo_code': forms.Textarea(attrs  = {'class': 'textfeld'}),
        }
        
class IndikatorPlotKonfigForm(forms.ModelForm):
    """
        Klasse für das Definieren der Felder des Simulation Konfigurations Formulars.
        Ein Konfigurations Formular hat die Felder "isin", "von_datum", "bis_datum", "strategie" und "startkapital".
        """
    class Meta:
        model = IndikatorPlotKonfig
        fields = [ #Liste aller Felder die von dem Model Simulation verwendet werden
            "isin",  
            "von_datum", 
            "bis_datum", 
        ]
        widgets = { # hier werden die Felderarten und css Klassen festgelegt.
            "isin"         : forms.HiddenInput(), # Dieses Feld wird vom System mit der getroffenen Wahl befüllt. Ist aber für Nutzer nicht sichtbar
            "von_datum"    : forms.DateInput(attrs={"type" : "date"}),
            "bis_datum"    : forms.DateInput(attrs={"type" : "date"}),
        }
        labels = { # hier werden die Labels angepasst
            "von_datum": "Start-Datum",
            "bis_datum": "End-Datum"
        }

     
   
