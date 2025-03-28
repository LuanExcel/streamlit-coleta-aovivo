import streamlit as st
import pandas as pd

st.header("Esse é meu questionário")

with st.form("form"):
    # st.write("Esse é meu questionário")
    # Caixa de seleção
    meu_estado = st.selectbox(
        label="selecione o seu estado", options=["Paraiba", "Pernambuco"]
    )
    minha_area_de_atuacao = st.selectbox(
        label="Selecione sua área de atuação",
        options=["Engenheiro", "Arquiteto", "Analista"],
    )

    # Every form must have a submit button.
    # Quando clicar no botão quero que salve em algum lugar
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("slider", meu_estado, "checkbox", minha_area_de_atuacao)
        meu_dict = {
            "meu_estado": meu_estado,
            "minha_area_de_atuacao": minha_area_de_atuacao,
        }

        df = pd.DataFrame([meu_dict])
        df.to_excel("meu_arquivo.xlsx", index=False)

st.write("Outside the form")
