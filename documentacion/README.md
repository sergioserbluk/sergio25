# Documentación para la exposición "Conectando al Centro de Estudiantes"

Este documento resume cómo el prototipo desarrollado por el equipo se articula
con los contenidos del cuadernillo **Conectando al Centro de Estudiantes** y
sirve como guía para explicar el proyecto en una feria o defensa académica.

## 1. Síntesis del enfoque pedagógico

- **Participación estudiantil:** la plataforma enfatiza canales de escucha
  activa (preguntas abiertas a la IA) y la producción colaborativa de
  contenidos para la comunidad académica.
- **Seguridad y confianza:** los ejemplos incluyen manejo responsable de
  credenciales y registros de interacción, alineado con la teoría de protección
  de datos personales.
- **Innovación con IA:** se muestra el uso de modelos generativos para apoyar
  la comunicación institucional, respetando criterios éticos señalados en el
  material de referencia.

## 2. Mapeo entre teoría y componentes del proyecto

| Eje teórico del cuadernillo | Implementación en el prototipo |
| --- | --- |
| **Seguridad digital y cuidado de datos**: se plantea almacenar contraseñas de manera segura. | El script `login.py` implementa verificación con hash SHA-256, evitando guardar contraseñas en texto plano y mostrando el ciclo completo de autenticación. |
| **Integración con servicios externos**: se sugiere aprovechar APIs para extender capacidades de los centros de estudiantes. | El módulo `asistentegemini/api_gemini.py` encapsula la conexión con Gemini mediante credenciales en variables de entorno, promoviendo buenas prácticas de despliegue. |
| **Experiencias participativas**: se promueve diseñar actividades para recopilar inquietudes y generar respuestas contextualizadas. | El menú interactivo de `asistentegemini/menu.py` permite consultas abiertas, reescritura colaborativa y ejemplos guiados para dinamizar el stand. |
| **Gestión de evidencia y trazabilidad**: registrar interacciones ayuda a evaluar el impacto del proyecto. | El menú registra cada actividad en archivos JSONL dentro de `archivos/sesiones`, facilitando el análisis posterior. |
| **Comunicación institucional**: adaptar el mensaje al público objetivo. | Las plantillas de estilos narrativos en `asistentegemini/menu.py` muestran cómo ajustar el tono según la audiencia (misterio, crónica formal, etc.). |

## 3. Guía para presentar el recorrido

1. **Inicio seguro:** mostrar el script de login y explicar cómo el hash protege
   las credenciales incluso si la base de datos es comprometida.
2. **Configuración responsable:** enseñar el archivo `.env` (no versionado) y
   señalar la importancia de ocultar la `API_KEY` antes de ejecutar el menú.
3. **Demostración del menú:** ejecutar `python -m asistentegemini.main` y elegir
   cada opción destacando:
   - Preguntas abiertas para conocer necesidades de los estudiantes.
   - Reescritura asistida para redactar comunicados institucionales.
   - Ejemplos prediseñados para debatir estilos de comunicación.
4. **Registro de interacción:** abrir `archivos/sesiones/sesion_YYYYMMDD.jsonl`
   para evidenciar cómo se almacenan los datos con sello de tiempo.

## 4. Buenas prácticas destacadas

- **Hash de contraseñas:** SHA-256 ilustra la diferencia entre almacenar texto
  plano y un digest irreversible; se puede complementar con sal aleatoria para
  despliegues reales.
- **Variables de entorno:** separar claves API del código evita filtraciones en
  repositorios públicos y permite usar distintos entornos (desarrollo, demo,
  producción).
- **Contextualización de prompts:** cada interacción con Gemini agrega un
  contexto sobre el Centro de Estudiantes, asegurando respuestas alineadas a la
  identidad institucional.
- **Trazabilidad:** guardar archivos `.jsonl` simplifica el análisis en cursos
  posteriores (por ejemplo, minería de texto o evaluación de métricas de uso).

## 5. Checklist rápido para la exposición

- [ ] Actualizar el `.env` con una `API_KEY` válida.
- [ ] Preparar ejemplos de preguntas frecuentes de estudiantes.
- [ ] Llevar textos reales del centro para reescribir en vivo.
- [ ] Revisar el directorio `archivos/sesiones` antes y después de la demo.
- [ ] Registrar hallazgos y posibles mejoras para retroalimentar al equipo.

Con esta guía cada estudiante puede vincular la teoría del cuadernillo con la
práctica del prototipo y destacar los aportes tecnológicos del proyecto.
