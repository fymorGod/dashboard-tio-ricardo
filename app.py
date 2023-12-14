import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from unidecode import unidecode

# Seus dados...
respostas = [
    'RESPEITA AS DIFERENÇAS?',
    'CONSTROI RELAÇÕES?',
    'É TRASNPARENTE?',
    'É COERENTE?',
    'VALORIZA COOPERAÇÃO?',
    'SE ATUALIZ. A NOVOS PROCESSOS?',
    'TEM AMOR POR SERVIR?',
    'ATUA COMO BASE P/ DESEMPENHO?',
    'COMPARTILHA SOLUÇÕES?',
    'CONTRIBUI P/ O BEM ESTAR DAS PESSOAS?',
    'DESENV. E IMPLENTA AÇÕES DE MELHORIA?',
    'INCENTIVA A AUTONOMIA?',
    'TEM O SENTIMENTO DE DONO?'
]
sempre = [12, 13, 14, 16, 14, 11, 13, 13, 11, 12, 12, 13, 13]
frequente = [1, 4, 3, 1, 2, 7, 5, 5, 6, 6, 6, 4, 3]
as_vezes = [5, 1, 1, 1, 2, 0, 0, 0, 1, 0, 0, 1, 2]
nunca = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.DataFrame({
    'Respostas': respostas,
    'Sempre': sempre,
    'Frequente': frequente,
    'Às Vezes': as_vezes,
    'Nunca': nunca
})
df.set_index('Respostas', inplace=True)

# Configurando o tema do Seaborn
sns.set_theme()

# Streamlit App
st.title('Dashboard de Respostas - IRAMAR')

# Estilizando a tabela
st.markdown(
    """
    <style>
        table {
            font-size: 14px;
            text-align: left;
        }
        th, td {
            padding: 8px;
        }
        th {
            background-color: #323232;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
    </style>
    """,
    unsafe_allow_html=True
)

opcao = st.sidebar.radio("Selecione o tipo de gráfico", ["Tabela", "Gráfico de Barras"])

if opcao == "Tabela": 
  st.table(df)
elif opcao == "Gráfico de Barras":
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)

selected_responses = st.sidebar.multiselect('Selecione as Respostas:', respostas)

for resposta in selected_responses:
    resposta_sem_acentos = unidecode(resposta.lower())
    if resposta_sem_acentos in df.index.map(lambda x: unidecode(x.lower())):
        st.write(f'## Gráfico de Barras para: {resposta}')
        fig, ax = plt.subplots(figsize=(8, 6))
        df.loc[df.index.map(lambda x: unidecode(x.lower())) == resposta_sem_acentos].plot(
            kind='bar', ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
        )
        plt.xlabel('Categorias')
        plt.ylabel('Frequência')
        plt.title(resposta)
        plt.xticks(rotation=0)  # Rótulos na horizontal
        st.pyplot(fig)
    else:
        st.warning(f'A resposta "{resposta}" não está presente no DataFrame.')
