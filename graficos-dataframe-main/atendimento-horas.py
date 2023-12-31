#GRÁFICO DE PIZZA
#79% DOS ATENDIMENTOS FORAM FEITOS ENTRE 00H E 12H
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


# Cria o gráfico de pizza
fig = px.pie(df, names='time', values='attended', title='Distribuição de Atendimentos por Hora do Dia')

# Mostra o gráfico
fig.show()
