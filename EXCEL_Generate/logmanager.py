#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

import logging.config
import os
import util

logging.config.fileConfig(os.path.join(util.getProjectPath(), "config/logger.conf"))

def getLogger(name):
    """Retourne un logger avec le nom passé en paramètre
        -name: Une string contenant le nom du logger
    """
    return logging.getLogger(name)
