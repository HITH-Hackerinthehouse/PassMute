# PassMute - A Password Trasmutation/Mutator tool

This is a command-line tool written in Python that applies one or more transmutation rules to a given password or a list of passwords read from one or more files. The tool can be used to generate transformed passwords for security testing or research purposes. Also, while you doing pentesting or bug hunting it will be very useful tool for you to brute force the passwords!!


**Proof of Brute Force Passwords by using PassMute**

![Passmute-4](https://user-images.githubusercontent.com/67961316/234674770-1dc87806-4b23-41d4-85b3-0009fe8ac7c1.jpg)


**How Passmute can also help to secure our passwords more?**

PassMute can help to generate strong and complex passwords by applying different transformation rules to the input password. However, password security also depends on other factors such as the length of the password, randomness, and avoiding common phrases or patterns.

The transformation rules include:

**reverse:** reverses the password string

**uppercase:** converts the password to uppercase letters

**lowercase:** converts the password to lowercase letters

**swapcase:** swaps the case of each letter in the password

**capitalize:** capitalizes the first letter of the password

**leet:** replaces some letters in the password with their leet equivalents

**strip:** removes all whitespace characters from the password

The tool can also write the transformed passwords to an output file and run the transformation process in parallel using multiple threads.

**Installation**
```
git clone https://HITH-Hackerinthehouse/PassMute.git
```

```
cd PassMute
```

```
chmod +x PassMute.py
```

**Usage**
To use the tool, you need to have Python 3 installed on your system. Then, you can run the tool from the command line using the following options:

``` python PassMute.py [-h] [-f FILE [FILE ...]] -r RULES [RULES ...] [-v] [-p PASSWORD] [-o OUTPUT] [-t THREAD_TIMEOUT] [--max-threads MAX_THREADS] ``` 

Here's a brief explanation of the available options:

-h or --help: shows the help message and exits

-f (FILE) [FILE ...], --file (FILE) [FILE ...]: one or more files to read passwords from

-r (RULES) [RULES ...] or --rules (RULES) [RULES ...]: one or more transformation rules to apply

-v or --verbose: prints verbose output for each password transformation

-p (PASSWORD) or --password (PASSWORD): transforms a single password

-o (OUTPUT) or --output (OUTPUT): output file to save the transformed passwords

-t (THREAD_TIMEOUT) or --thread-timeout (THREAD_TIMEOUT): timeout for threads to complete (in seconds)

--max-threads (MAX_THREADS): maximum number of threads to run simultaneously (default: 10)


**NOTE**: If you are getting any error regarding **argparse** module then simple install the module by following command:
``` pip install argparse  ```  

**Examples**

Here are some example commands those read passwords from a file, applies two transformation rules, and saves the transformed passwords to an output file:


**Single Password transmutation**: ``` python PassMute.py -p HITHHack3r -r leet reverse swapcase -v -t 50 ``` 


![Passmute-2](https://user-images.githubusercontent.com/67961316/234671617-675195a2-5d10-403a-996a-95b5805a93e1.jpg)


**Multiple Password transmutation**: 
``` python PassMute.py -f testwordlists.txt -r leet reverse -v -t 100 -o testupdatelists.txt ``` 


![Passmute-3](https://user-images.githubusercontent.com/67961316/234671689-54d00da4-90b9-41eb-9b17-bd067e39495e.jpg)


**Here Verbose and Thread are recommended to use in case you're transmutating big files and also it depends upon your microprocessor as well, it's not required every time to use threads and verbose mode.**


**Legal Disclaimer**:

You might be super excited to use this tool, we too. But here we need to confirm! whitehatsoumya, Hackerinthehouse, and Github won't be responsible for any actions made by you. This tool is made for security research and educational purposes only. It is the end user's responsibility to obey all applicable local, state and federal laws. 
