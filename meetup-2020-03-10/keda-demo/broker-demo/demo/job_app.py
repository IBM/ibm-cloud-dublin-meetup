# Copyright 2019 IBM Corporation All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
from demo.work_stream import RedisWorkStream

class Scripter(object):
    cfg = None
    logger = None
    r = None
    post = None

    def __init__(self, api_imp, post_process_imp, cfg, logger):
        """ Initializing demo broker  """
        self.cfg = cfg
        self.logger = logger
        self.post = post_process_imp
        self.r = RedisWorkStream(cfg, logger, api_imp, post_process_imp)

    def start(self):
        self.logger.info('Started demo job for {}'.format(self.cfg.TYPE))
        if not self.r._at_capacity():
            task = self.r._take_task()
            if task is not None:
                try:
                    self.post.putTaskToStdOut(task)
                except Exception as err:
                    self.r._logErrorAndResume(error, task)
                self.r._mark_done(task)
