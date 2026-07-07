import streamlit as st
import pandas as pd
import os
from langchain_community.document_loaders import PyPDFLoader
import cohere

st.set_page_config(page_title="Tranquipets AI Agent", page_icon="🐾", layout="wide")
st.title("🐾🏨 Tranquipets - AI Agent")

api_key = st.secrets.get("COHERE_API_KEY")
if not api_key:
    st.error("⚠️ Error: No se encontró la clave COHERE_API_KEY en los secretos de Streamlit.")
    st.stop()

co = cohere.Client(api_key)

with st.sidebar:
    st.header("📋 Gestión de Documentos")
    st.subheader("Subir Nuevas Políticas/Servicios")
   
    # Botón interactivo para subir PDFs adicionales en tiempo real
    archivos_nuevos = st.file_uploader(
        "Carga archivos PDF adicionales (Reglamentos, tarifas, etc.):",
        type=["pdf"],
        accept_multiple_files=True
    )
   
    st.write("---")
    st.subheader("📚 Documentos Vigentes")
   
    documentos_activos = ["faq_preguntas-frecuentes.pdf", "politicas_hotel_tranquipets.pdf"]
    if archivos_nuevos:
        for f in archivos_nuevos:
            documentos_activos.append(f"🆕 {f.name} (En memoria)")
           
    for doc in documentos_activos:
        st.markdown(f"- `{doc}`")

def cargar_base_conocimiento(archivos_extra):
    textos_contexto = []
   
    archivo_pdf = "faq_preguntas-frecuentes.pdf", "politicas_hotel_tranquipets.pdf"
    if os.path.exists(archivo_pdf):
        loader = PyPDFLoader(archivo_pdf)
        paginas = loader.load()
        for p in paginas:
            textos_contexto.append(f"[Fuente: PDF Base, Página: {p.metadata.get('page', 0) + 1}] {p.page_content}")

               
     if archivos_extra:
        for pdf_subido in archivos_extra:
            with open(pdf_subido.name, "wb") as f:
                f.write(pdf_subido.getbuffer())
           
            loader = PyPDFLoader(pdf_subido.name)
            paginas = loader.load()
            for p in paginas:
                textos_contexto.append(f"[Fuente: PDF Extra ({pdf_subido.name}), Página: {p.metadata.get('page', 0) + 1}] {p.page_content}")
           
            os.remove(pdf_subido.name)
               
    return "\n\n".join(textos_contexto)

contexto_unificado = cargar_base_conocimiento(archivos_nuevos)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! Bienvenidos a Tranquipets 🐾🏨. Soy tu asistente de Inteligencia Artificial. ¿En qué puedo ayudarte hoy respecto a la estadía de tu mascota, nuestros servicios, tarifas o reservas?"
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if usuario_input := st.chat_input("Escribe tu consulta para Tranquipets aquí..."):

    st.session_state.messages.append({"role": "user", "content": usuario_input})
    with st.chat_message("user"):
        st.write(usuario_input)

    with st.chat_message("assistant"):
        # Construir el prompt del sistema integrado para el modelo command-r
        prompt_sistema = (
            "Eres el AI Agent oficial de Tranquipets, un hotel premium para mascotas.\n"
            "Responde de manera profesional, muy amable, empática con los dueños de las mascotas y concisa, basándote estrictamente en el contexto provisto.\n"
            "Si no sabes algo o no está en el contexto, responde con amabilidad indicando que la información solicitada no se encuentra en los manuales actuales del hotel.\n\n"
            f"Contexto de la empresa:\n{contexto_unificado}"
        )
       
        try:
 (command-r-plus o command-r)
            response = co.chat(
                model="command-r-plus",
                message=usuario_input,
                preamble=prompt_sistema
            )
            respuesta_texto = response.text
        except Exception as e:
            respuesta_texto = f"⚠️ Ocurrió un error al conectar con Cohere: {str(e)}"
           
        st.write(respuesta_texto)

    st.session_state.messages.append({"role": "assistant", "content": respuesta_texto})
