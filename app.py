import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)

SYSTEM_PROMPT = (
    "Eres un tutor educativo claro y paciente. "
    "Explica paso a paso y con ejemplos sencillos. "
    "Si la pregunta no es academica, responde brevemente y redirige al tema de estudio. "
    "Cuando haya formulas, usa notacion de texto simple. "
)

def call_openai(prompt, model="gpt-4o-mini"):
    """
    Llama a la API de OpenAI (Responses API). Requiere la variable de entorno OPENAI_API_KEY.
    Si no hay clave, devuelve una respuesta simulada para pruebas locales.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "⚠️ Modo demo: no hay OPENAI_API_KEY configurada. Respuesta simulada: " + prompt[:180]

    try:
        # Importacion perezosa para evitar error si no esta instalada la libreria en tiempo de empaquetado.
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al llamar a OpenAI: {e}"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(force=True, silent=True) or {}
    user_text = (data.get("message") or "").strip()

    if not user_text:
        return jsonify({"ok": False, "error": "El campo 'message' es obligatorio."}), 400

    # Validacion basica: limitar longitud
    if len(user_text) > 2000:
        return jsonify({"ok": False, "error": "El mensaje es demasiado largo (max 2000 caracteres)."}), 400

    answer = call_openai(user_text)
    return jsonify({"ok": True, "answer": answer})

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)
