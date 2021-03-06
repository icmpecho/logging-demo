import logging
from random import randint
from time import sleep
from uuid import uuid4


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s')


def process(id, fail):
    logging.info("Processing task %s" % id)
    sleep(2)
    if fail:
        logging.error("Task %s failed to process" % id)
    else:
        logging.info("Task %s completed" % id)


if __name__ == '__main__':
    error_rate = randint(0, 9)
    logging.info("Starting processor with error rate %d" % error_rate)
    while True:
        process(uuid4().hex, randint(0, 9) <= error_rate)

