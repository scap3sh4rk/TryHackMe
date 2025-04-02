# Nmap Live Host discovery
[![Nmap TryHackMe](https://github.com/user-attachments/assets/d0d66f73-0111-41fc-b80d-e70e8454aac2)](https://tryhackme.com/room/nmap01)

## Task 4 Discovering Live Hosts
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

## Task 5 Host Discovery using ARP
#### ARP scan 
- Should run in `sudo`.
- sudo nmap -PR -sn 192.168.14.184/24 [Performs an ARP Scan over the interface the ipaddress has route on]
- Need to be in the subnet. ie, `/24`.
- `arp-scan` is a tool that does the same thing as the commend mentioned in second point does. The following screenshot shows the impact in wireshark.
![image](https://github.com/user-attachments/assets/8c95cdc4-da43-48cd-9b9f-ca9abb542e73)

1. 3 [Because ARP can only work if we are on the same network. Other than computer1,  we have computer2, computer3, router - 3 Devices]

## Task 6 Host Discovery Using ICMP
#### ICMP echo request scan [Type-8 Echo Request] [Type-0 Echo Replay]
- Use `-PE` flag to scan using `ICMP echo request`. Also add `-sn` to avoid a port scan.
- If the scannig machine is on the same subnet, the wireshark will show the same response as showin in the previous task [ARP scan] because it decides that the hosts are up from the recived response and no need further scanning. To simulate this, try to perform a scan over the different subnetwork.
#### ICMP Timestamp Scan [Type-13 Timestamp Request] [Type-14 Timestamp replay]
- ICMP has echo request scan and similarly there is `ICMP timestam` scan because echo request are mostly blocked in the network.
- Use `-PP` flag to use this.
- The timestamp request is used to determine the current time on the remote host [Type 13].
![image](https://github.com/user-attachments/assets/c8aceba1-2893-4de9-aeb0-dc89bdfda11d)

#### ICMP Address Mask Request [Type-17 Address mask Request] [ Type-18 Address mask replay]
- Use the flag, `-PM` for `ICMP address mask` scan.
- `nmap -PM -sn MACHINE_IP/24`

#### Answers
1. -PP
2. -PM
3. -PE

## Task 7 Host Discovery Using TCP & UDP
