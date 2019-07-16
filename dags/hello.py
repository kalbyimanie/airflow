from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

dag_id = "hello"
DAG_NAME = "hello.py"

with DAG(dag_id=dag_id, start_date=datetime(2019, 07, 17),
         schedule_interval=None) as dag:

    def say_hello():
        print("Hello World!!")

    PythonOperator(task_id="hello", python_callable=say_hello)
