from google import genai
#para ocultar la clave de la api y no quede expuesta en el codigo, se puede usar un archivo .env
import os
from dotenv import load_dotenv
#se carga la clave de la api desde el archivo .env (se debe crear un archivo .env en la carpeta del proyecto y agregar la clave de la api)
load_dotenv()
API_KEY = os.getenv("API_KEY") #se obtiene la clave de la api desde el archivo .env
#se crea el cliente de la api
client = genai.Client(api_key=API_KEY)


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="que es una api",
)

print(response.text)