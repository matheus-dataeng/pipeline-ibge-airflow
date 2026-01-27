import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
sys.path.append("/opt/airflow")

from pipelines.pipeline_completo import pipeline

with DAG(
    dag_id="IBGE_Localidades",
    description = "Projeto Pratico",
    start_date=pendulum.datetime(2026, 1, 26, tz="America/Sao_Paulo"),
    schedule=None,
    catchup=False,
    tags = ['Projeto', 'IBGE', 'Praticas']
) as dag:
    
    task_run_pipeline = PythonOperator(
        task_id="pipeline",
        python_callable=pipeline,
        )