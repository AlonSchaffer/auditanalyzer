import os
import logging


def find_log_in_dir(dir_log_files):
    log_names = []
    try:
        for file in os.listdir(dir_log_files):
            if file.startswith("audit.log"):
                log_names.append(file)
    except Exception as e:
        logging.error('couldnt iterate through ' + dir_log_files + str(e))
    return log_names
