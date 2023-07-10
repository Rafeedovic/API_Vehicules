from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'rafed',
    'start_date': datetime(2023, 7, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'data_vehicule_v1.5',
    default_args=default_args,
    description='API Transport',
    schedule=timedelta(days=1)
)


# Define tasks
start_task = EmptyOperator(task_id='start_task', dag=dag)

def task1_function():
    # Your task logic goes here
    print("Executing Task 1")

task1 = PythonOperator(
    task_id='task1',
    python_callable=task1_function,
    dag=dag
)

def task2_function():
    # Your task logic goes here
    print("Executing Task 2")

task2 = PythonOperator(
    task_id='task2',
    python_callable=task2_function,
    dag=dag
)

end_task = EmptyOperator(task_id='end_task', dag=dag)

# Define task dependencies
start_task >> task1 >> task2 >> end_task
