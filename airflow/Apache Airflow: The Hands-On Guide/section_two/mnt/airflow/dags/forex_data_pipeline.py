from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor

from datetime import datetime, timedelta

default_args = {
    "owner":"airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@admin.com",
    "retries":1,
    "retry_delay": timedelta(minutes = 5),
    'depends_on_past': False,
}

with DAG("forex_data_pipeline",
            default_args=default_args,
            start_date= datetime(2021,1,1),
            schedule_interval= "@daily",
            catchup=False) as dag:
    is_forex_rates_availables = HttpSensor(
        task_id = "is_forex_rates_availables",
        http_conn_id = "forex_api",
        endpoint = "marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b",
        response_check = lambda response: "rates" in response.text,
        poke_interval =5,
        timeout = 20
    )