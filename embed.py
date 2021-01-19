import sys
original = sys.argv[1]
secret = sys.argv[2]
debug = False


omessage = open(sys.argv[1], 'r')
cotext = omessage.read()

smessage = open(sys.argv[2], 'r')
setext = smessage.read()

binarysetext_space = " ".join(f"{ord(i):08b}" for i in setext)
binarysetext = binarysetext_space.replace(' ', '')
counter = 0
cover = ""

cotext= cotext.replace('."','. "')

for i in range(len(cotext)):
  if counter < len(binarysetext):
    if (cotext[i] == "."):
      if (binarysetext[counter]=="0"):
       cover = cover + "."
      elif (binarysetext[counter]=="1"):
        cover = cover + ". "
      counter = counter + 1
    else:
      cover = cover + cotext[i]

print (cover+ " ")



if(debug):
  print("original message: "+ cotext)
  print("secret message: "+ setext)
  print("key: 1 space for 0, 2 spaces for 1")
  print("binary of secret message: " +binarysetext)
