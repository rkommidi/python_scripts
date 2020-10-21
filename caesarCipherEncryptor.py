#!/usr/bin/env python

# Given a non-empty string of lowercase letters and an non-negative integer representing 
# a key, write a function that returns a new string obtained by shifting every letter in 
# the input string by k positions in the alphabet, where k is the key.

# Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a.



def caesarCipherEncryptor(string, key):
    newLetters = []
	key = key % 26
	for i in string:
		asci = ord(i)
		new_asci = asci + key

		if new_asci > 122:
		 new_asci = 96 + new_asci % 122

		newLetters.append(chr(new_asci))

	return "".join(newLetters)
