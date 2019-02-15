# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from datetime import datetime

from airflow import utils
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


START_DATE = datetime.strptime('2019-02-15T12:50:00', '%Y-%m-%dT%H:%M:%S')
DAG_NAME = 'test_clone_v1'

default_args = {
    'owner': 'airflow',
    'start_date': START_DATE
}
dag = DAG(DAG_NAME, schedule_interval='0 * * * *', default_args=default_args)

run_this_1 = DummyOperator(task_id='run_this_1', dag=dag)
run_this_2 = DummyOperator(task_id='run_this_2', dag=dag)
run_this_3 = DummyOperator(task_id='run_this_3', dag=dag)

run_this_1 >> run_this_2 >> run_this_3
