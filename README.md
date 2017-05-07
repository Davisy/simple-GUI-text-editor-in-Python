# encryption-of-the-textfile
This is the project for encryption of the text file by using python programming language

## FILE ENCRYPTION PROGRAM:

Python’s ord and chr functions convert characters to their numeric ASCII codes and back again, respectively.Please keep in mind that in Caesar cipher, each letter in the plaintext is replaced with the character that occurs in a given agreed distance value away in the sequence and ASCII is the numerical representation of a character

###FIRST STEP:import python modules
We have to import the os and shutil modules. The os module provides methods we can use to perform file processing operations.we will use the following methods from the os module we imported.
1. The `os.getcwd()` method returns a string representing the current working directory. we'll assign dire to  
   `os.getcwd()`
2. The `os.listdir(path)` displays a list of names of all the entries in the directory path.Our path is dire
   because we have assigned it to os.getcwd()
3. The os.rename(old_fileName,new_fileName).This method takes two arguments, the current filename, and the new
   filename.

The shutil module is for copying files.we will copy a file by just typing this:
`shutil.copy(originalFile,duplicateFile)`

###SECOND STEP:encryption
We have imported the necessary python modules,So the next step is the Encryption,which we know how to do for a plain text.For us to
encrypt a text file,we do the following:
1. Prompt user to enter the text file to encrypt.
2. check if the file exists in the current working directory and if it's a text file to avoid error in your python program.
3. Make a copy of the user file using `shutil.copy(userFile,copyFile)`.
4. open the userFile,read the file,and use for loop to iterate each word in the file and encrypt it.
5. Prompt the user to enter the name to save the unencrypted file(copyFile), because we have encrypted the userFile.If you don't do this step,the user can lose his unencrypted file and to retrieve it, he will have to decrypt the encrypted file.
6. Check if the new name of the unencrypted file does not exist in the current working directory.

###FINAL STEP:quitting the program
In the code, you will notice the following:
`print 'Press Enter to quit'`
`if plainFile == "":`
    `break`
The print statement tells the user:Press enter key on the keyboard to quit. The if conditional statement and break statement tells the computer that if no entry is made by the user which we signify no entry as a double quote(empty string),the program will exit from the while loop, Hence stopping the program.
