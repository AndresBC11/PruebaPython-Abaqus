from django.urls import path

from .api.views import PesoActivosEnPortafolioAPIView, ValorHistoricoPortafolioAPIView
from .views import graficadorView

urlpatterns = [
    path('api/peso-activos/', PesoActivosEnPortafolioAPIView.as_view(), name='peso_activos_en_portafolio'),
    path('api/valor-historico/', ValorHistoricoPortafolioAPIView.as_view(), name='valor_historico_portafolio'),
    path('', graficadorView, name='graficador'),
]