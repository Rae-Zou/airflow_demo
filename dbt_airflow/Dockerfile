FROM quay.io/astronomer/astro-runtime:9.1.0-python-3.9-base

COPY astro_provider_snowflake-0.0.0-py3-none-any.whl /tmp/
COPY requirements.txt  /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt 

WORKDIR /usr/local/airflow
RUN python3 -m venv dbt_venv &&\
    . dbt_venv/bin/activate &&\ 
    pip install --no-cache-dir dbt-snowflake &&\ 
    deactivate


