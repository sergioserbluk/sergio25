"""Script de autenticación con hash para el demo del Centro de Estudiantes."""

from __future__ import annotations

import hashlib
from getpass import getpass
from typing import Dict


def hash_password(password: str) -> str:
    """Calcula el hash SHA-256 de la contraseña dada."""

    return hashlib.sha256(password.encode("utf-8")).hexdigest()


REGISTERED_USERS: Dict[str, str] = {
    # Hash de la contraseña "admin123" calculado con ``hash_password``.
    "admin": "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",
}


def authenticate(username: str, password: str) -> bool:
    """Valida usuario y contraseña usando hash en lugar de texto plano."""

    stored_hash = REGISTERED_USERS.get(username)
    if stored_hash is None:
        return False
    return hash_password(password) == stored_hash


def main() -> None:
    """Pide credenciales al usuario hasta que sean válidas."""

    print("Sistema de ingreso del Centro de Estudiantes")
    while True:
        username = input("Ingrese su usuario: ").strip()
        password = getpass("Ingrese su contraseña: ")
        if authenticate(username, password):
            print("\n¡Has podido ingresar! Bienvenido/a.\n")
            break
        print("Usuario o contraseña incorrectos. Intente nuevamente.\n")


if __name__ == "__main__":
    main()