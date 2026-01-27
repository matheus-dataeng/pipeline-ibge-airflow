🚀 Pipeline de Dados IBGE: Localidades Brasileiras com Airflow & Docker

Este projeto demonstra a implementação de um pipeline de dados ETL (Extract, Transform, Load) orquestrado, utilizando Apache Airflow rodando em containers Docker. O objetivo é extrair informações de estados e regiões brasileiras diretamente da API de Localidades do IBGE, processá-las e armazená-las de forma organizada para análise.

🛠️ Tecnologias Utilizadas

•Linguagem: Python 

•Orquestração: Apache Airflow 

•Processamento de Dados: Pandas

•Infraestrutura: Docker & Docker Compose


📋 Arquitetura do Projeto

O pipeline foi desenhado seguindo as melhores práticas de engenharia de dados, separando a lógica de negócio da orquestração:

•Extração: Consumo da API REST do IBGE utilizando a biblioteca requests.

•Transformação: Limpeza e normalização de dados JSON complexos em DataFrames estruturados, separando entidades de UFs e Regiões.

•Carga: Persistência dos dados transformados em arquivos CSV em um volume compartilhado entre o container e a máquina local.

📂 Estrutura de Pastas

.
├── dags/               # Definição da DAG do Airflow
├── pipelines/          # Scripts Python com a lógica de ETL
├── dados/              # Pasta local onde os CSVs são salvos (Volume Docker)
├── docker-compose.yaml # Configuração da infraestrutura Airflow
├── .env.example        # Modelo de variáveis de ambiente
└── requirements.txt    # Dependências do projeto



🚀 Como Executar

Pré-requisitos

•Docker Desktop instalado

•Git

Passo a Passo

1.Clone o repositório:

git clone https://github.com/seu-usuario/ibge-localidades-airflow.git
cd ibge-localidades-airflow


2.Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto com base no .env.example:


PATH_DADOS=/opt/airflow/dados
AIRFLOW_UID=50000


3.Inicie o ambiente Airflow:
No terminal (Windows/CMD ), execute:

set AIRFLOW_UID=50000
docker-compose up -d


4.Acesse a interface do Airflow:
Abra o navegador em http://localhost:8080

•User: airflow | Password: airflow

5.Execute a DAG:

Ative a DAG IBGE_Localidades e dispare o gatilho (Trigger). Os arquivos serão gerados na pasta dados/ do seu computador.

🧠 Desafios Superados

Durante o desenvolvimento, foram aplicadas soluções para:

•Configuração de PYTHONPATH: Garantir que o Airflow localize módulos Python customizados dentro de containers.

•Gerenciamento de Volumes: Sincronização em tempo real entre o sistema de arquivos do container (Linux) e o host (Windows).

•Instalação Dinâmica de Dependências: Uso de _PIP_ADDITIONAL_REQUIREMENTS para manter a imagem leve e funcional.

