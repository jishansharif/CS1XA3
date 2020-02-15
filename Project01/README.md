# CS1XA3 Project01 -sharifj-

##Usage
	Execute this script from project root with:
		chmod +x CS1XA3/Project01/project_analyze.sh
		./CS1XA3/Project01/project_analyze arg n
		With possible arguments
		arg1 
		arg2
		My program only allows one user input rather than multiple.

## Feature 6.2
	Execution: Execute this program by entering ./project_analyze.sh 1
		     on your terminal

	Description: Had to make use of a tail command to find every file in 
	my repository that has the word #FIXME in the last line.

	Made use of if operators if the file fixme.log aldready exists.

	Made use of for loops within an if statement if the file
	fixme.log does not exist.	     
		     
	Had to create a fixme.log if it didn't exist and overwrite contents 
	if it did.
	
	Resources: I had to figure out the syntax for the tail operation and
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

	Resourses: man ls, man du, man grep, man cut. 
		https://www.tecmint.com/check-linux-disk-usage-of-files-and-directories/
		https://www.folkstalk.com/2012/02/cut-command-in-unix-linux-examples.html
		https://shapeshed.com/unix-sort/
		https://unix.stackexchange.com/questions/48492/list-only-regular-files-but-not-directories-in-current-directory

# Feature 6.5
	Execution: Execute this program by entering ./project_analyze.sh 2
                     on your terminal
	Description : Asked for a user extension, searches for this extension using the find type operator and counts the no of files
		      with this extension. 
        Resources : I have used the lecture slide to implement the pipe functions, count, and grep 


# Custom Features
Organized Directory!
				Description: If I have a directory containing more than 2 types of files, Within that directory, 
				Subdirectories will be made and files with the same extension will be placed on one file.
				If there are unique file extensions and one of each, A new subdirectory will be named labelled “Others”

Clearing Space
			       Description: If the system memory is above a certain limit, files which have not been used for over
				thirty days will be automatically deleted from the computer. If there is enough storage, Ignore.
