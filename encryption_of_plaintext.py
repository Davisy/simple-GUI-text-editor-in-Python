while True:
    #user input from the console
    plaintext = raw_input('Enter a plaintext:')
    dist = int(raw_input('Enter Encryption code:'))
    code=''
    for ch in plaintext:
        ordValue=ord(ch)
        cipherText=ordValue + dist
        if cipherText > ord('z'):
            cipherText=ord('a') + dist-\
            (ord('z')-ordValue + 1)
        code += chr(cipherText)
    
    print('Encryption word is:',code)
            
    