import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from unidecode import unidecode

# IRAMAR
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

#VALBER
dados = {
    'RESPOSTAS': [
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
      ],
    'SEMPRE': [19, 19, 22, 23, 19, 20, 22, 21, 21, 21, 18, 19, 19],
    'FREQUENTE': [6, 4, 3, 2, 6, 4, 3, 5, 5, 4, 5, 5, 7],
    'ÁS VEZES': [1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 4, 3, 1],
    'NUNCA': [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df2 = pd.DataFrame(dados)
dados_cicero = {
    'RESPOSTAS': [
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
      ],
    'SEMPRE': [15, 14, 16, 16, 15, 14, 14, 15, 16, 13, 13, 14, 12],
    'FREQUENTE': [1, 2, 0, 0, 1, 2, 2, 1, 0, 3, 3, 2, 4],
    'ÁS VEZES': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'NUNCA': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df_cicero= pd.DataFrame(dados_cicero)

dados_paulo = {
    'RESPOSTAS': [
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
      ],
    'SEMPRE': [13, 13, 16, 15, 13, 12, 14, 11, 12, 13, 16, 12, 11],
    'FREQUENTE': [6, 6, 4, 4, 5, 8, 5, 8, 8, 7, 4, 7, 9],
    'ÁS VEZES': [1, 1, 0, 1, 2, 0, 1, 1, 0, 0, 0, 1, 0],
    'NUNCA': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df_paulo = pd.DataFrame(dados_paulo)

dados_wherys = {
    'RESPOSTAS': [
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
      ],
    'SEMPRE': [6, 6, 11, 9, 9, 9, 12, 10, 8, 8, 9, 9, 8],
    'FREQUENTE': [6, 6, 1, 4, 5, 4, 3, 4, 8, 6, 4, 4, 7],
    'ÁS VEZES': [6, 5, 5, 4, 3, 4, 2, 3, 1, 3, 4, 4, 2],
    'NUNCA': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

df_wherys = pd.DataFrame(dados_wherys)

dados_marliria = {
   'RESPOSTAS': [
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
      ],
    'SEMPRE': [7, 7, 7, 6, 6, 6, 9, 7, 9, 6, 6, 6, 8],
    'FREQUENTE': [3, 2, 5, 5, 4, 5, 4, 6, 4, 5, 5, 4, 5],
    'ÁS VEZES': [3, 4, 1, 2, 3, 2, 0, 0, 0, 2, 2, 3, 0],
    'NUNCA': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df_marliria = pd.DataFrame(dados_marliria)

dados_kessio = {
    'RESPOSTAS': [
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
      ],
    'SEMPRE': [16, 14, 15, 15, 15, 14, 14, 15, 15, 14, 15, 14, 12],
    'FREQUENTE': [1, 3, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 4],
    'ÁS VEZES': [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    'NUNCA': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
}

df_kessio = pd.DataFrame(dados_kessio)

dados_ana = {
    'RESPOSTAS': [
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
      ],
    'SEMPRE': [27, 24, 29, 26, 20, 28, 25, 28, 29, 25, 23, 24, 27],
    'FREQUENTE': [3, 6, 1, 4, 9, 2, 5, 2, 1, 5, 6, 6, 2],
    'ÁS VEZES': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    'NUNCA': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df_ana = pd.DataFrame(dados_ana)

st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.DataFrame({
    'Respostas': respostas,
    'Sempre': sempre,
    'Frequente': frequente,
    'Às Vezes': as_vezes,
    'Nunca': nunca
})
df.set_index('Respostas', inplace=True)
df2.set_index('RESPOSTAS', inplace=True)
df_cicero.set_index('RESPOSTAS', inplace=True)
df_paulo.set_index('RESPOSTAS', inplace=True)
df_wherys.set_index('RESPOSTAS', inplace=True)
df_marliria.set_index('RESPOSTAS', inplace=True)
df_kessio.set_index('RESPOSTAS', inplace=True)
df_ana.set_index('RESPOSTAS', inplace=True)
# Configurando o tema do Seaborn
sns.set_theme()



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

opcao = st.sidebar.radio("Selecione o tipo de gráfico", ["Tabela Iramar", "Tabela Valber", "Tabela Cícero", "Tabela Paulo", "Tabela Wherys", "Tabela Marlíria", "Tabela Késsio", "Tabela Ana"])

selected_responses = st.sidebar.multiselect('Selecione as Respostas:', respostas)
def generatedGraph(frame):
    for resposta in selected_responses:
        resposta_sem_acentos = unidecode(resposta.lower())
        if resposta_sem_acentos in frame.index.map(lambda x: unidecode(x.lower())):
            st.write(f'### Gráfico de Barras para: {resposta.lower()}')
            fig, ax = plt.subplots(figsize=(8, 6))
            frame.loc[frame.index.map(lambda x: unidecode(x.lower())) == resposta_sem_acentos].plot(
                kind='bar', ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
            )
            plt.xlabel('Categorias')
            plt.ylabel('Frequência')
            plt.title(resposta)
            plt.xticks(rotation=0)  # Rótulos na horizontal
            st.pyplot(fig)
        else:
            st.warning(f'A resposta "{resposta}" não está presente no DataFrame.')


if opcao == "Tabela Iramar": 
  st.title('Dashboard de Respostas - IRAMAR')
  st.table(df)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df)
elif opcao == "Tabela Valber":
  st.title('Dashboard de Respostas - Valber')
  st.table(df2)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df2.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df2)
elif opcao == "Tabela Cícero":
  st.title('Dashboard de Respostas - Cícero')
  st.table(df_cicero)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df_cicero.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df_cicero)
elif opcao == "Tabela Paulo":
  st.title('Dashboard de Respostas - Paulo')
  st.table(df_paulo)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df_paulo.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df_paulo)
elif opcao == "Tabela Wherys":
  st.title('Dashboard de Respostas - Wherys')
  st.table(df_wherys)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df_wherys.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df_wherys)
elif opcao == "Tabela Marlíria":
  st.title('Dashboard de Respostas - Marlíria')
  st.table(df_marliria)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df_marliria.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df_marliria)
elif opcao == "Tabela Késsio":
  st.title('Dashboard de Respostas - Késsio')
  st.table(df_kessio)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df_kessio.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df_kessio)
elif opcao == "Tabela Ana":
  st.title('Dashboard de Respostas - Ana')
  st.table(df_ana)
  st.write('### Gráfico de Barras Empilhadas')
  fig, ax = plt.subplots(figsize=(12, 8))
  df_ana.plot(kind='barh', stacked=True, ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
  plt.legend(title='Frequência', bbox_to_anchor=(1.05, 1), loc='upper left')
  st.pyplot(fig)
  generatedGraph(df_ana)
