import datetime
import json
import logging
#change all messages to be a dictionary to be parsed to json


def parse_to_dict(messages):
    dict_messages_list = []
    for message in messages:
        dict = {}
        now = datetime.datetime.now()
        dict['datetime'] = now.strftime("%d/%m/%Y, %H:%M:%S")
        attributes = message.split()
        for attribute in attributes:
            #getting each attribute and value and adding it to the dictionary
            splitted = attribute.split('=')
            #if the attribute did not got two elements. it means that it doesnt have value to its null
            if len(splitted) == 1:
                dict[splitted[0]] = None
            else:
                dict[splitted[0]] = splitted[1]
        dict_messages_list.append(dict)
    return dict_messages_list
