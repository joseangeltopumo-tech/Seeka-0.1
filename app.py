import os
import gradio as gr
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def responder_chat(mensaje_usuario, historial):
    # Lista de modelos en orden de prioridad
    modelos = ["gemini-2.5-flash", "gemini-1.5-flash"]
    
    for modelo in modelos:
        try:
            response = client.models.generate_content(
                model=modelo,
                contents=mensaje_usuario,
            )
            return response.text
        except Exception as e:
            # Si falla un modelo por saturación, intenta con el siguiente en la lista
            continue
            
    return "En este momento todos los servidores de IA están ocupados. Por favor, intenta de nuevo en unos segundos."

# Configuración de la interfaz
demo = gr.ChatInterface(
    fn=responder_chat,
    title="Seeka 0.1",
    description="Listo para servir señor J.A."
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
    
