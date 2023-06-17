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
import random
import requests
import subprocess

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

# Constant
__version__ = "2.0"
GITHUB_RELEASES_API = "https://api.github.com/repos/HITH-Hackerinthehouse/PassMute/releases/latest"
ENCRYPTION_KEY = b"UzBrYTBkb2FqZGdvQCMjJCQ4ODk="

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

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def evaluate_password_strength(password):
    # Define the criteria to evaluate the password strength
    length = len(password)
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Evaluate the password strength based on the defined criteria
    if length >= 8 and has_lowercase and has_uppercase and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_lowercase or has_uppercase) and has_digit:
        return "Medium"
    else:
        return "Weak"

def check_for_updates():
    try:
        response = requests.get(GITHUB_RELEASES_API)
        response.raise_for_status()
        latest_version = response.json()["tag_name"]
        if latest_version != __version__:
            print(f"A new version ({latest_version}) is available. Please update the tool.")
        else:
            print("You are using the latest version of the tool.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking for updates: {str(e)}")

def update_tool():
    print("Updating the tool...")
    try:
        response = requests.get(GITHUB_RELEASES_API)
        response.raise_for_status()
        releases = response.json()
        if "assets" in releases and len(releases["assets"]) > 0:
            asset_url = releases["assets"][0]["browser_download_url"]
            download_path = os.path.join(os.getcwd(), "PassMute.py")
            subprocess.run(["curl", "-L", "-o", download_path, asset_url], check=True)
            print("Tool updated successfully.")
        else:
            print("No assets found in the release. Unable to update the tool.")
    except (subprocess.CalledProcessError, requests.exceptions.RequestException) as e:
        print(f"Error updating the tool: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Passmute - An all in one Password transformation and security tool")
    parser.add_argument("-f", "--file", nargs="+", help="file(s) to read passwords from")
    parser.add_argument("-r", "--rules", nargs="+", help="transformation rules to apply")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-p", "--password", help="transform a single password")
    parser.add_argument("-o", "--output", help="output file to save transformed passwords")
    parser.add_argument("-t", "--thread-timeout", type=float, help="timeout for threads to complete (in seconds)")
    parser.add_argument("--max-threads", type=int, default=10, help="maximum number of threads to run simultaneously")
    parser.add_argument("-s", "--strength", metavar="PASSWORD", help="evaluate password strength")
    parser.add_argument("--check-updates", action="store_true", help="check for tool updates")
    parser.add_argument("--update", action="store_true", help="update the tool")
    args = parser.parse_args()

    if args.check_updates:
        check_for_updates()

    if args.update:
        update_tool()

    if args.strength:
        strength = evaluate_password_strength(args.strength)
        print(f"Password strength: {strength}")
        sys.exit()

    if not args.rules:
        print("Error: Rules are required")
        parser.print_help()
        sys.exit()

    if args.file:
        for filename in args.file:
            transmute_passwords_from_file(filename, args.rules, args.verbose, args.output, args.thread_timeout, args.max_threads)
    if args.password:
        transmute_password_single(args.password, args.rules, args.output)

if __name__ == "__main__":
    main()
