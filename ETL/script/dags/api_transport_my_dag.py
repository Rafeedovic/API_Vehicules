from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from data_vehicule_v1_5 import main_etl

default_args = {
    'owner': 'rafed',
    'start_date': datetime(2023, 7, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'data_vehicule_v1_5',
    default_args=default_args,
    description='API Transport',
    schedule=timedelta(minutes=1)
)

# Define tasks
start_task = EmptyOperator(task_id='start_task', dag=dag)

def task1_function():
    # Your task logic goes here
    main_etl()

task1 = PythonOperator(
    task_id='task1',
    python_callable=task1_function,
    dag=dag
)

end_task = EmptyOperator(task_id='end_task', dag=dag)

# Define task dependencies
start_task >> task1 >> end_task
