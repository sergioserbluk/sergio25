"""Punto de entrada del asistente Gemini con menú interactivo."""

from __future__ import annotations

try:  # Permite ejecutar ``python asistentegemini/main.py`` y ``python -m``
    from .menu import run_menu
except ImportError:  # pragma: no cover - compatibilidad con ejecución directa
    from menu import run_menu  # type: ignore


def main() -> None:
    """Ejecuta el menú principal del asistente Gemini."""

    run_menu()


if __name__ == "__main__":
    main()
