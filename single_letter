#!/bin/bash

read word
wordsize=${#word}

for (( i=0; i<"$wordsize"; i++ )); do
	for x in {a..z}; do
		if [ "$x" == "${word:$i:1}" ]; then continue; fi
		word2="${word:0:$i}$x${word:$i+1:$wordsize+1}"
		grep -w "^$word2$" /usr/share/dict/words
		#awk "/(?!^$word$)(^$word2$)/" /usr/share/dict/words
	done
done
