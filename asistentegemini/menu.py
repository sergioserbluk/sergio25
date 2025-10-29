"""Menú interactivo que consulta a Gemini para la feria tecnológica."""

from __future__ import annotations

import json
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, List, Optional

from api_gemini import obtener_respuesta


SESSIONS_DIR = Path("archivos/sesiones")
DOCUMENTS_DIR = Path(__file__).resolve().parent / "documentos"


@dataclass(frozen=True)
class MenuOption:
    """Representa cada opción del menú con su texto y acción asociada."""

    label: str
    handler: Callable[[], None]


WRITING_STYLES: Dict[str, str] = {
    "Formal": "Un estilo profesional y objetivo, ideal para documentos oficiales",
    "Casual": "Un tono relajado y conversacional, perfecto para comunicación informal",
    "Técnico": "Preciso y detallado, enfocado en aspectos técnicos y específicos",
    "Persuasivo": "Convincente y argumentativo, diseñado para influir en el lector",
    "Narrativo": "Estilo de historia, con desarrollo de eventos y descripción vívida",
    "Poético": "Lenguaje figurativo y expresivo, con énfasis en la belleza del lenguaje",
    "Humorístico": "Tono ligero y divertido, con elementos de comedia",
    "Académico": "Riguroso y analítico, apropiado para contextos educativos",
}

CONTENT_DESTINATIONS: Dict[str, str] = {
    "Correo electrónico": "Para comunicación profesional o personal por email",
    "Redes sociales": "Para publicaciones en plataformas sociales",
    "Foro de discusión": "Para participar en debates y discusiones en línea",
    "Blog": "Para artículos y publicaciones de blog",
    "Ensayo": "Para trabajos académicos o análisis profundos",
    "Mensaje instantáneo": "Para comunicación rápida y directa",
    "Presentación": "Para diapositivas y presentaciones",
    "Documentación": "Para manuales y documentación técnica",
}

EXAMPLE_TEXTS: Dict[str, Dict[str, str]] = {
    "Cuento de misterio": {
        "descripcion": "Refuerza el suspenso y los detalles inquietantes.",
        "prompt": (
            "Actúa como guionista de un corto de suspenso. Reescribe el texto "
            "manteniendo un ritmo acelerado y resaltando sonidos perturbadores."
        ),
        "texto": (
            "Era una tarde cualquiera cuando escuchamos el crujido en el ático. "
            "Pensamos que era el viento, hasta que la puerta se cerró sola."
        ),
    },
    "Primera persona intimista": {
        "descripcion": "Explora emociones y dudas internas del protagonista.",
        "prompt": (
            "Convierte el texto en un relato íntimo en primera persona. Describe "
            "qué siente el narrador y cómo procesa lo ocurrido."
        ),
        "texto": (
            "La reunión terminó tarde y el equipo salió sin decir palabra. Solo "
            "quedó el eco de las sillas arrastrándose."
        ),
    },
    "Crónica formal": {
        "descripcion": "Organiza la información con un tono periodístico.",
        "prompt": (
            "Reescribe el texto como una crónica informativa para un boletín del "
            "centro de estudiantes. Prioriza datos verificables y citas breves."
        ),
        "texto": (
            "El barrio celebró la apertura de la nueva biblioteca con música y "
            "discursos de los vecinos más antiguos."
        ),
    },
}


def ensure_sessions_dir() -> None:
    """Crea el directorio de sesiones si aún no existe."""

    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)


def log_interaction(interaction_type: str, payload: Dict[str, object]) -> None:
    """Guarda cada interacción en un archivo JSONL fechado."""

    ensure_sessions_dir()
    log_entry = {"timestamp": datetime.now().isoformat(timespec="seconds"), "type": interaction_type}
    log_entry.update(payload)

    log_file = SESSIONS_DIR / f"sesion_{datetime.now():%Y%m%d}.jsonl"
    with log_file.open("a", encoding="utf-8") as handler:
        handler.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


def _consulta_gemini(prompt: str) -> str:
    """Normaliza el prompt con un contexto común antes de llamar a Gemini."""

    contexto = (
        "Soy un asistente virtual. Responde siempre en español de manera clara y "
        "precisa."
    )
    prompt_completo = f"{contexto}\n\n{prompt.strip()}"
    return obtener_respuesta(prompt_completo)


def _mostrar_respuesta(titulo: str, contenido: str) -> None:
    """Muestra la salida en pantalla con un título legible."""

    separador = "=" * len(titulo)
    print(f"\n{titulo}\n{separador}")
    
    # Divide el contenido en secciones y párrafos
    secciones = contenido.split("\n\n")
    for seccion in secciones:
        # Procesa cada línea de la sección
        lineas = seccion.split("\n")
        for linea in lineas:
            # Si es un encabezado (en mayúsculas y termina con :), no aplicar wrap
            if linea.isupper() and linea.endswith(":"):
                print(f"\n{linea}")
            # Si es una lista con viñetas, preservar la indentación
            elif linea.lstrip().startswith(("*", "-", "•")):
                indentacion = len(linea) - len(linea.lstrip())
                texto_envuelto = textwrap.fill(linea.lstrip(), width=74, 
                                             initial_indent=" " * indentacion,
                                             subsequent_indent=" " * (indentacion + 2))
                print(texto_envuelto)
            # Para el resto del texto, aplicar wrap normal
            elif linea.strip():
                print(textwrap.fill(linea, width=78))
            else:
                print()
        print()  # Espacio entre secciones
    print()


def handle_ai_questions() -> None:
    """Permite realizar preguntas abiertas a Gemini."""

    print("\n=== Consultas abiertas a Gemini ===")
    while True:
        question = input("Escriba su pregunta (o Enter para volver): ").strip()
        if not question:
            break

        respuesta = _consulta_gemini(question)
        _mostrar_respuesta("Respuesta de Gemini", respuesta)
        log_interaction("pregunta_ia", {"prompt": question, "response": respuesta})

        continuar = input("¿Desea realizar otra pregunta? (s/n): ").strip().lower()
        if continuar != "s":
            break


def _cargar_texto_desde_archivo(ruta: str) -> Optional[str]:
    """Carga texto desde un archivo y captura errores comunes."""

    try:
        return Path(ruta).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"No se pudo leer el archivo: {exc}")
        return None


def handle_text_rewrite() -> None:
    """Solicita a Gemini la reescritura de un texto dado."""

    print("\n=== Reescritura asistida ===")
    source_choice = input(
        "¿Cómo desea ingresar el texto?\n"
        "1) Pegar texto manualmente\n"
        "2) Cargar archivo .txt\n"
        "Seleccione una opción: "
    ).strip()

    if source_choice == "1":
        print("Ingrese el texto y finalice con una línea vacía:")
        buffer = []
        while True:
            line = input()
            if not line:
                break
            buffer.append(line)
        texto_original = "\n".join(buffer).strip()
    elif source_choice == "2":
        documentos: List[Path] = sorted(DOCUMENTS_DIR.glob("*.txt"))
        if not documentos:
            print("No se encontraron archivos .txt en la carpeta de documentos.")
            return

        print("Archivos disponibles:")
        for idx, archivo in enumerate(documentos, start=1):
            print(f"{idx}) {archivo.name}")

        seleccion = input(
            "Seleccione el número del archivo que desea cargar (Enter para cancelar): "
        ).strip()

        if not seleccion:
            print("Operación cancelada.")
            return

        if not seleccion.isdigit():
            print("Selección no válida.")
            return

        indice = int(seleccion)
        if not (1 <= indice <= len(documentos)):
            print("Selección no válida.")
            return

        ruta = documentos[indice - 1]
        texto_original = (_cargar_texto_desde_archivo(str(ruta)) or "").strip()
    else:
        print("Opción no válida.")
        return

    if not texto_original:
        print("No se recibió texto para procesar.")
        return

    # Selección de estilo narrativo
    print("\nEstilos de escritura disponibles:")
    for idx, (estilo, descripcion) in enumerate(WRITING_STYLES.items(), 1):
        print(f"{idx}) {estilo}: {descripcion}")
    
    while True:
        seleccion_estilo = input("\nSeleccione el número del estilo deseado: ").strip()
        if seleccion_estilo.isdigit() and 1 <= int(seleccion_estilo) <= len(WRITING_STYLES):
            estilo = list(WRITING_STYLES.keys())[int(seleccion_estilo) - 1]
            break
        print("Por favor, seleccione un número válido.")

    # Selección de destino
    print("\nDestinos de contenido disponibles:")
    for idx, (destino, descripcion) in enumerate(CONTENT_DESTINATIONS.items(), 1):
        print(f"{idx}) {destino}: {descripcion}")
    
    while True:
        seleccion_destino = input("\nSeleccione el número del destino deseado: ").strip()
        if seleccion_destino.isdigit() and 1 <= int(seleccion_destino) <= len(CONTENT_DESTINATIONS):
            destino = list(CONTENT_DESTINATIONS.keys())[int(seleccion_destino) - 1]
            break
        print("Por favor, seleccione un número válido.")

    instrucciones = (
        f"Realiza dos cosas:\n\n"
        f"1. TEXTO REESCRITO:\n"
        f"Primero, reescribe el siguiente texto en un estilo {estilo.lower()} adaptado para {destino.lower()}. "
        f"El texto debe mantener su mensaje central pero adaptarse al formato y tono apropiados.\n\n"
        f"2. ANÁLISIS DE CAMBIOS:\n"
        f"Después, proporciona un análisis detallado de los cambios realizados y explica por qué son "
        f"apropiados para el destino elegido.\n\n"
        f"Separa claramente las dos secciones con los encabezados 'TEXTO REESCRITO:' y 'ANÁLISIS DE CAMBIOS:'"
    )

    prompt = f"{instrucciones}\n\nTexto original:\n{texto_original}"
    respuesta = _consulta_gemini(prompt)
    _mostrar_respuesta("Reescritura propuesta", respuesta)

    log_interaction(
        "reescritura",
        {
            "style": estilo or "general",
            "prompt": texto_original,
            "response": respuesta,
        },
    )


def handle_predefined_examples() -> None:
    """Recurre a ejemplos curados para mostrar distintos estilos narrativos."""

    print("\n=== Ejemplos prediseñados ===")
    opciones = list(EXAMPLE_TEXTS.keys())
    for idx, nombre in enumerate(opciones, start=1):
        print(f"{idx}) {nombre} - {EXAMPLE_TEXTS[nombre]['descripcion']}")

    seleccion = input("Seleccione un estilo (o Enter para volver): ").strip()
    if not seleccion:
        return

    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(opciones)):
        print("Selección no válida.")
        return

    clave = opciones[int(seleccion) - 1]
    ejemplo = EXAMPLE_TEXTS[clave]
    prompt = (
        f"{ejemplo['prompt']}\n\nTexto de partida:\n{ejemplo['texto']}"
    )
    respuesta = _consulta_gemini(prompt)
    _mostrar_respuesta(f"Transformación: {clave}", respuesta)
    log_interaction(
        "ejemplo",
        {"style": clave, "prompt": ejemplo["texto"], "response": respuesta},
    )


def run_menu() -> None:
    """Punto de entrada del menú interactivo."""

    ensure_sessions_dir()
    print("Bienvenidos al demo de IA asistida por Gemini.\n")

    opciones: Dict[str, MenuOption] = {
        "1": MenuOption("Hacerle una pregunta libre a Gemini", handle_ai_questions),
        "2": MenuOption("Reescribir un texto con apoyo de IA", handle_text_rewrite),
        "3": MenuOption("Explorar ejemplos prediseñados", handle_predefined_examples),
    }

    while True:
        print("Menú principal")
        for key, option in opciones.items():
            print(f"{key}) {option.label}")
        print("4) Salir")

        choice = input("Seleccione una opción: ").strip()
        if choice == "4":
            print("¡Gracias por visitar el stand!\n")
            break

        option = opciones.get(choice)
        if option is None:
            print("Opción no válida. Intente nuevamente.\n")
            continue

        option.handler()


__all__ = [
    "run_menu",
    "handle_ai_questions",
    "handle_text_rewrite",
    "handle_predefined_examples",
]
