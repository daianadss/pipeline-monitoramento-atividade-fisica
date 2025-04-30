# Pipeline de Monitoramento de Atividade Física (Simulado)

Este projeto simula um pipeline de engenharia de dados que coleta, trata, classifica e armazena registros fictícios de atividades físicas. O objetivo é demonstrar um fluxo completo de **coleta, transformação e carga (ETL)** utilizando ferramentas amplamente usadas na engenharia de dados, de forma simples e compreensível.

---

## Tecnologias utilizadas

- Python
- Flask (para simulação da API)
- Pandas (para transformação e tratamento dos dados)
- SQLite + SQLAlchemy (para carga em banco de dados)
- SQL (para consultas aos dados armazenados)

---

## Estrutura do pipeline

1. **Coleta:** Os dados são simulados por uma API construída com Flask e acessados por um script coletor com requests. A cada chamada, novos dados são gerados e salvos no arquivo `dados_atividade.csv`.

2. **Transformação:** Com Pandas, os dados brutos são carregados, o tipo de dado é ajustado e uma nova coluna é criada (`nivel_por_passos`), classificando o nível da atividade física (Sedentário, Leve, Moderado ou Intenso) com base na quantidade de passos.

3. **Carregamento:** Os dados transformados são carregados em uma base de dados SQLite (`atividade_fisica.db`) usando SQLAlchemy.

4. **Consulta:** Um exemplo de consulta SQL diretamente no banco de dados, mostrando a quantidade de registros de cada nível de atividade.

---

## Exemplo de consulta SQL
```sql
SELECT nivel_por_passos, COUNT(*) as Qtde
FROM atividades
GROUP BY nivel_por_passos;
```

---

## Arquivos do projeto

| Arquivo             | Descrição                                                                 |
| ------------------- | ------------------------------------------------------------------------- |
| `api_simulador.py` | Gera e expõe dados simulados de atividade física via API Flask          |
| `coleta_dados.py`  | Coleta os dados da API e grava em `dados_atividade.csv`                  |
| `tratamento_carregamento.py` | Realiza o tratamento dos dados com Pandas e envia para o banco SQLite |
| `atividade_fisica.db` | Banco de dados SQLite com os dados tratados                            |
| `dados_atividade.csv` | Arquivo CSV com os dados brutos coletados                              |

---

## Sobre os dados simulados

Os dados usados são gerados aleatoriamente, sem base em sensores reais ou padrões fisiológicos.

Por isso, alguns registros apresentam inconsistências — como uma longa distância associada a poucos passos.

Pelo propósito didático do projeto, voltado para o fluxo de engenharia de dados, essas inconsistências foram consideradas aceitáveis.

---

## Como rodar

### Pré-requisitos

Certifique-se de ter o Python instalado e as bibliotecas abaixo:

```bash
pip install flask pandas sqlalchemy
```

### Etapas

 
#### Inicie a API simuladora

Em um terminal, execute:

```
python api_simulador.py
```

Isso iniciará a API em `http://127.0.0.1:5000/atividade`, que irá simular dados de atividade física.

#### Coleta dos dados

Em outro terminal, execute:

```
python coleta_dados.py
```

O script irá coletar os dados gerados pela API e salvar no arquivo `dados_atividade.csv`.

#### Tratamento e carregamento

Após a coleta, execute:

```
python tratamento_carregamento.py
```

Esse script:
- Converte os tipos de dados,

- Adiciona a classificação por nível de atividade,

- E armazena os dados no banco SQLite `atividade_fisica.db`.