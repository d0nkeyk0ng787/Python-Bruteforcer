# Python-Bruteforcer
This is a python script that can perform a dictionary attack against MD5, SHA512. It can also perform a hash bruteforce based on a provided pattern for the plaintext associated with that hash.

* Usage Dictionary - python3 script.py dict <wordlistpath> <hashlist>
* Example - python3 script.py dict /usr/bin/wordlists/rockyou.txt /tmp/hash.txt
* Usage Bruteforce - python3 script.py brute <pattern> <hashlist>
* Example - python3 script.py brute Aaaa00 /tmp/hashes.txt
* This script can crack both MD5 and SHA-512 hashes using a specified wordlist.
* It can also attempt to bruteforce a hash, based on a provided pattern.
* Pattern Example - For the password 'Password123', the pattern would be Aaaaaaaa000.
