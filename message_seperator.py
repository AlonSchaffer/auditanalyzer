

def message_seperator(log):
    message_list = []
    for line in log:
        #check if the line starts with "type"
        is_type = line.split("=", 2)

        if is_type[0] == 'type':
            # add the line to the message list
            message_list.append(line)
        else:
            # add the line to the last message
            message_list[len(message_list)] += line

    return message_list
