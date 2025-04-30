# %%
import pandas as pd
import sqlite3
import sqlalchemy

# %%
df_atividades = pd.read_csv("dados_atividade.csv", sep=",",)
df_atividades.head(5)

# %%
df_atividades.info()

# %%
df_atividades["data_hora"] = pd.to_datetime(df_atividades["data_hora"])

# %%
def classificar_atividade(linha):
    passos = linha["passos"]
    
    if passos <= 1000:
        nivel = "Sedentário"
    elif 1001 <= passos <= 5000:
        nivel = "Leve"
    elif 5001 <= passos <= 10000:
        nivel = "Moderado"
    else:
        nivel = "Intenso"
    
    return nivel

# %%
df_atividades["nivel_por_passos"] = df_atividades.apply(classificar_atividade, axis=1)
df_atividades.head(5)

# %%

engine = sqlalchemy.create_engine("sqlite:///atividade_fisica.db")

df_atividades.to_sql("atividades", engine, index=False, if_exists="append")

# %%

# Contagem de registros por nível de atividade
query = """
        SELECT nivel_por_passos, COUNT(*) as Qtde
        FROM atividades
        GROUP BY nivel_por_passos
"""
pd.read_sql(query, con=engine)