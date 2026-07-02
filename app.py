import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise de anúncios de venda de carros')

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Ver distribuição da quilometragem')  # criar um botão

if hist_button:  # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Ver relação entre preço e quilometragem')

if scatter_button:
    st.write('Criando um gráfico de dispersão: preço x quilometragem')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
