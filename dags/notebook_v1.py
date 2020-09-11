# -*- coding: utf-8 -*-

import datetime as dt

from airflow import DAG


args = {
    "owner": "vinayak",
    "start_date": dt.datetime.strptime("2020-09-12T00:00:00", "%Y-%m-%dT%H:%M:%S"),
}

dag = DAG(
    dag_id="notebook_v1",
    default_args=args,
    schedule_interval="*/10 * * * *",
)

notebook_task = PapermillOperator(
    task_id="run_notebook",
    input_nb="/opt/airflow/dags/notebook.ipynb",
    output_nb="/tmp/{{ dag.dag_id }}/{{ run_id }}/notebook.ipynb",
    dag=dag,
)
