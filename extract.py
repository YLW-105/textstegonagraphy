import sys
cover = sys.argv[1]
debug = False

#reading in cover message
message = open(sys.argv[1], 'r')
text = message.read()

binaryMessage = ""

#converting white space into binary string: 1 space is 0, 2 space is 1
for i in range(len(text)- 1):
  if text[i]==".":
    if text[i+1].isspace():
    #checks periods at the very end of the doc
      if i+2 >= len(text):
        binaryMessage = binaryMessage + "0"
        i=i+2
    #2 consecutive spaces
      elif text[i+2].isspace():
        binaryMessage = binaryMessage + "1"
    #1 space after period
      else:
        binaryMessage = binaryMessage + "0"
secretMessage = ""

#dealing with hanging white spaces that are not part of the binary string
trun = len(binaryMessage)-(len(binaryMessage) % 8)

#converting binary string into string
for i in range(0, len(binaryMessage[:trun]),8):
  strMg = ""
  #converting 8 at a time
  if (binaryMessage[i:8+i]) != "00000000":
    strMg= int(binaryMessage[i:8+i], 2)
    secretMessage = secretMessage + chr(strMg)
  else:
    break

#printing secret message
print(secretMessage)

#for debugging
if(debug):
  print("cover message: "+ cover)
  print("key: 1 space for 0, 2 spaces for 1")
  print("binary: " +binaryMessage)
  print("extracted secret message: " +secretMessage)
