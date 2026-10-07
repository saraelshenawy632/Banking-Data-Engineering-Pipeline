from datetime import datetime

from airflow import DAG

from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator
)


# ============================================================
# CONFIGURATION
# ============================================================

DATABRICKS_CONN_ID = "databricks_default"

NOTEBOOK_BASE_PATH = (
    "/Workspace/Users/selshenawy69@gmail.com/"
)

ALERT_EMAIL = "selshenawy69@gmail.com"


# ============================================================
# DEFAULT ARGUMENTS
# ============================================================

default_args = {
    "owner": "sara",
    "depends_on_past": False,
    "email": [ALERT_EMAIL],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 0,
}


# ============================================================
# HELPER FUNCTION
# ============================================================

def create_databricks_task(task_id, notebook_name):

    return DatabricksSubmitRunOperator(

        task_id=task_id,

        databricks_conn_id=DATABRICKS_CONN_ID,

        email=[ALERT_EMAIL],

        email_on_failure=True,

        email_on_retry=False,

        retries=0,

        json={
            "tasks": [
                {
                    "task_key": f"{task_id}_task",

                    "notebook_task": {
                        "notebook_path": (
                            NOTEBOOK_BASE_PATH
                            + notebook_name
                        )
                    }
                }
            ]
        }
    )


# ============================================================
# DAG
# ============================================================

with DAG(

    dag_id="banking_data_pipeline",

    start_date=datetime(
        2026,
        10,
        1
    ),

    schedule=None,

    catchup=False,

    default_args=default_args,

    tags=[
        "banking",
        "data-engineering",
        "databricks",
        "pyspark"
    ],

) as dag:


    # ========================================================
    # BRONZE
    # ========================================================

    bronze = create_databricks_task(
        task_id="bronze",
        notebook_name="01_bronze"
    )


    # ========================================================
    # SILVER
    # ========================================================

    silver = create_databricks_task(
        task_id="silver",
        notebook_name="02_silver"
    )


    # ========================================================
    # GOLD ACCOUNT
    # ========================================================

    gold_account = create_databricks_task(
        task_id="gold_account",
        notebook_name="03_gold_account"
    )


    # ========================================================
    # GOLD DAILY
    # ========================================================

    gold_daily = create_databricks_task(
        task_id="gold_daily",
        notebook_name="04_gold_daily"
    )


    # ========================================================
    # GOLD TRANSACTION
    # ========================================================

    gold_transaction = create_databricks_task(
        task_id="gold_transaction",
        notebook_name="05_gold_transaction"
    )


    # ========================================================
    # DATA QUALITY
    # ========================================================

    data_quality = create_databricks_task(
        task_id="data_quality",
        notebook_name="06_data_quality"
    )


    # ========================================================
    # DEPENDENCIES
    # ========================================================

    bronze >> silver

    silver >> [
        gold_account,
        gold_daily,
        gold_transaction
    ]

    [
        gold_account,
        gold_daily,
        gold_transaction
    ] >> data_quality