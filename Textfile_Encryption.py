'''/
PROJECT NAME:ENCRYPTION OF THE TEXTFILE
AUTHOR:DAVIS DAVID
/'''

#import modules 
import os
import shutil # used for copying files 


dire = os.getcwd() 
listOFFile =os.listdir(dire)

print("ENCRYPTIION OF FILE BY USING PYTHON")
print("=====================================")

print("Your existing text files in this directories are:")
for i in listOFFile:
    if i.endswith(".txt"):
        print(i)

print("") #put some space
while True:
    
    plainFile=raw_input("Enter filename for Encryption:")
    if plainFile == "":
        print("No file has been written try to write a file name")   
        break 
    
    #allow user to Enter the Encryption key
    EncryptionValue = input("Enter the key for Encryption(Must be a Number btn(0-26)):")
    if int(EncryptionValue) == True:
        pass 
    if plainFile in listOFFile and plainFile.endswith(".txt"):
        inputFile=plainFile 
        unEncryptFile='unEcrypted.txt'
        shutil.copy(plainFile,unEncryptFile)
        TextFile = open(plainFile,'r')
        plainText = TextFile.read()
        cipherText=""
        
        for ch in plainText:
            ordValue=ord(ch)
            cipherValue=ordValue + EncryptionValue
            if cipherValue > ord('z'):
                cipherValue=ord('a') + EncryptionValue -\
                    (ord('z') - ordValue + 1)
            cipherText +=chr(cipherValue)
        
        TextFile.close()
        TextFile = open(plainFile,'w')
        TextFile.write(str(cipherText))
        TextFile.close()
        newFileName = raw_input("Save unencrypted file as:")
        
        if newFileName.endswith(".txt") and newFileName not in listOFFile:
            os.rename(unEncryptFile,newFileName)
            print('Encryption successful!!')
        elif not newFileName.endswith(".txt"):
            print("Save file as text format.Re-Enter file name")
        elif newFileName in listOFFile:
            print("This file name already exists!")
        elif plainFile not in listOFFile:
            print("Entry does not exist in current working directory")
        elif not plainFile.endswith(".txt"):
            print("invalid entry!")
    else:#if the file is incorrect
        print("file does not exist or file is not a text file")
        print("try again.....")
         