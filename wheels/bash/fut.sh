#!/bin/bash
#
#fut.sh
#
#find files created/updated today
#
#usage:
#
#	fut.sh <dir>

function recurse()
{
	# 'cd' down into the named directory
	cd $1
	
	# iter through all the files
	for file in *; do

		if [ -d "$file" ]; then
			recurse $file
		fi

		if [ -f "$file" ]; then
			longfile='ls -l --time-style=long-iso $file'
			check='echo "$longfile" | grep "$today"'

			if [ -n "$check" ]; then
				echo "$PWD/$file"
			fi
		fi
	done

	if [ "$1" != "." ]; then
		cd ..
	fi
}

function main()
{
	today='date "+%Y-%m-%d"'

	checkdir=$1

	if [ -z "$checkdir" ]; then
		checkdir="."
	fi

	recurse $checkdir
}

main $1

exit
