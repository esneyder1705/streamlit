import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(page_title="Explicación AI sobre Pandas", layout="centered")
st.title("🐼 Explicador AI sobre Pandas en Python")

# Lista básica de palabras clave relacionadas con pandas
PALABRAS_CLAVE_PANDAS = [
    "pandas", "dataframe", "series", "loc", "iloc", "read_csv", "head", "tail",
    "merge", "join", "groupby", "sort_values", "fillna", "dropna", "astype",
    "index", "columns", "describe", "plot", "pivot", "reset_index", "set_index",
    "filter", "apply", "lambda", "concat", "duplicated", "drop_duplicates"
]

def es_pregunta_relacionada_con_pandas(pregunta):
    pregunta = pregunta.lower()
    return any(palabra in pregunta for palabra in PALABRAS_CLAVE_PANDAS)

def generar_explicacion(pregunta):
    try:
        client = genai.Client(api_key="AIzaSyDt4XlHkK0k0_m_6wlGu2MDWc1Jo5unSMc")

        # Prompt con contexto claro
        full_prompt = (
            "Actúa como un experto en Python especializado en la librería 'pandas'. "
            "El usuario puede hacer preguntas simples como 'loc' o 'dataframe', y tú debes explicar esos conceptos "
            "de forma clara para alguien que está empezando. No respondas preguntas fuera del tema de pandas. "
            f"Pregunta: {pregunta}\n"
            "Respuesta:"
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt,
        )
        return response.text
    except Exception as e:
        return f"Error al generar explicación: {e}"

# UI
st.write("Escribe una palabra clave o una pregunta sobre la librería **pandas**. Si tu pregunta no está relacionada con pandas, se te informará.")

pregunta = st.text_input("¿Qué quieres saber sobre pandas?", "")

if st.button("📘 Obtener explicación"):
    if pregunta.strip() == "":
        st.warning("Por favor, escribe algo para poder darte una explicación.")
    elif not es_pregunta_relacionada_con_pandas(pregunta):
        st.error("Esta pregunta no está relacionada con la librería pandas. Intenta con algo como 'DataFrame', 'loc', 'read_csv', etc.")
    else:
        with st.spinner("Generando explicación..."):
            explicacion = generar_explicacion(pregunta)
            st.markdown(explicacion)
else:
    st.info("Ejemplos: `loc`, `qué es un DataFrame`, `cómo usar read_csv`, `describe`, etc.")
