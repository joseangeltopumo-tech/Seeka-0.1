import os
import gradio as gr
from google import genai

# Sica buscará la llave de forma segura en la nube
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


# Instrucciones del sistema (La esencia de tu Jarvis)
instrucciones_sistema = """
Eres un asistente de Inteligencia Artificial avanzado, leal, eficiente y muy perspicaz, inspirado en Jarvis.
Tu creador y usuario es tu prioridad.
Debes dirigirte a él con respeto, amabilidad y tono colaborador.
Recuerda responder siempre en español, de forma clara, directa y lista para ayudarle en sus proyectos y vida diaria.
"""

def responder_chat(mensaje_usuario, historial):
    # Llamada al modelo con las instrucciones del sistema
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=mensaje_usuario,
        config={
            "system_instruction": instrucciones_sistema
        }
    )
    return response.text

# Crear la interfaz visual de chat tipo Gemini (versión limpia)
demo = gr.ChatInterface(
    fn=responder_chat,
    title="Seeka 0.1",
    description="Listo para servir señor J.A."
)

import os

# Al final de tu código, reemplaza la línea demo.launch() por esto:
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)

    
