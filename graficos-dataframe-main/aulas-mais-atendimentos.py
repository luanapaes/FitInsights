import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

#---------------------------------------------
# Contagem de atendimentos por categoria
contagem_por_categoria = df['category'].value_counts()

# Exibe a contagem por categoria
print(contagem_por_categoria)
print('----------------------------------------')

#----------------------------------------------------
# Agrupa os dados por dia da semana e calcula a contagem de atendimentos em cada grupo
contagem_por_dia = df['day_of_week'].value_counts()

# Encontra os dois menores valores de contagem
menores_contagens = contagem_por_dia.nsmallest(2)

# Exibe os dois dias da semana com menos atendimentos
print("Dois dias da semana com menos atendimentos:")
print(menores_contagens)

#-------------------------------------------------------------

# Agrupa os dados por dia da semana e horário, e calcula a contagem de atendimentos em cada grupo
contagem_por_dia_e_hora = df.groupby(['day_of_week', 'time'])['attended'].count().reset_index()

# Encontra a linha com o maior número de atendimentos
maior_contagem = contagem_por_dia_e_hora['attended'].max()
linha_mais_atendimentos = contagem_por_dia_e_hora[contagem_por_dia_e_hora['attended'] == maior_contagem]

# Extrai o dia da semana e o horário correspondentes
dia_semana_mais_atendidos = linha_mais_atendimentos['day_of_week'].values[0]
horario_mais_atendidos = linha_mais_atendimentos['time'].values[0]

# Exibe o resultado
print(f"No dia da semana '{dia_semana_mais_atendidos}' no horário '{horario_mais_atendidos}' foi quando mais pessoas foram atendidas, com {maior_contagem} atendimentos.")

