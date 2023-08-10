import os
from dotenv import load_dotenv

load_dotenv()

FIPE_BASE_URL = os.getenv("FIPE_API_URL")

FIPE_API_MARCAS = os.getenv("FIPE_API_MARCAS")
FIPE_API_ANOS = os.getenv("FIPE_API_ANOS")
FIPE_API_MODELOS = os.getenv("FIPE_API_MODELOS")
FIPE_API_VALOR = os.getenv("FIPE_API_VALOR")

if not any([FIPE_BASE_URL, FIPE_API_MARCAS, FIPE_API_ANOS, FIPE_API_MODELOS, FIPE_API_VALOR]):
    raise Exception("Missing FIPE URLs")
