import pandas as pd
import plotly.express as px

# Carregando o dataframe
df = pd.read_csv('data.csv')

# Converte o DataFrame em um dicionário
data_dict = df.to_dict(orient='list')

# Acessa cada coluna do dicionário e atribui a uma variável
months_as_member = data_dict['months_as_member']
weight = data_dict['weight']
days_before = data_dict['days_before']
day_of_week = data_dict['day_of_week']
time = data_dict['time']
category = data_dict['category']
attended = data_dict['attended']

# Cria um DataFrame com contagem de ocorrências por dia da semana e categoria
df_grouped = df.groupby(['day_of_week', 'category']).size().reset_index(name='count')

# Define um mapeamento de cores para cada dia da semana
color_map = {
    'Monday': 'red',
    'Tuesday': 'green',
    'Wednesday': 'blue',
    'Thursday': 'orange',
    'Friday': 'purple',
    'Saturday': 'pink',
    'Sunday': 'brown'
}

# Cria o gráfico de linhas (dispersão) com cores diferentes para cada dia da semana
fig = px.scatter(df_grouped, x='day_of_week', y='category', size='count', color='day_of_week',
                 color_discrete_map=color_map,
                 labels={'day_of_week': 'Dia da Semana', 'category': 'Categoria', 'count': 'Contagem'},
                 title='Gráfico de Dispersão: Correlação entre Dias da Semana e Categorias')

# Exibe o gráfico
fig.show()
