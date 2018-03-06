import structlog
from random import randint
from time import sleep
from uuid import uuid4


structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.JSONRenderer()
    ]
)


logger = structlog.get_logger()


def process(id, fail):
    log = logger.bind(task_id=id)
    log.info("Started")
    sleep(2)
    if fail:
        log.error("Failed")
    else:
        log.info("Completed")


if __name__ == '__main__':
    error_rate = randint(0, 9)
    logger.info("Starting processor", error_rate=error_rate)
    while True:
        process(uuid4().hex, randint(0, 9) == 0)
