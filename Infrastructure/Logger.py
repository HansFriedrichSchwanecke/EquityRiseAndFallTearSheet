import logging as log


class Logger:

    def __init__(self, file_path: str, logging_level) -> None:
        super().__init__()
        log.basicConfig(file_path, encoding = 'utf_8', level=logging_level)
        log.info('Logging started.')

    