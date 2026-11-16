import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("esus-vepi.LeitoOcupacao_2020.csv", sep=";")
df["mes"] = df["dataNotificacao"].astype(str).str[5:7]

df_filtrado = df[
    (df["estado"].isin(["Minas Gerais"]))
].copy()

df_tabela = df_filtrado[["dataNotificacao", "estado", "ocupacaoConfirmadoUti"]]
st.title("Painel Streamlit do Leito de Ocupacao")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela do Leito de Ocupacao")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráfico":
    st.header("Gráfico do Leito de Ocupacao")

    st.subheader("1. Gráfico de Linha — Leito de Ocupacao")
    df_graficolinha = df_tabela[df_tabela["estado"] == "Minas Gerais"]

    fig_linha_taquaril = px.line(
        df_graficolinha,
        x="estado",
        y="ocupacaoConfirmadoUti",
        markers=True,
        title="ocupação de CTI por COVID-19",
        template="plotly_dark"
    )
    fig_linha_taquaril.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig_linha_taquaril.update_xaxes(type="category")
    fig_linha_taquaril.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_taquaril, use_container_width=True)

st.markdown("---")
st.caption("Fonte dos dados: dados abertos do GOV — https://opendatasus.saude.gov.br/")