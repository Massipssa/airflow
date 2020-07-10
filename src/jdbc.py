from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta


# set default args
default_args = {
    'owner': 'massi',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 26),
    'email': ['kerrache.massipssa@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'sla': timedelta(hours=1)
}

# define a DAG
dag = DAG(dag_id='jdbc_dag', default_args=default_args,  schedule_interval="2 * * * *")

# postgres

sql = "select * from test_table"

task_1 = PostgresOperator(
        task_id='task_1',
        postgres_conn_id='post_gres_conn',
        sql=sql,
        autocommit=True,
        depends_on_past=True,
        sla=timedelta(minutes=5)
    )
