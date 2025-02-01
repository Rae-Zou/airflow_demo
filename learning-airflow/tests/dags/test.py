from pathlib import Path

current_dir = Path(__file__).parent
dag_path = current_dir.parent.parent / 'dags'

print(dag_path)