# Steganography (Text Stegonagraphy) Demo

### Stego Team Members 
Yi Ling Wu, Cindy Zheng

### Description:
A demo on how to embed a secret message into a text file using a form of White-Space steganography, and how to extract a secret message from a cover message.

### Dependencies and Requirements:
Python 3 
Make

### *Note about Makefile*
The makefile uses `python3` to run embed.py and extract.py. If you only have one version of python on your computer, you may have to edit the makefile and change `python3` to `python`
### Launch Codes:
1. Clone this repo `git clone https://github.com/YLW-105/textstegonagraphy`
2. Change directories to the repo `cd textstegonagraphy`

### To embed using White-Space steganography
1. Run this command in terminal `make embed ARGS="tryembedding.txt secret.txt" > output.txt`
  
  secret.txt is embedded into tryembedding.txt, and the result is piped into the output.txt file.
  The secret message can be extracted following the instructions below, using output.txt as the argument.
 
### To extract a secret message from the cover message file
1. Run this command in terminal `make extract ARGS="tryextracting.txt"`

