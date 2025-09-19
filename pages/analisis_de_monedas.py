import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(page_title="Preguntas sobre Análisis de Mercados", layout="centered")
st.title("📈 Pregunta sobre Análisis de Mercados de Monedas")

st.markdown("""
Esta herramienta está diseñada para responder únicamente preguntas relacionadas con **el análisis de mercados de monedas**, incluyendo:
- Criptomonedas (BTC, ETH, etc.)
- Divisas tradicionales (USD, EUR, JPY)
- Indicadores financieros
- Estrategias de inversión

❗ Si haces una pregunta que **no esté relacionada**, la IA te avisará educadamente.

---
""")

# Campo de texto
pregunta = st.text_area("✍️ Escribe tu pregunta:", placeholder="Ej. ¿Cuál es el mejor indicador para analizar criptomonedas?", height=100)

# Botón de envío
if st.button("🚀 Preguntar"):
    if not pregunta.strip():
        st.warning("Por favor escribe una pregunta.")
    else:
        with st.spinner("Pensando..."):

            # Instrucción de sistema
            system_prompt = (
                "Actúa como un experto en análisis de mercados de monedas (forex y criptomonedas). "
                "Solo responde preguntas relacionadas con ese tema. "
                "Si el usuario hace una pregunta fuera de tema (por ejemplo, sobre deportes, salud, astrología, etc.), "
                "respóndele con respeto que este asistente solo está diseñado para temas de análisis de mercados de monedas."
            )

            try:
                client = genai.Client(api_key="AIzaSyDt4XlHkK0k0_m_6wlGu2MDWc1Jo5unSMc")
                full_prompt = f"{system_prompt}\n\nPregunta del usuario: {pregunta}"

                response = client.models.generate_content(
                    model="gemini-1.5-flash",  # <- aquí el modelo corregido
                    contents=full_prompt
                )

                st.markdown("### 🤖 Respuesta de la IA:")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"❌ Error al generar respuesta: {e}")