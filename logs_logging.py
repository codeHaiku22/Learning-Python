#!/usr/bin/python
# import logging

#By default, the logging level is set to warning and above.
# logging.debug('This is a debug message.')
# logging.info('This is an info message.')
# logging.warning('This is a warning message.')               #WARNING:root:This is a warning message.
# logging.error('This is an error message.')                  #ERROR:root:This is an error message.
# logging.critical('This is a critical message.')             #CRITICAL:root:This is a critical message.

#The default logging level can be changed.
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('This is a debug message.')                   #11/17/2020 13:32:19 - root - DEBUG - This is a debug message.
logging.info('This is an info message.')                    #11/17/2020 13:32:19 - root - INFO - This is an info message.
logging.warning('This is a warning message.')               #11/17/2020 13:32:19 - root - WARNING - This is a warning message.
logging.error('This is an error message.')                  #11/17/2020 13:32:19 - root - ERROR - This is an error message.
logging.critical('This is a critical message.')             #11/17/2020 13:32:19 - root - CRITICAL - This is a critical message.

