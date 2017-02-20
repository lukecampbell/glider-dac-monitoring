#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
glider_dac_monitoring/config.py

Configuration variables for the project
'''
import os

_CONFIG = None


def get_config():
    '''
    Returns a dictionary of configuration variables specified by environment
    variables
    '''
    global _CONFIG
    if _CONFIG is None:
        _CONFIG = {}
        _CONFIG['MONGO_HOST'] = os.environ.get('MONGO_HOST', 'localhost')
        _CONFIG['MONGO_PORT'] = os.environ.get('MONGO_PORT', 27107)

    return _CONFIG
