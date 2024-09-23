import streamlit as st
from datetime import datetime

st.header("st.text.input")
nome = st.text_input("Digite o seu nome: ")

if nome:
    st.write(f"Você digitou o nome: {nome}")
else:
    st.write("Você ainda não digitou")

st.header("st.number_input")
numero = st.number_input("Digite um número ")
st.write(numero)

st.header("st.date_input")
data = st.date_input("Entre com uma data: ", key="input_data")

# Corrigir a formatação da data
data_formatada = data.strftime('%d/%m/%Y')

st.header("st.button")
botao = st.button("Clique aqui para se cadastrar", key="btn_cadastrar")

if botao:
    st.write("O botão foi clicado!")
    st.write(f"Nome: {nome}")
    st.write(f"Data: {data_formatada}")

st.header("st.selectbox")
cor = st.selectbox("Escolha uma opção: ", ["vermelho", "azul", "verde"], key="sb.cor")
st.write(cor)

# Corrigir st.multiselect
cores = st.multiselect("Selecione as cores: ", ["vermelho", "azul", "verde"])
st.write(cores)

# Botão Radio
st.header("st.radio")
opcao = st.radio("Selecione uma opção", ["masculino", "feminino"], index=0)
st.write(opcao)

# Checkbox e Markdown corrigidos
st.header("st.checkbox")
st.markdown("""
# Contrato de Trabalho

Nos termos descritos, se você marcar como aceito, poderá realizar o seu cadastro.
""")
aceite = st.checkbox("Eu aceito os termos")

if aceite:
    nome_aceito = st.text_input("Digite o seu nome: ", key="nome_aceito")  # Adicione um key
    idade = st.number_input("Digite a sua idade: ", key="idade_aceita")  # Adicione um key
    data_contratacao = st.date_input("Data de Contratação", key="data_contratacao")  # Adicione um key

    # Exibir a idade se desejado
    st.write(f"Idade: {idade}")
    st.button("Cadastrar")


