import sys

#takes in secret message and the file we want to hide the secret message in as args
original = sys.argv[1]
secret = sys.argv[2]
debug = False

#Opens and reads through the original and secret message files
omessage = open(sys.argv[1], 'r')
cotext = omessage.read()

smessage = open(sys.argv[2], 'r')
setext = smessage.read()

#Converts the secret message to binary
binarysetext_space = " ".join(f"{ord(i):08b}" for i in setext)
binarysetext = binarysetext_space.replace(' ', '')
counter = 0
cover = ""

#Deals with periods that are followed by quotation marks
cotext= cotext.replace('."','. "')

#Embedding the spaces to the original message
for i in range(len(cotext)):
    if counter < len(binarysetext):
        #Checks to see if the character is a period
        if (cotext[i] == "."):
            #See whether to add one or two spaces after the period depending on the binary
            if (binarysetext[counter]=="0"):
                cover = cover + "."
            elif (binarysetext[counter]=="1"):
                cover = cover + ". "
                counter = counter + 1
                #Else keep the text the same
        else:
            cover = cover + cotext[i]

print (cover+ " ")


if(debug):
    print("original message: "+ cotext)
    print("secret message: "+ setext)
    print("key: 1 space for 0, 2 spaces for 1")
    print("binary of secret message: " +binarysetext)
