import logging
import json
import os
PATH = 'command_counter.json'


def write_to_file(num):
   try:
       counter = {'number': num}
       with open(PATH, 'w') as wf:
           json.dump(counter, wf)
   except Exception as e:
       logging.error('there is a problem with write to file func' + str(e))


def get_num_from_file():
    try:
        with open(PATH, 'r') as rf:
            if os.stat(PATH).st_size == 0:
                return 0
            else:
                number = json.load(rf)
                return number['number']
    except Exception as e:
        logging.error('there is a problem with get num from file func' + str(e))
