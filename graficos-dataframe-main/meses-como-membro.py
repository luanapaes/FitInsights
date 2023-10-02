#gráfico de areas
#meses como membro 2 - index 292 : durante 2 meses 292 alunos estavam em determinada categoria, por exemplo

import pandas as pd
import plotly.express as px

# Carrega o dataframe
df = pd.read_csv('data.csv')

# Converte o DataFrame em um dicionário
data_dict = df.to_dict(orient='list')

# Acessa cada coluna do dicionário e atribua-a a uma variável
months_as_member = data_dict['months_as_member']
weight = data_dict['weight']
days_before = data_dict['days_before']
day_of_week = data_dict['day_of_week']
time = data_dict['time']
category = data_dict['category']
attended = data_dict['attended']

import pandas as pd
import plotly.express as px


# Cria o gráfico de área
fig = px.area(df, x='months_as_member', facet_col='category', 
              labels={'months_as_member': 'Meses como Membro', 'category': 'Categoria'},
              title='Gráfico de Área: Distribuição de Categorias em Relação aos Meses como Membro')

# Exibe o gráfico
fig.show()
