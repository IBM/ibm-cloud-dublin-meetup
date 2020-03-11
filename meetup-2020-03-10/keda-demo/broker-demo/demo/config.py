# Copyright 2019 IBM Corporation All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

import os

TYPE = os.environ.get('BROKER_TYPE', "demo")

MODE = os.environ.get('BROKER_MODE', "broker")

TASK_CAPACITY = int(os.environ.get('BROKER_TASK_CAPACITY', 5000))
TASK_POLL_RATE = int(os.environ.get('BROKER_TASK_POLL_RATE', 30 * 1000))

DEBUG = os.environ.get('BROKER_DEBUG', False)

QUEUE_PROVIDER = 'redis'

QUEUE_CONFIG = {
    'redis': {
        'host': os.environ.get('REDIS_HOST', 'localhost').split(":", 2)[0],
        'port': os.environ.get('REDIS_HOST', 'localhost').split(":", 2)[1],
        'db': os.environ.get('REDIS_DB', '0'),
        'password': os.environ.get('REDIS_PASSWORD'),
        'wait_queue': os.environ.get('REDIS_WAIT_QUEUE', '{}_wait_q'.format(TYPE)),
        'work_queue': os.environ.get('REDIS_WORK_QUEUE', '{}_work_q'.format(TYPE)),
        'backlog_queue': os.environ.get('REDIS_BACKLOG_QUEUE', '{}_backlog_q'.format(TYPE)),
        'wait_queue_amount': int(os.environ.get('REDIS_WAIT_QUEUE_AMOUNT', 1)),
        'ssl' : os.environ.get('REDIS_SSL', 'true').lower() in ('true')

    }
}

DB_CONFIG = {
    'psql':{
        'host': os.environ.get('PSQL_HOST', 'localhost'),
        'port': int(os.environ.get('PSQL_PORT', 5432)),
        'db': os.environ.get('PSQL_DB', 'ibmcloud'),
        'user': os.environ.get('PSQL_USER', 'admin'),
        'password': os.environ.get('PSQL_PASSWORD'),
        'schema': os.environ.get('PSQL_SCHEMA'),
    }

}


# Dict corresponding to https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': os.environ.get('BROKER_LOG_MSG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            'datefmt': os.environ.get('BROKER_LOG_DATE_FORMAT', '%Y-%m-%d %H:%M:%S'),
        },
    },
    'handlers': {
        'default': {
            'level': os.environ.get('BROKER_LOG_LEVEL', 'DEBUG'),
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        'broker': {
            'handlers': ['default'],
            'level': os.environ.get('BROKER_LOG_LEVEL', 'DEBUG'),
            'propagate': True
        }
    }
}
