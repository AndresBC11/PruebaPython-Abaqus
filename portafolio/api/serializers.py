import datetime
from ..models import Portafolio

def validar_fechas(fecha_inicio, fecha_fin):
    """
    Función para validar que las fechas de inicio y fin sean válidas.
    """
    if fecha_inicio is None or fecha_fin is None:
        raise ValueError("Las fechas de inicio y fin no pueden ser nulas.")
    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha de inicio no puede ser mayor que la fecha de fin.")
    try:
        fecha_inicio_valida = datetime.date.fromisoformat(fecha_inicio)
        fecha_fin_valida = datetime.date.fromisoformat(fecha_fin)
    except (ValueError, TypeError):
        raise ValueError("Las fechas deben tener el formato válido AAAA-MM-DD.")


def validar_portafolio(portafolio):
    """
    Función para validar que el portafolio exista en la base de datos.
    """
    if portafolio is None:
        raise ValueError("El portafolio no puede ser nulo.")
    if not Portafolio.objects.filter(nombre=portafolio).exists():
        raise ValueError(f"El portafolio con nombre -{portafolio}- no existe.")