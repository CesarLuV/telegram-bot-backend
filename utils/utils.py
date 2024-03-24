'''File that contains utilities to be reused.'''

from datetime import datetime
from os import environ
from pathlib import Path
from timeit import default_timer
from typing import List, Tuple

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def measure_time(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        logger.info(
            f"{'='*39}\nStart time [{name}]: {datetime.now()}\n{'='*39}\n")
        start = default_timer()
        res = func(*args, **kwargs)
        end = default_timer()
        logger.info(f"{'='*39}\nEnd time {name}: {datetime.now()}\n{'='*39}\n")
        logger.info(
            f"{'#'*39}\nElapsed time of [{name}]: {end - start}\n{'#'*39}\n")
        return res
    return wrapper


@measure_time
def file_opener(file_name: str, folder_path: str = None) -> List[Tuple[str, str]]:
    env_vars = dict(environ)
    folder_path = folder_path if folder_path else env_vars.get('FOLDER_NAME')
    phrases = []
    
    if not folder_path:
        raise ValueError("Folder path not provided")
    
    file_path = Path(folder_path + "/" + file_name)

    if not file_path:
        raise ValueError(f'File [{file_path}] not found')
    
    with open(file=file_path, mode="r") as opened_file:
        while True:
            line = opened_file.readline()
            if not line:
                break
            if "#" == line[0]:
                continue
            if line.strip() == "\n":
                continue
            if "\\" in line:
                clean_line = line.replace("\\", "").replace("\n", "").strip()
                line = opened_file.readline()
                clean_author = line.replace("—", "").replace("\n", "").strip()
                phrases.append((clean_line, clean_author))
    return phrases
