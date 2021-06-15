from airflow import DAG
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
