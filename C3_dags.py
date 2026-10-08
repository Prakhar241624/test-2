from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime


@dag(
    dag_id="etl_operator_demos",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
)
def etl_operator_demos():

    @task.python
    def start():
        print("pipeline started")

    download = BashOperator(
        task_id="download",
        bash_command='echo "downloading file"',
    )

    process = BashOperator(
        task_id="process",
        bash_command='echo "processing file"',
    )

    @task.python
    def finish():
        print("pipeline finished")

    start() >> download >> process >> finish()
    



etl_operator_demos()


# If a 5th DAG is added with the SAME dag_id in the same file:
#
# @dag(
#     dag_id="etl_operator_demos",
#     schedule=None,
#     start_date=datetime(2026, 1, 1),
#     catchup=False,
# )
# def new_etl_operator_demos():
#     ...
#
# new_etl_operator_demos()
#
# Airflow 3 treats dag_id as the unique identifier.
# Two DAG definitions with the same dag_id cause a duplicate-DAG/import
# problem rather than creating a separate DAG.
# Existing DAG runs remain associated with the same dag_id.
# New runs use the currently loaded DAG definition.
