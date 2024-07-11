import os

import streamlit as st
from st_social_media_links import SocialMediaIcons
from streamlit.components.v1 import html
from streamlit_card import card
from streamlit_pills import pills

# Page title
st.markdown("<h1 style='text-align: center;'>Portfolio IA generativa</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Raúl Pérula-Martínez</h2>", unsafe_allow_html=True)
st.markdown(
    '<style>.center {display: block; margin-left: auto; margin-right: auto; width: 10%;}</style><img src="https://pbs.twimg.com/profile_images/1783482553820655616/-1BCUsRh_400x400.jpg" alt="Me"  class="center">',
    unsafe_allow_html=True,
)

# Some animation to get an smile in winter ;)
# TODO: add a condition to show the snow only when in December or January
# st.snow()

# Stack section
st.header("Stack")

col1, col2 = st.columns(2)

with col1:
    options = ["LangChain", "LlamaIndex"]
    pills("Frameworks", options, index=None)

    options = ["Ollama", "Langfuse", "LangSmith"]
    pills("Plataformas", options, index=None)

    options = ["Google Vertex AI", "Azure OpenAI", "Amazon Bedrock"]
    pills("Servicios Cloud u On-Premise", options, index=None)

with col2:
    options = [
        "OpenAI GPT-4",
        "OpenAI Whisper",
        "OpenAI Text Embedding Ada",
        "OpenAI Text Embedding 3",
        "Google Palm 2",
        "Google Gemini",
        "Llama 3",
        "Hugging Face Sentence Transformer",
        "Anthropic Claude 3",
    ]
    pills("Modelos Fundacionales", options, index=None)

    options = ["Faiss", "Pinecone", "Qdrant", "PostgreSQL pgvector", "Amazon OpenSearch service"]
    pills("Bases de datos vectoriales", options, index=None)

    options = ["GitHub Copilot", "OpenAI ChatGPT", "Microsoft Copilot", "Google Gemini"]
    pills("Copilots", options, index=None)

# Social networks section
st.header("¿Conectamos?")

social_media_links = [
    "https://medium.com/@raul.perula",
    "https://github.com/raulperula",
    "https://www.linkedin.com/in/raulperula/",
    "https://x.com/raulperula",
]
colors = ["#000000" for i in range(len(social_media_links))]  # must have the same size as "social_media_links"

social_media_icons = SocialMediaIcons(social_media_links, colors)
social_media_icons.render(sidebar=False, justify_content="space-evenly")
social_media_icons.render(sidebar=True, justify_content="space-evenly")
