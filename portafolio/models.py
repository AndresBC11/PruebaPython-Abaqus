import datetime
from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Portafolio(BaseModel):
    nombre = models.CharField(max_length=100)
    activos = models.ManyToManyField(
        'Activos',
        through='Activo_en_portafolio',
        related_name='portafolios_relacionados'
    )
                                          
    def __str__(self):
        return self.nombre

class ValorHistoricoPortafolio(BaseModel):
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE, related_name='valores_historicos')
    fecha = models.DateField()
    valor = models.DecimalField(
        max_digits=100, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    class Meta:
        unique_together = ('portafolio', 'fecha')
        ordering = ['fecha']

    def __str__(self):
        return f"{self.portafolio.nombre} - {self.fecha} - {self.valor}"

class Activo_en_portafolio(BaseModel):
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE, related_name='activos_en_portafolio')
    activo = models.ForeignKey('Activos', on_delete=models.CASCADE, related_name='portafolios')
    fecha = models.DateField(editable=False, null=True, blank=True)
    peso = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
        default=Decimal('0.0000')
    )
    valor = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        default=Decimal('0.00')
    )
    cantidad = models.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    
    class Meta:
        unique_together = ('portafolio', 'activo')

    def __str__(self):
        return f"{self.portafolio.nombre} - {self.activo.nombre}"
    
    def save(self, *args, **kwargs):
        # Si el objeto tiene un activo asignado, extraemos su fecha
        if self.activo and hasattr(self.activo, 'fecha'):
            self.fecha = self.activo.fecha
        
        # Llamamos al método save original de Django para que guarde todo
        super(Activo_en_portafolio, self).save(*args, **kwargs)

class Activos(BaseModel):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(default=datetime.date(1900, 1, 1))
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    def __str__(self):
        return self.nombre
    