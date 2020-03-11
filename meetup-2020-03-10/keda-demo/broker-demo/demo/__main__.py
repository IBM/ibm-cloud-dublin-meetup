# Copyright 2019 IBM Corporation All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""
Demo Broker
Usage:
    broker-demo [options]
Options:
    -h --help                   Show this screen.
"""
from demo.app import Worker
from demo.job_app import Scripter
from demo import config
from .logger import logger
from demo.api_imp import Demo
from demo.post_process_imp import DemoPostProcess


def main():
    broker = DemoPostProcess(logger, config)
    if config.MODE == 'broker':
        worker = Worker(Demo, broker, config, logger)
        worker.start()
    elif config.MODE == 'job':
        scripter = Scripter(Demo, broker, config, logger)
        scripter.start()
    else:
        logger.error("We do not support current mode: {}".format(config.MODE))


if __name__ == "__main__":
    # execute only if run as a script
    main()
