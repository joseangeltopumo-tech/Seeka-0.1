import gradio as gr
from google import genai

# Tu clave de API y cliente
client = genai.Client(api_key="AQ.Ab8RN6IbSPIN1MOOKrfiC6WEH5E-WftObeDVo6_QgL4XyhxjpA")

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
    title="Seeka0.1",
    description="Habla con tu propia Inteligencia Artificial con esencia propia."
)

if __name__ == "__main__":
    demo.launch()
    