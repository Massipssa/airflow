from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


# set default args
default_args = {
    'owner': 'massi',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 26),
    'email': ['kerrache.massipssa@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# define a DAG
dag = DAG(dag_id='test_dag', default_args=default_args, schedule_interval="2 * * * *")


# define tasks
task_1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello World from Task 1"',
    dag=dag)

task_2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Hello World from Task 2"',
    dag=dag)

# set task's dependencies
task_1 >> task_2
