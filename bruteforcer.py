#! /usr/bin/env python3
import re
import sys
import time
import hashlib
import string
import itertools


upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
digits = list(string.digits)


def determinePatternCase(pattern):
	lengthOfPattern = len(pattern)
	pattern = list(pattern)
	casePattern = ""

	for i in range(lengthOfPattern):
		if ord(pattern[i]) >= 48 and ord(pattern[i]) <= 57:
			casePattern = casePattern + "d"
		elif ord(pattern[i]) >= 65 and ord(pattern[i]) <= 90:
			casePattern = casePattern + "u"
		elif ord(pattern[i]) >= 97 and ord(pattern[i]) <= 122:
			casePattern = casePattern + "l"

	return casePattern


def prod(pattern):

	upper = list(string.ascii_uppercase)
	lower = list(string.ascii_lowercase)
	digits = list(string.digits)
	choice = []

	for i in pattern:
		match i:
			case "u": choice.append(upper)
			case "l": choice.append(lower)
			case "d": choice.append(digits)

	return list(itertools.product(*choice))


def hashValidator(hashes):
	validatedMD5 = []
	validatedSHA = []

	for hsh in hashes:
		try:
			int(hsh, 16)
		except:
			pass
		if len(hsh) == 32:
			validatedMD5.append(hsh)
		elif len(hsh) == 128:
			validatedSHA.append(hsh)
		else:
			pass

	return validatedMD5, validatedSHA


def md5Encode(word):
	return hashlib.md5(word.encode()).hexdigest()


def shaEncode(word):
	return hashlib.sha512(word.encode()).hexdigest()


def encodeChecker(word, validatedMD5, validatedSHA):
	encodedmd5 = md5Encode(word)
	encodedsha = shaEncode(word)

	if encodedmd5 in validatedMD5:
		print(f"MD5 Hash Cracked - {encodedmd5}:{word}")
		validatedMD5.remove(encodedmd5)
	if encodedsha in validatedSHA:
		print(f"SHA512 Hash Cracked - {encodedsha}:{word}")
		validatedSHA.remove(encodedsha)


def helper():
	print("Usage Dictionary - python3 script.py dict <wordlistpath> <hashlist>")
	print("Example - python3 script.py dict /usr/bin/wordlists/rockyou.txt /tmp/hash.txt")
	print("Usage Bruteforce - python3 script.py brute <pattern> <hashlist>")
	print("Example - python3 script.py brute Aaaa00 /tmp/hashes.txt")
	print("This script can crack both MD5 and SHA-512 hashes using a specified wordlist.")
	print("It can also attempt to bruteforce a hash, based on a provided pattern.")
	print("Pattern Example - For the password 'Password123', the pattern would be Aaaaaaaa000.")


if len(sys.argv) < 2:
	helper()
	exit()
elif sys.argv[1] == "dict":
	choice = sys.argv[1]
	wordList = sys.argv[2]
	hashValue = sys.argv[3]
elif sys.argv[1] == "brute":
	choice = sys.argv[1]
	pattern = sys.argv[2]
	hashValue = sys.argv[3]
else:
	helper()
	exit()


if __name__ == '__main__':

	startTime = time.time()

	with open(hashValue, "r") as hashList:
		hashes = hashList.read().splitlines()
		validatedMD5, validatedSHA = hashValidator(hashes)

	if choice == "dict":
		f = open(wordList, "r")
		for word in f:
			if len(validatedMD5 + validatedSHA) == 0:
				break
			word = word.rstrip('\n')
			encodeChecker(word, validatedMD5, validatedSHA)

	elif choice == "brute":
		casePattern = determinePatternCase(pattern)
		result = prod(casePattern)
		for i in result:
			if len(validatedMD5 + validatedSHA) == 0:
				break
			word = "".join(i)
			encodeChecker(word, validatedMD5, validatedSHA)
				
	endTime = time.time()
	print("Time taken to perform password attack was", round(endTime - startTime, 2), "secconds.")

