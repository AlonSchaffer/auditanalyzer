from log_finder import find_log_in_dir
from parser import parse_to_dict
from message_seperator import message_seperator
from command_counter_file_manager import write_to_file, get_num_from_file
from tcp_socket_sender import send_json_to_port
import logging


def main():
    try:
        dir_log_files = '/var/log/audit/'
        # the last message that the program sent
        message_counter = get_num_from_file()
        # check if log_names has any log files
        log_names = find_log_in_dir(dir_log_files)
        if len(log_names) > 0:
            all_messages = []
            unsent_messages_list = []
            for log_name in log_names:
                try:
                    with open(dir_log_files + log_name, 'r') as log:
                        message_list = message_seperator(log)
                        obj_list = parse_to_dict(message_list)
                        for obj in obj_list:
                            all_messages.append(obj)
                except Exception as e:
                    logging.error('error entering {}'.format(dir_log_files + log) + str(e))

           #doesnt send any
            if len(all_messages) == message_counter:
                #send_json_to_port(all_messages)
                print('all messeges has been sent')
            elif message_counter == 0:
            # sends all messeges that the program found
                send_json_to_port(all_messages)
                write_to_file(len(all_messages))
            else:
                # takes from the counter to the number of messeges and send all the unsent messeges
                for x in range(message_counter + 1, len(all_messages)):
                    unsent_messages_list.append(all_messages[x])
                    send_json_to_port(unsent_messages_list)
                    write_to_file(len(all_messages))
        else:
            logging.warning('couldnt find log names in the directory')
    except Exception as e:
        logging.critical(str(e))

if __name__ == '__main__':
    main()