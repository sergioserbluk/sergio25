"""Wrapper simplificado para consultar la API de Gemini."""

from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterable, Mapping, MutableMapping, Optional

try:  # pragma: no cover - dependencias opcionales
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    def load_dotenv() -> bool:  # type: ignore[override]
        """Implementación mínima cuando python-dotenv no está instalado."""

        return False


try:  # pragma: no cover - dependencias opcionales
    import google.generativeai as genai
except ImportError as exc:  # pragma: no cover
    genai = None  # type: ignore[assignment]
    _IMPORT_ERROR = exc
else:
    _IMPORT_ERROR = None


DEFAULT_MODEL_NAME = "gemini-2.0-flash"


@dataclass(frozen=True)
class GenerationParams:
    """Parámetros con valores por defecto documentados para Gemini."""

    temperature: float = 0.7
    top_p: float = 1.0
    top_k: int = 40
    max_tokens: int = 256


def _configure_model() -> Optional["genai.GenerativeModel"]:
    """Configura el cliente de Gemini respetando la presencia de API_KEY."""

    load_dotenv()
    api_key = os.getenv("API_KEY")
    if genai is None:
        return None

    if not api_key:
        # Sin API_KEY devolvemos ``None`` para informar al usuario después.
        return None

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(DEFAULT_MODEL_NAME)


_MODEL = _configure_model()


def _build_generation_config(
    params: Optional[GenerationParams],
    overrides: Optional[Mapping[str, object]] = None,
) -> MutableMapping[str, object]:
    """Compone el diccionario de configuración para ``generate_content``."""

    params = params or GenerationParams()
    config: MutableMapping[str, object] = {
        "temperature": params.temperature,
        "top_p": params.top_p,
        "top_k": params.top_k,
        "max_output_tokens": params.max_tokens,
    }

    if overrides:
        config.update({k: v for k, v in overrides.items() if v is not None})
    return config


def obtener_respuesta(
    prompt: str,
    *,
    params: Optional[GenerationParams] = None,
    stop_sequences: Optional[Iterable[str]] = None,
    safety_settings: Optional[Iterable[Mapping[str, object]]] = None,
    config_overrides: Optional[Mapping[str, object]] = None,
) -> str:
    """Genera una respuesta desde Gemini con parámetros opcionales.

    Cuando no hay clave de API disponible en el entorno se devuelve un mensaje
    descriptivo en lugar de lanzar una excepción. Esto mantiene funcional la
    demostración en contextos educativos o sin conexión.
    """

    prompt = prompt.strip()
    if not prompt:
        raise ValueError("El prompt no puede estar vacío.")

    if genai is None:
        return (
            "La biblioteca 'google-generativeai' no está instalada. Instálela con "
            "pip para habilitar las respuestas de Gemini."
        )

    if _IMPORT_ERROR is not None:
        return f"Error al importar la biblioteca de Gemini: {_IMPORT_ERROR}"

    if _MODEL is None:
        return (
            "No se encontró la variable de entorno API_KEY. Configure el archivo"
            " .env antes de solicitar respuestas a Gemini."
        )

    try:
        response = _MODEL.generate_content(
            prompt,
            generation_config=_build_generation_config(params, config_overrides),
            safety_settings=safety_settings,
            stop_sequences=stop_sequences,
        )
    except Exception as exc:  # pragma: no cover - dependencias externas
        return f"Error al consultar Gemini: {exc}"

    return response.text or "La API no devolvió texto en la respuesta."

