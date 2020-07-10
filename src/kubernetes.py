from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.pod import Resources
from airflow.contrib.kubernetes.pod import Port
from datetime import datetime, timedelta 

default_args = {
    'owner': 'massi',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 26),
    'email': ['kerrache.massipssa@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(dag_id='test_kubernetes', default_args = default_args)

port = Port("Http", 8080)

pod_task = KubernetesPodOperator(namespace='dev',
                              image="python:3.6",
                              cmds=["python","-c"],
                              arguments=[f"from time import sleep; sleep(5); print('slept for 5 seconds')"],
                              labels={"foo": "bar"},
                              name=f"sleeper-agent-start",
                              task_id=f"sleeper-agent-start-task",
                              get_logs=True,
                              dag=dag,
                              affinity=solver_affinity,
                              resources=Resources(request_cpu='100m'),
                              in_cluster=True
                            )