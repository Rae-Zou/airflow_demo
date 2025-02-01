import os
import sys
import pytest
from pathlib import Path
from airflow.models import DagBag
from airflow.utils.dag_cycle_tester import check_cycle

@pytest.fixture(scope="session")
def dagbag():
    """Create and return a DagBag instance."""
    current_dir = Path(__file__).parent
    dag_path = current_dir.parent.parent / 'dags'
    sys.path.append(str(dag_path))
    return DagBag(dag_folder=str(dag_path), include_examples=False, read_dags_from_db=False)

def test_dag_structure(dagbag):
    dag_id = 'simple_classic_dag'  
    dag = dagbag.get_dag(dag_id)
    assert dag is not None, f"DAG {dag_id} not found"
    assert len(dag.tasks) > 0, f"DAG {dag_id} has no tasks"
