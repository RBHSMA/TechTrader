from django.urls import path
from regel.views import (
    RegelHinzufuegenView,
    RegelListeView,
    RegelDetailView,
    RegelBearbeitenView,
    RegelEntfernenView,
)


app_name = 'regel'
urlpatterns = [
    path('', RegelListeView.as_view(), name='regel-liste'),
    path('hinzufuegen/', RegelHinzufuegenView.as_view(), name='regel-hinzufuegen'),
    path('<int:id>/', RegelDetailView.as_view(), name='regel-details'),
    path('<int:id>/bearbeiten/', RegelBearbeitenView.as_view(), name='regel-bearbeiten'),
    path('<int:id>/entfernen/', RegelEntfernenView.as_view(), name='regel-entfernen'),
]
