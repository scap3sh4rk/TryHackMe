# Nmap Live Host discovery
[![Nmap TryHackMe](https://github.com/user-attachments/assets/d0d66f73-0111-41fc-b80d-e70e8454aac2)](https://tryhackme.com/room/nmap01)

## Task 4
#### Scans: 
- ARP scan [Link layer]
- Ping scan [Internet layer]
- TCP scan [Transport layer]
- UDP scan [Transport Layer]

1. ARP request
2. ARP response
3. 1
4. router
5. computer5
6. y

## Task 5
#### ARP scan 
- Should run in `sudo`.
- sudo nmap -PR -sn 192.168.14.184/24 [Performs an ARP Scan over the interface the ipaddress has route on]
- Need to be in the subnet. ie, `/24`.
- `arp-scan` is a tool that does the same thing as the commend mentioned in second point does. The following screenshot shows the impact in wireshark.
![image](https://github.com/user-attachments/assets/8c95cdc4-da43-48cd-9b9f-ca9abb542e73)

1. 3 [Because ARP can only work if we are on the same network. Other than computer1,  we have computer2, computer3, router - 3 Devices]
