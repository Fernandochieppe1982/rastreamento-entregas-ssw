import streamlit as st
import datetime

# Estilo visual da Griffus S/A
st.set_page_config(page_title="Griffus S/A - Rastreamento", page_icon="📦", layout="centered")

# CSS customizado para cores Griffus
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
        }
        h1 {
            color: white;
            background-color: #0057b7;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton>button {
            background-color: #0057b7;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1>Griffus S/A - Rastreamento de Entregas</h1>", unsafe_allow_html=True)

# Campos de entrada
nf = st.text_input("🔢 Número da Nota Fiscal")
cnpj = st.text_input("🏢 CNPJ do Remetente", max_chars=18)

# Simular consulta
if st.button("🔍 Rastrear Entrega"):
    if nf.strip() == "" or cnpj.strip() == "":
        st.warning("Por favor, preencha ambos os campos.")
    else:
        # Simulação de status
        st.success(f"✅ NF {nf} entregue com sucesso em 12/07/2025 às 16h52.")
        st.info("Transportadora: SSW | Local: ES")

# Rodapé
st.markdown("---")
st.markdown("© 2025 - Sistema de rastreamento desenvolvido para Griffus S/A")
