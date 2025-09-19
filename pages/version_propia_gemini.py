import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(page_title="Chat Avanzado con Gemini", layout="centered")
st.title("💬 Chat Avanzado con Gemini")
st.markdown("Selecciona una función y genera respuestas o correos con Gemini.")

# Inicializar estado para el historial del chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Inicializar función seleccionada
if "funcion" not in st.session_state:
    st.session_state.funcion = "chat"  # opciones: chat, correo

# Inicializar tema seleccionado
if "tema" not in st.session_state:
    st.session_state.tema = "General"

# Instanciar cliente una sola vez usando el nuevo decorador
@st.cache_resource
def get_client():
    return genai.Client(api_key="AIzaSyD2UbfVSwJMBtvNcgjUdRvjjKJUL-6O-XU")

client = get_client()

# Funciones para llamar a Gemini según tipo
def generar_respuesta_texto(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def generar_correo(asunto, detalles):
    prompt = f"Genera un correo formal con el asunto: '{asunto}' y el siguiente contenido:\n{detalles}\n"
    return generar_respuesta_texto(prompt)

# Función para agregar mensaje al historial
def agregar_mensaje(usuario, texto):
    st.session_state.chat_history.append({"usuario": usuario, "texto": texto})

# Barra lateral para selección de función y tema
with st.sidebar:
    st.header("Configuración")
    funcion = st.radio("Selecciona función", options=["chat", "correo"], index=["chat", "correo"].index(st.session_state.funcion))
    st.session_state.funcion = funcion

    tema = st.selectbox("Selecciona un tema", options=["General", "Tecnología", "Educación", "Negocios", "Entretenimiento", "Otro"])
    st.session_state.tema = tema

    if tema == "Otro":
        tema_personalizado = st.text_input("Escribe un tema personalizado:")
        if tema_personalizado:
            st.session_state.tema = tema_personalizado

    if st.button("Limpiar chat"):
        st.session_state.chat_history = []
        st.rerun()

st.markdown(f"### Función actual: **{st.session_state.funcion.capitalize()}**")
st.markdown(f"**Tema seleccionado:** {st.session_state.tema}")

# Inputs y lógica por función
if st.session_state.funcion == "chat":
    prompt = st.text_input("Escribe tu mensaje:", placeholder=f"Pregunta o comentario sobre {st.session_state.tema}")
    enviar = st.button("Enviar")
    if enviar and prompt:
        agregar_mensaje("Tú", prompt)
        with st.spinner("Generando respuesta..."):
            respuesta = generar_respuesta_texto(f"Tema: {st.session_state.tema}\n{prompt}")
        agregar_mensaje("Gemini", respuesta)
        st.rerun()

elif st.session_state.funcion == "correo":
    asunto = st.text_input("Asunto del correo:", placeholder="Ej. Solicitud de reunión")
    detalles = st.text_area("Detalles del correo:", placeholder="Escribe aquí los puntos que quieres incluir en el correo")
    generar_correo_btn = st.button("Generar correo")
    if generar_correo_btn and asunto and detalles:
        agregar_mensaje("Tú", f"Generar correo con asunto '{asunto}' y detalles:\n{detalles}")
        with st.spinner("Generando correo..."):
            correo = generar_correo(asunto, detalles)
        agregar_mensaje("Gemini", correo)
        st.rerun()

# Mostrar historial
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### Historial de Conversación:")
    for msg in st.session_state.chat_history:
        if msg["usuario"] == "Tú":
            st.markdown(f"**Tú:** {msg['texto']}")
        else:
            st.markdown(f"**Gemini:** {msg['texto']}")
else:
    st.info("No hay mensajes en el historial.")





