from __future__ import print_function  # Python 2/3 compatibility
import json
import boto3
import logging
import argparse

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    init_logger()
    args = parse_args()
    print("Hello world")

def init_logger():
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)


def parse_args():
    parser = argparse.ArgumentParser(
            description='Hello world',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--stage',
                      choices=CONFIG.keys(),
                      default='DEV',
                      type=str,
                      help='Stage/region of the AWS account')

    args = parser.parse_args()
    return args


main()
