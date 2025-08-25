# Chatbot Educativo con IA (Flask + OpenAI)

Proyecto integrador: plataforma web que consume una API de IA (OpenAI) para brindar respuestas educativas paso a paso.

## Caracteristicas
- Frontend HTML + Bootstrap + JS
- Backend Flask (Python) con endpoint `/api/chat`
- Integracion con OpenAI (configurable por variable de entorno)
- Validaciones basicas y manejo de errores
- Listo para desplegar en Render, Railway o similares

## Requisitos
- Python 3.10+
- Una clave de API de OpenAI (opcional para modo demo)

## Como ejecutar en local
```bash
# 1) Clonar o descargar este repo
# 2) Crear entorno y activar (opcional)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3) Instalar dependencias
pip install -r requirements.txt

# 4) Configurar variables de entorno
cp .env.example .env
# Edita .env y coloca tu OPENAI_API_KEY

# 5) Ejecutar
python app.py
# Abre http://localhost:8000
```

> Si no configuras `OPENAI_API_KEY`, el backend respondra en **modo demo** con un texto simulado.

## Estructura
```
chatbot-educativo-ia/
├─ app.py
├─ requirements.txt
├─ .env.example
├─ templates/
│  └─ index.html
├─ static/
│  ├─ styles.css
│  └─ script.js
└─ manuals/
   ├─ ManualUsuario.md
   └─ ManualProgramador.md
```

## Despliegue rapido (Render)
1. Sube este proyecto a GitHub.
2. En Render, crea un **New Web Service** desde tu repo.
3. Configura:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Environment: `OPENAI_API_KEY` (agrega tu clave)
4. Deploy.

## Licencia
MIT
