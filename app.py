import streamlit as st
import random

# Configuração da página
st.set_page_config(
    page_title="Gerador Mega-Sena",
    page_icon="🎰",
    layout="centered"
)

# Título
st.title("🎰 Gerador de Números da Mega-Sena")

st.write(
    "Clique no botão abaixo para gerar 6 números aleatórios "
    "entre 1 e 60."
)

# Botão
if st.button("🎲 Gerar números", type="primary", use_container_width=True):

    # Sorteia 6 números diferentes entre 1 e 60
    numeros = sorted(random.sample(range(1, 61), 6))

    st.subheader("🍀 Seus números:")

    # Exibe os números
    colunas = st.columns(6)

    for coluna, numero in zip(colunas, numeros):
        coluna.metric("", f"{numero:02d}")

    st.success("Boa sorte! 🍀")

# Aviso
st.caption(
    "⚠️ Os números são gerados aleatoriamente. "
    "Isso não aumenta as chances de ganhar."
)

