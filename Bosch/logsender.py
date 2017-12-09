#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

import logging
import logging.handlers


LOG_FILE = 'test.log'
# get a handler instance
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=5)
# the format of a log item
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
# get a formatter instance
formatter = logging.Formatter(fmt)
#  set formatter as format to be used
handler.setFormatter(formatter)

logger = logging.getLogger('test')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('first info')
logger.debug('first debug')


