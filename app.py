import streamlit as st
import pandas as pd

st.title ("Minha Primeira Aplicação")
dados = pd.read_csv("acidentes.csv")

dados
