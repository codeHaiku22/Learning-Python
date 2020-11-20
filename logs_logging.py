#!/usr/bin/python
import logging

"""
Note: The .basicConfig() function can only be called once.  Therefore, each code block below must be run independent of the other modules.
        - This why each one has been commented out, since only one can exist.
"""

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #1 - Logging Levels                                                                   """
"""---------------------------------------------------------------------------------------------------"""
#Logging Levels
#By default, the logging level is set to warning and above.
#logging.debug('This is a debug message.')
#logging.info('This is an info message.')
#logging.warning('This is a warning message.')               #WARNING:root:This is a warning message.
#logging.error('This is an error message.')                  #ERROR:root:This is an error message.
#logging.critical('This is a critical message.')             #CRITICAL:root:This is a critical message.

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #2 - .basicConfig()                                                                   """
"""---------------------------------------------------------------------------------------------------"""
#.basicConfig()
#The default logging level can be changed.
#The "%(asctime)s adds the time of creation of the LogRecord.
# - The datefmt attribute changes the format of this timestamp (uses the same formatting language as the formatting functions in the datetime module).
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

#logging.debug('This is a debug message.')                   #11/17/2020 13:32:19 - root - DEBUG - This is a debug message.
#logging.info('This is an info message.')                    #11/17/2020 13:32:19 - root - INFO - This is an info message.
#logging.warning('This is a warning message.')               #11/17/2020 13:32:19 - root - WARNING - This is a warning message.
#logging.error('This is an error message.')                  #11/17/2020 13:32:19 - root - ERROR - This is an error message.
#logging.critical('This is a critical message.')             #11/17/2020 13:32:19 - root - CRITICAL - This is a critical message

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #3 - Logging to a File                                                                """
"""---------------------------------------------------------------------------------------------------"""
#Logging to a File
# logging.basicConfig(filename='block3.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# logging.warning('This will get logged to a file.')

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #4 - Logging Variable Data                                                            """
"""---------------------------------------------------------------------------------------------------"""
#Logging Variable Data
# name = 'Johnny'

# logging.error('%s raised an error', name )                  #ERROR:root:Johnny raised an error

# #using f-strings
# logging.error(f'{name} raised an error')                    #ERROR:root:Johnny raised an error

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #5 - Capturing Stack Traces                                                           """
"""---------------------------------------------------------------------------------------------------"""
#Capturing Stack Traces

#exc_info Parameter
#The exc_info parameter allows us to capture the full stack trace in an application.  
#Execption information can be capture if the exc_info parameter is inlcuded in the logging and set to True.
# a = 5
# b = 0

# try:
#     c = a / b
# except Exception as e:
#     logging.error("Exception occurred", exc_info=True)      #ERROR:root:Exception occurred
#                                                             #Traceback (most recent call last):
#                                                             #  File "./logs_logging.py", line 55 in <module>
#                                                             #    c = a / b
#                                                             #ZeroDivisionError: division by zero

# #exception() Method
# #If logging from an exception handler, use the logging.exception() method.
# #This method logs a message with level ERROR and adds exception information to the message.
# #It is a shorter way of calling logging.error(exc_info="True")
# #Since this method always dumps exception information, it should only be called from an exception handler.
# a = 5
# b = 0

# try:
#     c = a / b
# except Exception as e:
#     logging.exception("Exception occurred")                 #ERROR:root:Exception occurred
#                                                             #Traceback (most recent call last):
#                                                             #  File "./logs_logging.py", line 72 in <module>
#                                                             #    c = a / b
#                                                             #ZeroDivisionError: division by zero

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #6 - Classes and Functions                                                            """
"""---------------------------------------------------------------------------------------------------"""
#Classes and Functions
#So far we have seen the default logger named "root" which is used by the logging module whenever its functions are called directly: logging.debug()
#You should define your own logger by creating an object of the Logger class, especially if your application has multiple modules.
#The most commonly used classes defined in the logging module are:
# - Logger      This is the class whose objects will be used in the application code directly to call the functions.
# - LogRecord   Automatically created by Logger and contains information related to the logged event (name of logger, function, line number, message, etc.)
# - Handler     Send the LogRecord to the required output destination; is a base for subclasses like StreamHandler, FileHandler, HTTPHandler, etc.
# - Formatter   This is where you specify the format of the output by specifying a string format that lists out the attributes that the output should contain.
#Out of all of these, we mostly deal with the Logger class which are instantiated using the module-level function logging.getLogger(name).
# - Multiple calls to getLogger() with the same name will return a reference to the same Logger object.
#   + This saves us from passing the logger objects to every part where it is needed.

#Let's create a custom logger named ".example_logger"
#Unlike the root logger: 
# - The name of a custom logger is not part of the default output format
# - A custom logger cannot be configured using basicConfig(); instead you have to use Handlers and Formatters

# logger = logging.getLogger('example_logger')
# logger.warning('This is a warning.')                        #This is a warning.

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #7 - Using Handlers                                                                   """
"""---------------------------------------------------------------------------------------------------"""
#Using Handlers
#Handlers are used to configure custom loggers and can send logs to multiple places when they are generated.
# - Standard output stream
# - File
# - HTTP
# - SMTP
#Like loggers, you can set the severity level in handlers.
# - This is useful if you want to set multiple handlers for the same logger, but want different severity levels for each of them.
#    + For example, you may want logs with level WARNING and above sent to the console but level ERROR and above to also go to a file.

# #Create a custom logger
# logger = logging.getLogger(__name__)

# #Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('block7.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)

# #Create formatters
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# #Add formatters to handlers
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# #Add handlers to logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)

# #Outputs all information to console that is WARNING or above (including ERROR).
# logger.warning('This is a warning.')                        #__main__ - WARNING - This is a warning.
# logger.error('This is an error!')                           #__main__ - ERROR - This is an error!

# #The file "block7.log" will only contain the ERROR entry.

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #8 - Using Configuration (.conf) Files                                                """
"""---------------------------------------------------------------------------------------------------"""
#Using Configuration (.conf) Files
#You can configure logging as shown in CODE BLOCK #7 above by creating a configuration file and loading it using fileConfig().
# - A dictionary can also be used to create a configuration and can be loaded using dictConfig().

#The content below has been saved in a file named "block8.conf".
# - It contains 2 loggers, 1 handler, and 1 formatter.
#--[ block8.conf ]----------------------------------------------------------------------------------#
# [loggers]
# keys=root,sampleLogger
#
# [handlers]
# keys=consoleHandler
#
# [formatters]
# keys=sampleFormatter
#
# [logger_root]
# level=DEBUG
# handlers=consoleHandler
#
# [logger_sampleLogger]
# level=DEBUG
# handlers=consoleHandler
# qualname=sampleLogger
# propagate=0
#
# [handler_consoleHandler]
# class=StreamHandler
# level=DEBUG
# formatter=sampleFormatter
# args=(sys.stdout,)
#
# [formatter_sampleFormatter]
# format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
#---------------------------------------------------------------------------------------------------#

#To load the block8.conf file, the fileConfig() method must be used.
# import logging.config

# logging.config.fileConfig(fname='block8.conf', disable_existing_loggers=False)

# #Get the logger specified in the file
# logger = logging.getLogger(__name__)

# logger.debug('This is a debug message.')                    #2020-11-20 14:34:05,519 - __main__ - DEBUG - This is a debug message.

"""---------------------------------------------------------------------------------------------------"""
"""  CODE BLOCK #9 - Using Configuration (.yaml) Files                                                """
"""---------------------------------------------------------------------------------------------------"""
#Using Configuration (.yaml) Files
#You can configure logging as shown in CODE BLOCK #7 above by creating a configuration file and loading it using fileConfig().
# - A dictionary can also be used to create a configuration and can be loaded using dictConfig().

#The content below has been saved in a file named "block9.yaml".
# - It contains 2 loggers, 1 handler, and 1 formatter.
#--[ block9.yaml ]----------------------------------------------------------------------------------#
# version: 1
# formatters:
#   simple:
#     format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# handlers:
#   console:
#     class: logging.StreamHandler
#     level: DEBUG
#     formatter: simple
#     stream: ext://sys.stdout
# loggers:
#   sampleLogger:
#     level: DEBUG
#     handlers: [console]
#     propagate: no
#   root:
#     level: DEBUG
#     handlers: [console]
#---------------------------------------------------------------------------------------------------#

#To load the block8.conf file, the fileConfig() method must be used.
import logging.config
import yaml

with open('block9.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message.')                    #2020-11-20 14:45:55,228 - __main__ - DEBUG - This is a debug message.