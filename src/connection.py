from airflow import settings
from airflow.models import Connection
import logging

log = logging.getLogger(__name__)


def create_conn(conn_id, conn_type, host, port, password, extra=None):

    try:
        connection = Connection(
            conn_id=conn_id,
            conn_type=conn_type,
            host=host,
            port=port,
            password=password,
            extra=extra
        )
        session = settings.Session()
        session.add(connection)
        session.commit()
    except Exception as e:
        log.error("Error during the creation of the connection")
        raise e




