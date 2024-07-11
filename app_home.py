import streamlit as st

st.set_page_config(
    page_title="Portfolio de Raúl PM",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/raulperula/raulperula_portfolio_genai",
        "Report a bug": "https://github.com/raulperula/raulperula_portfolio_genai/issues",
        "About": "## Hecho con :heart: por Raúl Pérula Martínez.",
    },
)

# Define the pages of each project
profile = st.Page(
    "home/0_Sobre_mi.py",
    title="Sobre mi",
    icon=":material/description:",
    default=True,
)
copilot = st.Page(
    "projects/1_Copilot_Summarization.py",
    title="Copilot Generación de Resúmenes",
    icon=":material/precision_manufacturing:",
)
chatbot = st.Page(
    "projects/2_Chatbot_Q&A.py",
    title="Chatbot de Preguntas y Respuestas",
    icon=":material/smart_toy:",
)

# Define the navigation panel
pg = st.navigation(
    {
        "Home": [profile],
        "Proyectos": [copilot, chatbot],
    }
)

# Start the app
pg.run()
