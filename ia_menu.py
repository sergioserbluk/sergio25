"""Interactive console menu for AI-assisted text demos.

This script simulates a simple AI-driven assistant for a fair or
demonstration setting. It offers visitors three main activities:

1. Ask a question to the AI.
2. Rewrite or correct a piece of text in a specific style.
3. Explore predefined narrative style examples.

All interactions are logged inside ``archivos/sesiones`` so the team can
later review what happened during each demo. The script is intentionally
modular to make it easy to swap the ``generate_ai_response`` function with
real API calls when the students are ready to connect it to their NLP
backend.
"""

from __future__ import annotations

import json
import textwrap
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional


SESSIONS_DIR = Path("archivos/sesiones")


EXAMPLE_TEXTS: Dict[str, Dict[str, str]] = {
    "Cuento de misterio": {
        "original": (
            "Era una tarde cualquiera cuando escuchamos el crujido en el ático. "
            "Pensamos que era el viento, hasta que la puerta se cerró sola."
        ),
        "descripcion": "Transforma el texto para reforzar el suspenso y la tensión.",
    },
    "Primera persona intimista": {
        "original": (
            "La reunión terminó tarde y el equipo salió sin decir palabra. "
            "Solo quedó el eco de las sillas arrastrándose."
        ),
        "descripcion": "Convierte la escena en un relato introspectivo en primera persona.",
    },
    "Crónica formal": {
        "original": (
            "El barrio celebró la apertura de la nueva biblioteca con música y discursos "
            "de los vecinos más antiguos."
        ),
        "descripcion": "Redacta el texto como una crónica informativa y objetiva.",
    },
}


def ensure_sessions_dir() -> None:
    """Create the sessions directory when it is missing."""

    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)


def log_interaction(interaction_type: str, payload: Dict[str, object]) -> None:
    """Append a JSON entry for each interaction to the daily log file."""

    ensure_sessions_dir()
    timestamp = datetime.now().isoformat(timespec="seconds")
    log_entry = {"timestamp": timestamp, "type": interaction_type, **payload}
    log_file = SESSIONS_DIR / f"sesion_{datetime.now():%Y%m%d}.jsonl"
    with log_file.open("a", encoding="utf-8") as handler:
        handler.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


def generate_ai_response(prompt: str, style: Optional[str] = None) -> str:
    """Simulate an AI answer that references the desired style when provided."""

    wrapped_prompt = textwrap.fill(prompt.strip(), width=72)
    base_response = (
        "Procesé tu solicitud y aquí tienes una propuesta creativa inspirada en "
        "las investigaciones del equipo."
    )
    if style:
        base_response += f" Se aplicó el estilo solicitado: {style.strip()}."

    reformulation = (
        "\n\nResumen del prompt original:\n"
        f"{wrapped_prompt}\n\n"
        "Respuesta simulada:\n"
        "- Idea principal destacada.\n"
        "- Ejemplo narrativo adaptado.\n"
        "- Sugerencia adicional para continuar la conversación."
    )
    return base_response + reformulation


def countdown_timer(seconds: int) -> None:
    """Display a simple countdown so visitors know how much time is left."""

    if seconds <= 0:
        return

    print(f"\nTemporizador iniciado por {seconds} segundos. ¡Aprovechen el turno!")
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"Tiempo restante: {mins:02d}:{secs:02d}", end="\r", flush=True)
        time.sleep(1)
    print("\n¡Tiempo cumplido! Por favor, roten al siguiente equipo.\n")


def ask_for_timer() -> None:
    """Offer to run a countdown timer after completing an interaction."""

    use_timer = input("¿Desean iniciar un temporizador para este grupo? (s/n): ").strip().lower()
    if use_timer == "s":
        while True:
            duration = input("Ingrese la duración en segundos (ej. 180 para 3 minutos): ").strip()
            if duration.isdigit():
                countdown_timer(int(duration))
                break
            print("Valor no válido. Intente nuevamente.")


def prompt_multiline_text() -> str:
    """Allow the user to type multiple lines until an empty line is provided."""

    print("Ingrese el texto. Presione Enter en una línea vacía para finalizar:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines).strip()


def handle_ai_questions() -> None:
    """Menu option to ask the AI a free-form question."""

    print("\n=== Consultas a la IA ===")
    while True:
        question = input("Escriba su pregunta (o deje vacío para volver): ").strip()
        if not question:
            print("Regresando al menú principal...\n")
            break

        print("Procesando…\n")
        answer = generate_ai_response(question)
        print(answer)

        log_interaction(
            "pregunta_ia",
            {
                "prompt": question,
                "response": answer,
            },
        )

        again = input("¿Desea realizar otra pregunta? (s/n): ").strip().lower()
        if again != "s":
            print("Regresando al menú principal...\n")
            break

    ask_for_timer()


def handle_text_rewrite() -> None:
    """Menu option to rewrite or correct user-provided text."""

    print("\n=== Reescritura / Corrección de texto ===")

    source_choice = input(
        "¿Cómo desea ingresar el texto?\n"
        "1) Pegar texto directamente\n"
        "2) Cargar archivo .txt\n"
        "Seleccione una opción: "
    ).strip()

    if source_choice == "1":
        original_text = prompt_multiline_text()
    elif source_choice == "2":
        file_path = input("Ingrese la ruta del archivo .txt: ").strip()
        try:
            original_text = Path(file_path).read_text(encoding="utf-8")
            print("Texto recibido correctamente.\n")
        except OSError as error:
            print(f"No se pudo leer el archivo: {error}. Regresando al menú.\n")
            return
    else:
        print("Opción no válida. Regresando al menú.\n")
        return

    if not original_text:
        print("No se recibió texto. Regresando al menú.\n")
        return

    style = input(
        "Indique el estilo deseado (ej. 'cuento de misterio', 'primera persona'): "
    ).strip()

    print("Procesando…\n")
    response = generate_ai_response(original_text, style)
    print(response)

    log_interaction(
        "reescritura",
        {
            "input_method": "archivo" if source_choice == "2" else "texto",
            "style": style,
            "prompt": original_text,
            "response": response,
        },
    )

    save_choice = input("¿Desea guardar la reescritura en un archivo? (s/n): ").strip().lower()
    if save_choice == "s":
        ensure_sessions_dir()
        filename = input(
            "Ingrese el nombre del archivo (sin extensión, se guardará como .txt): "
        ).strip() or "reescritura"
        output_path = SESSIONS_DIR / f"{filename}.txt"
        output_path.write_text(response, encoding="utf-8")
        print(f"Reescritura guardada en: {output_path}\n")

    repeat = input("¿Desea probar con otro estilo? (s/n): ").strip().lower()
    if repeat == "s":
        handle_text_rewrite()
    else:
        print("Regresando al menú principal...\n")
        ask_for_timer()


def handle_predefined_examples() -> None:
    """Menu option that showcases preloaded narrative transformations."""

    print("\n=== Ejemplos prediseñados ===")
    styles = list(EXAMPLE_TEXTS.keys())
    for idx, style in enumerate(styles, start=1):
        print(f"{idx}) {style} - {EXAMPLE_TEXTS[style]['descripcion']}")

    selection = input("Seleccione un estilo (o deje vacío para volver): ").strip()
    if not selection:
        print("Regresando al menú principal...\n")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(styles)):
        print("Selección no válida. Regresando al menú.\n")
        return

    style_key = styles[int(selection) - 1]
    example = EXAMPLE_TEXTS[style_key]
    print("\nTexto original:\n")
    print(textwrap.fill(example["original"], width=72))
    print("\nProcesando…\n")
    response = generate_ai_response(example["original"], style_key)
    print(response)

    log_interaction(
        "ejemplo",
        {
            "style": style_key,
            "prompt": example["original"],
            "response": response,
        },
    )

    ask_for_timer()


def main() -> None:
    """Display the main menu and route user selections."""

    ensure_sessions_dir()
    print("Bienvenidos al demo de IA para la feria tecnológica.\n")

    options = {
        "1": handle_ai_questions,
        "2": handle_text_rewrite,
        "3": handle_predefined_examples,
    }

    while True:
        print(
            "Menú principal\n"
            "1) Hacerle una pregunta a la IA\n"
            "2) Reescribir o corregir un texto\n"
            "3) Ver ejemplos prediseñados (diferentes estilos narrativos)\n"
            "4) Salir"
        )
        choice = input("Seleccione una opción: ").strip()

        if choice == "4":
            print("¡Gracias por participar! Hasta la próxima.\n")
            break

        handler = options.get(choice)
        if handler is None:
            print("Opción no válida. Intente nuevamente.\n")
            continue

        handler()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSesión finalizada por el usuario. ¡Hasta luego!\n")
