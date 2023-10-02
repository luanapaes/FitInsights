#grafico de barras
import pandas as pd

# carregando o dataframe
df = pd.read_csv('data.csv')

# Converta o DataFrame em um dicionário - cada coluna virou um "array"
data_dict = df.to_dict(orient='list')

# Acesse cada coluna do dicionário e atribua-a a uma variável
months_as_member = data_dict['months_as_member']
weight = data_dict['weight']
days_before = data_dict['days_before']
day_of_week = data_dict['day_of_week']
time = data_dict['time']
category = data_dict['category']
attended = data_dict['attended']

import plotly.express as px
import pandas as pd

# cria um DataFrame com as variáveis dias da semana e hora
df = pd.DataFrame({
    'day_of_week': day_of_week,
    'time': time
})

# Cria uma coluna com a contagem de ocorrências para cada combinação de dia da semana e hora
df_grouped = df.groupby(['day_of_week', 'time']).size().reset_index(name='count')

# Cria o gráfico de barras
fig = px.bar(df_grouped, x='day_of_week', y='count', color='time',
             labels={'day_of_week': 'Dia da Semana', 'count': 'Contagem'},
             title='Gráfico de Barras: Contagem por Dia da Semana e Hora')

# Exibe o gráfico
fig.show()
