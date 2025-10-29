# api_gemini.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Configurar cliente
genai.configure(api_key=API_KEY)

# Crear modelo
model = genai.GenerativeModel("gemini-2.0-flash")

def obtener_respuesta(
    prompt: str,
    temperature: float = 0.7,
    top_p: float = 1.0,
    top_k: int = 40,
    max_tokens: int = 256,
    stop_sequences: list = None,
    safety_settings: list = None,
) -> str:
    """Genera una respuesta desde Gemini con parámetros opcionales."""
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "max_output_tokens": max_tokens,
                "stop_sequences": stop_sequences,
            },
            safety_settings=safety_settings
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

