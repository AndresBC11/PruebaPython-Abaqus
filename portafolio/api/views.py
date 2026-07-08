from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Activo_en_portafolio, Portafolio, ValorHistoricoPortafolio
from .serializers import validar_fechas, validar_portafolio
class PesoActivosEnPortafolioAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        portafolio = request.query_params.get('portafolio')

        try:
            validar_fechas(fecha_inicio, fecha_fin)
            validar_portafolio(portafolio)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        activos_portafolio = Activo_en_portafolio.objects.filter(
            fecha__range=[fecha_inicio, fecha_fin],
            portafolio = Portafolio.objects.get(nombre=portafolio)
        ).select_related('activo').order_by('fecha')

        listado_pesos = []
        for activo_portafolio in activos_portafolio:
            listado_pesos += [{
                'activo': activo_portafolio.activo.nombre,
                'peso': float(activo_portafolio.peso),
                'fecha': activo_portafolio.fecha
            }]
        
        return Response(listado_pesos, status=status.HTTP_200_OK)
        
class ValorHistoricoPortafolioAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        portafolio = request.query_params.get('portafolio')

        try:
            validar_fechas(fecha_inicio, fecha_fin)
            validar_portafolio(portafolio)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
        valores_historicos = ValorHistoricoPortafolio.objects.filter(
            fecha__range=[fecha_inicio, fecha_fin],
            portafolio = Portafolio.objects.get(nombre=portafolio)
        ).select_related('portafolio').order_by('fecha')

        listado_valores_historicos = []

        for valor_historico in valores_historicos:
            listado_valores_historicos += [{
                'portafolio': valor_historico.portafolio.nombre,
                'fecha': valor_historico.fecha,
                'valor': float(valor_historico.valor)
            }]
        
        return Response(listado_valores_historicos, status=status.HTTP_200_OK)