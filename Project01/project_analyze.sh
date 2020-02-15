#!/bin/bash

if [[ "$1" -eq "1" ]]; then

	if [[ -f fixme.log ]]; then
		rm fixme.log
		for file in *
		do
			line=$(tail -n 1 "$file" )
				if [[ $line = *"#FIXME"* ]]; then
					echo -e "$file\n" >> fixme.log
				fi
		done
	fi

	if [[ ! -f fixme.log ]]; then
		touch fixme.log
		for file1 in *
                do
                        line=$(tail -n 1 "$file1" )
                                if [[ $line = *"#FIXME"* ]]; then
                                        echo -e "$file1\n" >> fixme.log
                                fi
                done
	fi

elif [[ "$1" -eq "2" ]]; then
	echo "Enter file extension:"
	read x
	echo "The number of files is"  $(find * -type f -name "*$x"| wc -l)


elif [[ "$1" -eq "3" ]]; then
	du `ls -F . | grep -v \/ | xargs` | sort -rn | cut -f2 | xargs du -sh
fi


