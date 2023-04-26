# PassMute a Password Trasmutation/Mutator tool

This is a command-line tool written in Python that applies one or more transformation rules to a given password or a list of passwords read from one or more files. The tool can be used to generate transformed passwords for security testing or research purposes. Also while you do pentesting or bug hunting it will be very useful tool for you to brute force the passwords!!

The transformation rules include:

**reverse:** reverses the password string
**uppercase:** converts the password to uppercase letters
**lowercase:** converts the password to lowercase letters
**swapcase:** swaps the case of each letter in the password
**capitalize:** capitalizes the first letter of the password
**leet:** replaces some letters in the password with their leet equivalents
**strip:** removes all whitespace characters from the password

The tool can also write the transformed passwords to an output file and run the transformation process in parallel using multiple threads.

**Usage**
To use the tool, you need to have Python 3 installed on your system. Then, you can run the tool from the command line using the following options:
``` python PassMute.py [-h] [-f FILE [FILE ...]] -r RULES [RULES ...] [-v] [-p PASSWORD] [-o OUTPUT] [-t THREAD_TIMEOUT] [--max-threads MAX_THREADS] ``` 

Here's a brief explanation of the available options:

**-h, --help: shows the help message and exits

-f FILE [FILE ...], --file FILE [FILE ...]: one or more files to read passwords from

-r RULES [RULES ...], --rules RULES [RULES ...]: one or more transformation rules to apply

-v, --verbose: prints verbose output for each password transformation

-p PASSWORD, --password PASSWORD: transforms a single password

-o OUTPUT, --output OUTPUT: output file to save the transformed passwords

-t THREAD_TIMEOUT, --thread-timeout THREAD_TIMEOUT: timeout for threads to complete (in seconds)

--max-threads MAX_THREADS: maximum number of threads to run simultaneously (default: 10)**


**Example**
Here's an example command that reads passwords from a file, applies two transformation rules, and saves the transformed passwords to an output file:

``` python PassMute.py -f passwords.txt -r leet uppercase -o transformed.txt ``` 


**Legal Disclaimer**:

You might be super excited to use this tool, me too. But here is the problem! whitehatsoumya or Github won't be responsible for any actions made by you. This tool is made for security research and education purposes only. It is the end user's responsibility to obey all applicable 
local, state and federal laws. 
