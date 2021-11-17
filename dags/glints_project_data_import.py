from airflow import DAG, AirflowException
from datetime import datetime, timedelta
import logging
from airflow.operators.python_operator import PythonOperator
import psycopg2
from contextlib import closing

WORKFLOW_DAG_ID = 'glints_project_data_import'
WORKFLOW_START_DATE = datetime.now()
WORKFLOW_SCHEDULE_INTERVAL = '@once'
WORKFLOW_DEFAULT_ARGS = {
	'owner': 'airflow',
	'start_date': WORKFLOW_START_DATE,
	'retries': 0
}

dag = DAG(
	dag_id=WORKFLOW_DAG_ID,
	schedule_interval=WORKFLOW_SCHEDULE_INTERVAL,
	default_args=WORKFLOW_DEFAULT_ARGS,
	catchup=False
)
            
def populate_data(**context):
    psql_conn1 = "host=glints_project_final_database_source_1 port=5432 dbname=glints_db user=airflow password=airflow"            
    psql_conn2 = "host=glints_project_final_database_target_1 port=5432 dbname=glints_db user=airflow password=airflow"   

    with closing(psycopg2.connect(psql_conn1)) as conn1:
        with closing(conn1.cursor()) as curr1:
            curr1.execute(f"SELECT * FROM sales;")
            rows1 = curr1.fetchall()
        conn1.commit()
        
    #LOGGER = logging.getLogger("airflow.task")
    #LOGGER.info(rows1)
	
    with closing(psycopg2.connect(psql_conn2)) as conn2:
        with closing(conn2.cursor()) as curr2:
            for row in rows1:
                all_data1 = row
                curr2.execute("INSERT INTO sales VALUES(%s, %s, %s)" ,(all_data1[0],all_data1[1],all_data1[2]))
            conn2.commit()
	
t = PythonOperator(
    task_id="glints_project_data_import",
    python_callable=populate_data,
    dag=dag
)
