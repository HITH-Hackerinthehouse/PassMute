logo = """     
  _____                              _         _                          
 |  __ \                            | |       | |                         
 | |__) |_ _ ___ ___ _ __ ___  _   _| |_ ___  | |__  _   _                
 |  ___/ _` / __/ __| '_ ` _ \| | | | __/ _ \ | '_ \| | | |               
 | |  | (_| \__ \__ \ | | | | | |_| | ||  __/ | |_) | |_| |               
 |_|   \__,_|___/___/_| |_| |_|\__,_|\__\___| |_.__/ \__, |               
                                                      __/ |               
                                              _    _ |___/ _______ _    _ 
                                             | |  | |_   _|__   __| |  | |
                                             | |__| | | |    | |  | |__| |
                                             |  __  | | |    | |  |  __  |
                                             | |  | |_| |_   | |  | |  | |
                                             |_|  |_|_____|  |_|  |_|  |_|
                                                  Developed in India with ❤️                           
"""
print("\033[31m" + logo + "\033[0m")

import threading
import string
import argparse
import sys
import os


def transform_password(password, rules):
    transformed_password = password
    for rule in rules:
        if rule == "reverse":
            transformed_password = transformed_password[::-1]
        elif rule == "uppercase":
            transformed_password = transformed_password.upper()
        elif rule == "lowercase":
            transformed_password = transformed_password.lower()
        elif rule == "swapcase":
            transformed_password = transformed_password.swapcase()
        elif rule == "capitalize":
            transformed_password = transformed_password.capitalize()
        elif rule == "leet":
            leet_map = {
                "a": "4",
                "e": "3",
                "i": "1",
                "o": "0",
                "s": "5",
                "t": "7",
            }
            transformed_password = "".join(
                leet_map.get(c.lower(), c) for c in transformed_password
            )
        elif rule == "strip":
            transformed_password = "".join(
                c for c in transformed_password if c not in string.whitespace
            )
        else:
            print(f"Unknown rule: {rule}")
    return transformed_password

def transmute_password(password, rules, output_file=None):
    transformed_password = transform_password(password, rules)
    print(f"Transformed password: {transformed_password}")
    if output_file:
        with open(output_file, 'a') as f:
            f.write(transformed_password + '\n')

def transmute_passwords_from_file(filename, rules, verbose, output_file=None, thread_timeout=None, max_threads=10):
    if not os.path.isfile(filename):
        print(f"Error: {filename} is not a file")
        return
    with open(filename, "r") as f:
        passwords = f.read().splitlines()
    threads = []
    for password in passwords:
        while threading.active_count() >= max_threads:
            pass
        t = threading.Thread(target=transmute_password, args=(password, rules, output_file))
        threads.append(t)
        t.start()
    if verbose:
        for t in threads:
            t.join()
    else:
        for t in threads:
            t.join(thread_timeout)

def transmute_password_single(password, rules, output_file=None):
    transformed_password = transform_password(password, rules)
    print(f"Transformed password: {transformed_password}")
    if output_file:
        with open(output_file, 'a') as f:
            f.write(transformed_password + '\n')

def main():
    parser = argparse.ArgumentParser(description="Password transformation tool")
    parser.add_argument("-f", "--file", nargs="+", help="file(s) to read passwords from")
    parser.add_argument("-r", "--rules", nargs="+", help="transformation rules to apply")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-p", "--password", help="transform a single password")
    parser.add_argument("-o", "--output", help="output file to save transformed passwords")
    parser.add_argument("-t", "--thread-timeout", type=float, help="timeout for threads to complete (in seconds)")
    parser.add_argument("--max-threads", type=int, default=10, help="maximum number of threads to run simultaneously")
    args = parser.parse_args()
    if not args.rules:
        print("Error: Rules are required")
        parser.print_help()
        sys.exit()
    if args.file:
        for filename in args.file:
            transmute_passwords_from_file(filename, args.rules, args.verbose, args.output, args.thread_timeout)
    if args.password:
        transmute_password_single(args.password, args.rules, args.output)

if __name__ == "__main__":
    main()
