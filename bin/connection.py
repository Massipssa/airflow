from airflow import settings
from airflow.models import Connection


connection = Connection(
    conn_id='test-conne',
    conn_type='',
    host='host',
    password='password',
    port='0000'
)

session = settings.Session()
session.add(connection)
session.commit()
