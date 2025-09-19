import streamlit as st

def main():
    st.set_page_config(page_title="Bienvenida", page_icon="👋", layout="centered")
    
    # Estilo personalizado con Markdown y CSS
    st.markdown("""
        <style>
        .welcome-title {
            color: #4CAF50;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 0;
        }
        .welcome-subtitle {
            color: #555;
            font-size: 22px;
            text-align: center;
            margin-top: 5px;
            margin-bottom: 30px;
        }
        .btn-style {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            font-size: 18px;
        }
        .btn-style:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="welcome-title">👋 ¡Bienvenido a Mi Sitio!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="welcome-subtitle">Tu espacio para aprender y explorar con Streamlit</p>', unsafe_allow_html=True)
    
    # Imagen de bienvenida actualizada con use_container_width
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80", use_container_width=True)
    
    st.write("---")
    
    # Texto descriptivo en columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("¿Qué es esto?")
        st.write("""
        Este es un sitio interactivo creado con **Streamlit** para darte la bienvenida.
        Aquí podrás ver cómo construir interfaces web rápidas y atractivas con Python.
        """)
    
    with col2:
        st.header("¿Qué puedes hacer?")
        st.write("""
        - Explorar contenido dinámico  
        - Probar botones y widgets  
        - Ver resultados instantáneos  
        - ¡Y mucho más!  
        """)
    
    st.write("---")

    # Botón de saludo
    if st.button("¡Haz clic para saludarte! 👋"):
        st.balloons()
        st.success("¡Hola! Gracias por visitar este sitio. 😊")

    st.markdown("---")
    st.markdown("Creado por: Esneyder Vásquez y Luis Fernando Zuluaga")

if __name__ == "__main__":
    main()

