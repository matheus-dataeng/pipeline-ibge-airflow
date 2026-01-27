import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
def extract_ibge():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    response = requests.get(url).json()
    return pd.json_normalize(response)

def transform_ibge(df):
    df_regioes = df[['regiao.id','regiao.sigla', 'regiao.nome']].drop_duplicates()
    df_regioes.rename(columns={'regiao.id': 'Regiao_id', 
                               'regiao.sigla': 'Regiao_sigla', 
                               'regiao.nome': 'Regiao_nome'}, inplace=True)

    df_ufs = df[['id', 'sigla', 'nome', 'regiao.id', 'regiao.sigla']].drop_duplicates()
    df_ufs.rename(columns={'id': 'Uf_id', 
                           'sigla': 'Sigla', 
                           'nome': 'Nome', 
                           'regiao.id': 'Regiao_id', 
                           'regiao.sigla': 'Regiao_sigla'}, inplace=True)
    
    return df_ufs, df_regioes

def load_ibge(df_ufs, df_regioes):
    caminho_pasta = os.getenv("PATH_DADOS")
    os.makedirs(caminho_pasta, exist_ok=True)
    
    df_ufs.to_csv(os.path.join(caminho_pasta, "Ufs.csv"), index=False)
    df_regioes.to_csv(os.path.join(caminho_pasta, "Regioes.csv"), index=False)

def pipeline():
    dados_brutos = extract_ibge()
    df_ufs, df_regioes = transform_ibge(dados_brutos)
    load_ibge(df_ufs, df_regioes)