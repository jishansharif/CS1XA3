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

elif [[ "$1" -eq "4" ]]; then
	echo "BACKUP or RESTORE?"
	read ans
	if [[ "$ans" = "BACKUP" ]]; then
		if [[ -d "/home/sharifj/private/CS1XA3/Project01/backup" ]]; then 
    			rm -r backup
			mkdir backup
			touch restore.log
			mv restore.log backup 
			for file in $(find . -type f -name "*.tmp")
			do
				cp "$file" backup
				path=$(pwd)
				echo "$file" "$path" >>/home/sharifj/private/CS1XA3/Project01/backup/restore.log
				rm "$file"
			done
		else
    			mkdir backup
			touch restore.log
			mv restore.log backup
                        for file in $(find . -type f -name "*.tmp")
                        do
				cp "$file" backup
				path=$(pwd)
				echo "$file" "$path" >>/home/sharifj/private/CS1XA3/Project01/backup/restore.log
				rm "$file"
			done
		fi
	
	elif [[ "$ans" = "RESTORE" ]]; then
		cd backup
                while IFS= read -r line
		do
			firstword=$(echo "$line"|awk '{print $1}')
			secondword=$(echo "$line"|awk '{print $2}')
                                if [[ ! -f "$word1" ]]; then
                                        echo "No such file"
                                fi

				if [[ -f "$word1" ]]; then
					mv "$word1" "$word2"
				fi
                done < restore.log
		
	fi
elif [[ "$1" -eq "5" ]]; then
	if [[  ! -f "permissions.log" ]]; then
		touch permissions.log
	fi
	echo "CHANGE or RESTORE?"
	read ans
	if [[ "$ans" = "CHANGE" ]]; then
		rm permissions.log
		touch permissions.log
		for file in $(find * -type f -name ".sh")
		do
			store=stat$( -c "%a" "$file")
			echo "$file" "$store" >> permissions.log
		done

		for file2 in $(find * -type f -name "*.sh")
		do
			for a in $(find "$file2" -writable)
			do 
				chmod u+x "$file2"
			done
			
			for b in $(find "$file2" -perm -020)
			do
				chmod g+x "$b"
			done

			for c in $(find "$file2" -perm -002)
			do
				chmod o+x "$c"
			done
		done
	fi

	if [[ "$ans" = "RESTORE" ]]; then
		while IFS= read -r line
		do
			firstword=$(echo "$line"|awk '{print $1}')
			secondword=$(echo "$line"|awk '{print $2}')
			chmod "$secondword" "$firstword"
		done < permissions.log
	fi



elif [[ "$1" -eq "6" ]]; then
	echo "Enter file extension "
	read extension
	echo "Enter name of new folder"
	read foldername
	mkdir "$foldername"
	echo "The number of files is"  $(find * -type f -name "*$extension"| wc -l)
	for file in $(find * -type f -name "*$extension"); 
	do
		mv "$file" "$foldername"
	done


elif [[ "$1" -eq "7" ]]; then
	find /home/sharifj/private/CS1XA3/Project01 -type f -mtime +30 -exec rm -f {} \;
	find /var/log -name "*.log" -type f -mtime +30 -exec rm -f {} \;
	find /var/log -name "*.txt" -type f -mtime +30 -exec rm -f {} \;
fi


