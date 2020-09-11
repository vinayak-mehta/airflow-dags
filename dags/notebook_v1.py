# -*- coding: utf-8 -*-

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.papermill_operator import PapermillOperator


args = {
    "owner": "vinayak",
    "start_date": days_ago(1),
}

with DAG(
    dag_id="notebook_v1",
    default_args=default_args,
    schedule_interval="0 0 * * *",
) as dag:
    run_this = PapermillOperator(
        task_id="run_example_notebook",
        input_nb="/opt/airflow/dags/notebook.ipynb",
        output_nb="/tmp/{{ dag.dag_id }}/{{ run_id }}/notebook.ipynb",
        parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"},
    )
