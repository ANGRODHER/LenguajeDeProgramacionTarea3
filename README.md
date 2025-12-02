# Manejador de Tipos de Datos

Este proyecto simula un manejador de tipos de datos que soporta tipos atómicos, structs y unions. Permite definir tipos de datos, calcular su tamaño, alineación y padding bajo diferentes estrategias.

---

## Requisitos

- Python 3.12 o superior
- `pip` para instalar dependencias

---

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone git@github.com\:ANGRODHER/LenguajeDeProgramacionTarea3.git
   cd LenguajeDeProgramacionTarea3

2. **Crear y activar un entorno virtual:**

python3 -m venv venv
source venv/bin/activate  # En Linux
# venv\Scripts\activate     # En Windows

3. **Instalar las dependencias::**

pip install -e .
pip install pytest

**Ejecutar el programa principal**
Para ejecutar el programa principal y comenzar a interactuar con el manejador de tipos de datos, usa el siguiente comando:
python src/main.py

**Ejecutar las pruebas**
Para ejecutar las pruebas unitarias, usa el siguiente comando:
python -m pytest test/

**Estructura del Proyecto**
LenguajeDeProgramacionTarea3/
│
├── setup.py                # Configuración del paquete
├── src/
│   ├── __init__.py         # Inicialización del paquete
│   ├── main.py             # Programa principal
│   └── manejador_tipos.py  # Implementación del manejador de tipos
└── test/
    └── test_manejador.py   # Pruebas unitarias
