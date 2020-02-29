#  CS 1XA3 Project01 - sharifj

# Usage Execute this script from project root with: chmod +x CS1XA3/Project01/project_analyze.sh ./CS1XA3/Project01/project_analyze arg n 
  With possible arguments arg1 arg2 My program only allows one user input rather than multiple.
## Feature 01
Description: this feature does ....
Execution: execute this feature by ...
Reference: some code was taken from [[https://someurl.com]]

## Feature 6.2
Execution: Execute this program by entering ./project_analyze.sh 1
	     on your terminal.
Description:Had to make use of a tail command to find every file in 
my repository that has the word #FIXME in the last line.

Made use of if operators if the file fixme.log aldready exists.

Made use of for loops within an if statement if the file
fixme.log does not exist.	     
	     
Had to create a fixme.log if it didn't exist and overwrite contents 
if it did.
Reference: I had to figure out the syntax for the tail operation and
	   for this I used 
https://www.linode.com/docs/quick-answers/linux/how-to-use-tail/
https://linuxize.com/post/linux-tail-command/

## Feature 6.4
Execution: Execute this program by entering ./project_analyze.sh 3
	     on your terminal
Description: Use pipes and a few commands (ls, du, grep, xargs) combining them to 
generate result. ls was used to list only files, grep was used to remove directories,
xarg was used to make pipe input into one line and pass to next command.
I used du to list files by bytes sizes, I also used cut to select the size column, and sort
to sort in descending order of size. I then used the file names and re-entered into du to show final output.

Reference: man ls, man du, man grep, man cut. 
	https://www.tecmint.com/check-linux-disk-usage-of-files-and-directories/
	https://www.folkstalk.com/2012/02/cut-command-in-unix-linux-examples.html
	https://shapeshed.com/unix-sort/
	https://unix.stackexchange.com/questions/48492/list-only-regular-files-but-not-directories-in-current-directory

## Feature 6.5
Execution: Execute this program by entering ./project_analyze.sh 2
                 on your terminal
Description : Asked for a user extension, searches for this extension using the find type operator and counts the no of files
	      with this extension. 
Resources : I have used the lecture slide to implement the pipe functions, count, and grep 

## Custom Features

Organized Directory! Description: If I have a directory containing more than 2 types of files, Within that directory,
Subdirectories will be made and files with the same extension will be placed on one file. If there are unique file extensions 
and one of each, A new subdirectory will be named labelled “Others”

Clearing Space Description: If the system memory is above a certain limit, files which have not been used for over thirty days
will be automatically deleted from the computer. If there is enough storage, Ignore.


## Feature 6.7
Execution:Execute this program by entering ./project_analyze.sh 5
Description: Permissions changed so that only people who have write permissionsalso have executable permission
using chmod 
stat is a Unix system call that returns file attributes about an inode.
awk is used to take the first word of the string. 
Used a combinations of while loops and for loops to help me overwrite permissions.log
This is case sensitive so the code won't run for any input except CHANGE or RESTORE
Resources: http://linuxcommand.org/lc3_lts0090.php
 	   https://www.howtoforge.com/linux-stat-command/
	   https://www.cyberciti.biz/faq/bash-scripting-using-awk/

## Feature 6.8
Execution:Execute this program by entering ./project_analyze.sh 6
Description: (find . -type f -name "*.tmp") was used to identufy files with specific estensions
Using loops, files with the same extension was moved to a backup directory 
pwd was used and copied onto restore.log 
IFS was used to word split after expansion and to split lines into words with the read builtin command.
This was proved essential when constructing the RESTORE requirements.
This is case sensitive so the code won't run for any input except BACKUP or RESTORE
Resources: https://www.cyberciti.biz/faq/howto-find-a-directory-linux-command/
	   https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php
	   https://www.cyberciti.biz/faq/howto-check-if-a-directory-exists-in-a-bash-shellscript/
	   https://askubuntu.com/questions/333710/how-to-find-all-files-with-the-same-extension-within-a-directory
	   https://askubuntu.com/questions/377438/how-can-i-recursively-delete-all-files-of-a-specific-extension-in-the-current-di
	   https://linuxize.com/post/how-to-copy-files-and-directories-in-linux/

## Custom Feature 1
Execution:Execute this program by entering ./project_analyze.sh 6
Description:The user will manually have to choose the files with extensions they'll want to sort
All files with the same extensions are found using the (find . -type f -name "*extension") command
User is asked to choose a filename and the files with the same extension are moved to the newly created folder.
This is done using one for loop to iterate through the files with the same extension.
Note that this method enables the user to sort the repo according to their preference. 
Resources: https://linuxize.com/post/how-to-copy-files-and-directories-in-linux/
	   I have used the lecture slide to implement the pipe functions, count, and grep 


## Custom Feature 2
Execution:Execute this program by entering ./project_analyze.sh 7
Description:This command will delete all files older than 30 days in system 'x'
find x -type f -mtime +30 -exec rm -f {} \;
I have also added a function to remove unused log and txt files
However, this does not take into consideration the storage space, ie it'll delete unused files
regardless if there is enough storage space or not.
Resources:https://tecadmin.net/delete-files-older-x-days/
	  https://stackoverflow.com/questions/13489398/delete-files-older-than-10-days-using-shell-script-in-unix
	  https://www.linux.com/tutorials/linux-101-check-disk-space-command/
