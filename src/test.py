from __future__ import print_function  # Python 2/3 compatibility
import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    init_logger()
    logger.info("main")


def init_logger():
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)


main()

