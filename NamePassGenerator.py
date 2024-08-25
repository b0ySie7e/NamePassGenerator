#/usr/bin/python3

import argparse
import sys
import os
import signal
from pwn import *

def signal_handler(signal, frame):
    print("\n[+] Exiting.")
    sys.exit(0)

def gen_with_file(file):
    
    input_file = file
    output_file = "wordlist.txt"

    if os.path.exists(output_file):
        print("[!] {} file already exists.".format(output_file))
        sys.exit(1)
    
    log.info('[🤔] Generating...')
    with open(input_file, 'r') as file:
        with open(output_file, 'w') as output:
            for line in file:
                name, lastname = line.strip().split(' ')
                name = name.lower()
                lastname = lastname.lower()
                
                formatted_names = [
                    "{}{}".format(name, lastname),
                    "{}-{}".format(name, lastname),
                    "{}.{}".format(name, lastname),
                    "{}{}".format(name[0], lastname),
                    "{}-{}".format(name[0], lastname),
                    "{}.{}".format(name[0], lastname),
                    "{}{}".format(lastname, name),
                    "{}-{}".format(lastname, name),
                    "{}.{}".format(lastname, name),
                    "{}{}".format(lastname, name[0]),
                    "{}-{}".format(lastname, name[0]),
                    "{}.{}".format(lastname, name[0]),
                    "{}{}".format(name[:3], lastname[:3]),
                    "{}.{}".format(name[:3], lastname[:3])
                ]

                for formatted_name in formatted_names:
                    output.write(formatted_name + '\n')
            log.progress('Task completed and Saved in the file %s'%output_file)

def gen_with_data_user(name, lastname):
    output_file = "wordlistUser.txt"
    
    if os.path.exists(output_file):
        print("[!] {} file already exists.".format(output_file))
        sys.exit(1)
    
    log.info('[🤔] Generating...')
    with open(output_file, 'w') as output:
        formatted_names = [
        "{}{}".format(name, lastname),
        "{}-{}".format(name, lastname),
        "{}.{}".format(name, lastname),
        "{}{}".format(name[0], lastname),
        "{}-{}".format(name[0], lastname),
        "{}.{}".format(name[0], lastname),
        "{}{}".format(lastname, name),
        "{}-{}".format(lastname, name),
        "{}.{}".format(lastname, name),
        "{}{}".format(lastname, name[0]),
        "{}-{}".format(lastname, name[0]),
        "{}.{}".format(lastname, name[0]),
        "{}{}".format(name[:3], lastname[:3]),
        "{}.{}".format(name[:3], lastname[:3])
        ]
        for formatted_name in formatted_names:
            output.write(formatted_name + '\n')
    log.progress('Task completed and Saved in the file %s'%output_file)

if __name__=='__main__':
    signal.signal(signal.SIGINT, signal_handler)
    
    parser=argparse.ArgumentParser(description='Generate a list of users from a firts and last name')
    parser.add_argument('-w','--file', help='file containning the list of users')
    parser.add_argument('-n', '--name', help='Name')
    parser.add_argument('-s', '--surname', help='Surname')
    args = parser.parse_args()
    
    if args.file:
        file=args.file
        if os.path.exists(file):
            gen_with_file(file)
        else:
            print("[😒] file does not exist...")
    elif args.name and args.surname:
        name=args.name
        surname=args.surname
        gen_with_data_user(name, surname)

    else:
        parser.print_help()
    
