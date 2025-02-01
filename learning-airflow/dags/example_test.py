from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    dag_id="decorator_example_dag",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
)
def generate_dag():
    
    @task()
    def get_data():
        return {"number": 42, "message": "Hello from task 1"}
    
    @task()
    def process_data(input_data: dict):
        number = input_data["number"]
        message = input_data["message"]
        return f"Processed message: {message}, number doubled: {number * 2}"
    
    @task()
    def final_step(processed_result: str):
        print(f"Final result: {processed_result}")
    
    # Define the task dependencies
    data = get_data()
    processed = process_data(data)
    final_step(processed)

# Initialize the DAG
example_dag = generate_dag()