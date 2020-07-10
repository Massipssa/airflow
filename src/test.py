from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.kubernetes.pod import Resources
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 4, 10, 23),  # May need to change for moving forward
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

SLEEP_DURATION = 300

solver_affinity = {'nodeAffinity': {
                'requiredDuringSchedulingIgnoredDuringExecution': {
                    'nodeSelectorTerms': [{
                        'matchExpressions': [{
                            'key': 'cloud.google.com/gke-nodepool',
                            'operator': 'In',
                            'values': [
                                'solver-eightcore'
                            ]
                        }]
                    }]
                }
            }}

dag = DAG(
    'wide_sleep_patterns_test_100_300', default_args=default_args, schedule_interval=timedelta(minutes=60), max_active_runs=1, concurrency=100)

start = KubernetesPodOperator(namespace='dev',
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
end = KubernetesPodOperator(namespace='dev',
                            image="python:3.6",
                            cmds=["python","-c"],
                            arguments=[f"from time import sleep; sleep(5); print('slept for 5 seconds')"],
                            labels={"foo": "bar"},
                            name=f"sleeper-agent-end",
                            task_id=f"sleeper-agent-end-task",
                            get_logs=True,
                            dag=dag,
                            affinity=solver_affinity,
                            resources=Resources(request_cpu='100m'),
                            in_cluster=True
                            )

for i in range(300):

    sleeper_agent = KubernetesPodOperator(namespace='dev',
                                          image="python:3.6",
                                          cmds=["python","-c"],
                                          arguments=[f"from time import sleep; sleep({SLEEP_DURATION}); print('slept for {SLEEP_DURATION} seconds')"],
                                          labels={"foo": "bar"},
                                          name=f"sleeper-agent-{i}",
                                          task_id=f"sleeper-agent-{i}-task",
                                          get_logs=True,
                                          dag=dag,
                                          affinity=solver_affinity,
                                          resources=Resources(request_cpu='100m'),
                                          in_cluster=True
                                          )

    start >> sleeper_agent >> end