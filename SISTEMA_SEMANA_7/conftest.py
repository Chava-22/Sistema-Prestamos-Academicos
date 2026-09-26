import sys
from pathlib import Path

# Permite que pytest encuentre los módulos del proyecto (cola_solicitudes,
# catalogo, equipo, etc.) sin importar desde dónde se ejecute el comando.
sys.path.insert(0, str(Path(__file__).resolve().parent))
