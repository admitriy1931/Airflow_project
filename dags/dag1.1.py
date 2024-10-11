from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "etl_user",
    "depends_on_past": False,
    "start_date": datetime(2024, 10, 11),
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    'dag1.1',
    default_args=default_args,
    schedule_interval='* * * * *',
    catchup=True,
    max_active_tasks=3,
    max_active_runs=1,
    tags=["Task1", "Task2"]
)

task1 = BashOperator(
    task_id='task1',
    bash_command='python3 /opt/airflow/airflow_project/scripts/dag1.1/task1.py',  # Полный путь
    dag=dag
)

task2 = BashOperator(
    task_id='task2',
    bash_command='python3 /opt/airflow/airflow_project/scripts/dag1.1/task2.py',  # Полный путь
    dag=dag
)

task1 >> task2