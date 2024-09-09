from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.models import Variable

db_host = Variable.get("DB_HOST")
db_user = Variable.get("DB_USER")
# db_password = Variable.get("DB_PASSWORD")

# from airflow.hooks.base import BaseHook
# connection = BaseHook.get_connection("conn1")
# db_host = connection.host
# db_user = connection.login
# db_password = connection.password


default_args = {
    "owner": "You",
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}
today = datetime.now()

with DAG(
    dag_id="Docker_DAG10",
    description="Trying DinD",
    default_args=default_args,
    start_date=today,
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world, this is the first task!"
    )
    
    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo this is task2"
    )
    
    task3 = DockerOperator(
        task_id='run_docker',  
        image='kiarash8203/dind:latest',  
        api_version='auto',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',  
        network_mode='bridge',
    )
        task4=DockerOperator(
        task_id='database',  
        image='yourimage',  
        api_version='auto',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',  
        network_mode='bridge',
        mounts=[docker.types.Mount(
            source='/home/kiarash/Desktop/dumps',
            target='/app/dumps',
            type='bind',  
            read_only=False 
    )],
        environment={
        'DB_HOST': db_host,
        'DB_USER': db_user,
        'DB_PASSWORD': db_password,
    }

    )
    task1 >> task2 
    task1 >> task3 >> task4 

