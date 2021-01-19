import sys
cover = sys.argv[1]
debug = False


message = open(sys.argv[1], 'r')
text = message.read()

binaryMessage = ""

for i in range(len(text)- 1):
  if text[i]==".":
    if text[i+1].isspace():
      if i+2 >= len(text):
        binaryMessage = binaryMessage + "0"
        i=i+2
      elif text[i+2].isspace():
        binaryMessage = binaryMessage + "1"
      else:
        binaryMessage = binaryMessage + "0"
secretMessage = ""
trun = len(binaryMessage)-(len(binaryMessage) % 8)
for i in range(0, len(binaryMessage[:trun]),8):
  strMg = ""
  if (binaryMessage[i:8+i]) != "00000000":
    strMg= int(binaryMessage[i:8+i], 2)
    secretMessage = secretMessage + chr(strMg)
  else:
    break
    
print(secretMessage)


if(debug):
  print("cover message: "+ cover)
  print("key: 1 space for 0, 2 spaces for 1")
  print("binary: " +binaryMessage)
  print("extracted secret message: " +secretMessage)
