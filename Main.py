import streamlit as st
import pandas as pd
from mysql_connection import *  
from numerize.numerize import numerize
import plotly.express as px
import plotly.subplots as sp
import datetime

# página
st.set_page_config(page_title="Feedback", page_icon="😁", layout="wide")  
st.subheader("🪥 Dashboard Feedback Odonto 🦷")

# CSS Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Pegando dados do MySQL para a tabela "feedback"
result_data = view_all_data()
df_data = pd.DataFrame(result_data, columns=["id", "nome", "nascimento", "sexo", "consultas", "notaAtendimento", "notaTratamento", "dentista", "tratamento"])

df_data['nascimento'] = pd.to_datetime(df_data['nascimento'])

# Calcular idades
data_atual = pd.Timestamp(datetime.date.today())  # Converter a data atual em um objeto datetime
df_data['idade'] = (data_atual - df_data['nascimento']).dt.days // 365

# Combinando "sexo" e "idade"
opcoes_clientes = df_data["sexo"].unique().tolist() + df_data['idade'].unique().tolist()

# opções do menu
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal",
        options=["Dashboard", "Tabela"],
        icons=["house", "book"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# Filtros
st.sidebar.header("Filtros")
tratamento = st.sidebar.multiselect(
    "tratamento",
    options=df_data["tratamento"].unique(),
    default=df_data["tratamento"].unique(),
)
dentista = st.sidebar.multiselect(
    "dentista",
    options=df_data["dentista"].unique(),
    default=df_data["dentista"].unique(),
)

clientes = st.sidebar.multiselect(
    "Clientes",
    options=opcoes_clientes,
    default=opcoes_clientes
)

consultas = st.sidebar.multiselect(
    "consultas",
    options=df_data["consultas"].unique(),
    default=df_data["consultas"].unique(),
)
# Filtrar o DataFrame com base nas seleções de filtro
filtered_df = df_data[
    (df_data['tratamento'].isin(tratamento)) &
    (df_data['dentista'].isin(dentista)) &
    ((df_data['sexo'].isin(clientes)) | (df_data['idade'].isin(clientes)))
]

# Aplicar filtro nas consultas
if consultas:
    filtered_df = filtered_df[filtered_df['consultas'].isin(consultas)]

# Calcular a média das notas de tratamento para cada tratamento no DataFrame df_data
media_notas_por_tratamento = df_data.groupby('tratamento')['notaTratamento'].mean().reset_index()

# Converter a coluna 'tratamento' para o mesmo tipo da coluna 'tratamento'
media_notas_por_tratamento['tratamento'] = media_notas_por_tratamento['tratamento'].astype(str)

# Criar um novo DataFrame que contenha as médias de notas e os nomes dos tratamentos
novo_df = pd.merge(df_data, media_notas_por_tratamento, left_on='tratamento', right_on='tratamento', how='inner')

# Calculando a média da coluna 'notaAtendimento'
media_nota_atendimento = df_data['notaAtendimento'].mean()

# Calculando a média da coluna 'notaTratamento'
media_nota_tratamento = df_data['notaTratamento'].mean()

# Agrupe o DataFrame pelo dentista e calcule a média das notas de atendimento
media_notas_atendimento_por_dentista = df_data.groupby('dentista')['notaAtendimento'].mean().reset_index()

# Calcula o número de tipos únicos de tratamento
total_tratamentos = len(tratamento)

# Calcula o total de consultas
total_de_consultas = df_data['consultas'].sum()

# Agrupe o DataFrame pelo tipo de tratamento e calcule a média das notas de tratamento
media_notas_por_tratamento = df_data.groupby('tratamento')['notaTratamento'].mean()

def metrics():
    from streamlit_extras.metric_cards import style_metric_cards

    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    col1.metric(label="Total de tratamentos", value=total_tratamentos)

    col2.metric(label="Total de consultas", value=total_de_consultas)

    col3.metric(label="Total de clientes", value=df_data.nome.count())

    col4.metric(label="Média Nota de Atendimento", value=media_nota_atendimento, delta="Média de notas de atendimento")

    col5.metric(label="Média Nota de Tratamento", value=media_nota_tratamento, delta="Média de notas de tratamento")

    style_metric_cards(background_color="#fffff", border_left_color="#1f66bd")

# Dashboards
div1, div2 = st.columns(2)

# Gráfico de Pizza
def pie():
    with div1:
        theme_plotly = None  # None or streamlit
        fig = px.pie(filtered_df, values='consultas', names='dentista', title='Consultas por Dentistas')
        fig.update_layout(legend_title="dentista", legend_y=0.9)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

# Gráfico de barras
def barchart():
    with div2:
        fig = px.bar(
            media_notas_atendimento_por_dentista,
            x='dentista',
            y='notaAtendimento',
            title='Média de Notas de Atendimento por Dentista'
        )
        st.plotly_chart(fig, use_container_width=True)

# Função para gerar o gráfico de linhas
def line_chart(data, x, y, color, title):
    fig = px.line(data, x=x, y=y, color=color, title=title)
    st.plotly_chart(fig, use_container_width=True)

def linechart():
    fig = px.line(
        df_data,
        x="consultas",
        y="idade",
        color="sexo",
        title="Avaliando os Clientes"
    )
    st.plotly_chart(fig, use_container_width=True)

# Tabela do MYSQL
def table():
    with st.expander("Tabela"):
        shwdata = st.multiselect('Filter :', filtered_df.columns, default=["id", "nome", "nascimento", "sexo", "consultas","tratamento","notaAtendimento","notaTratamento","dentista"])
        st.dataframe(filtered_df[shwdata], use_container_width=True)

if selected == "Dashboard":
    pie()
    barchart()
    metrics()
    linechart()

if selected == "Tabela":
    metrics()
    table()
    df_data.describe().T