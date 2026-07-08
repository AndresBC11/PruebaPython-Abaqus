from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from portafolio.services.xlsx_transformer import transform_xlsx
class Command(BaseCommand):
    help = "Procesa un archivo .xlsx"

    def add_arguments(self, parser):
        parser.add_argument(
            "archivo",
            type=str,
            help="Ruta al archivo .xlsx",
        )

    def handle(self, *args, **options):
        ruta_archivo = Path(options["archivo"])

        if not ruta_archivo.exists():
            raise CommandError(f"No existe el archivo: {ruta_archivo}")

        if ruta_archivo.suffix.lower() != ".xlsx":
            raise CommandError("El archivo debe tener extensión .xlsx")

        transform_xlsx(ruta_archivo)

        self.stdout.write(self.style.SUCCESS(f"Archivo recibido de ruta: {ruta_archivo}"))