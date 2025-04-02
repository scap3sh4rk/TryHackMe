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
#### TCP SYN Ping [-PS] 
- Use either `sS` or `-PS`, Here there is a catch, `sS` is a TCP port scan technique and `-PS` is a TCP ping scan technique. Need previliged account
![image](https://github.com/user-attachments/assets/b7665a28-1bb5-492a-af05-b3ba6a0dadb4)
- Default if we use `-PS` the scanned port is `80` on the target machine.
- If we want to specify the port you can go with `-PS443,12,11` so on.
- Remember these are a `host discovery` techniques.
- The flag starting from `P` => Its a ping (Assumption).
- Technically any service running on the specific ports are expected to `reply` to the TCP SYN message.

#### TCP ACK ping [-PA]
- `TCP` packet with the `ACK` flag set is sent. Requires a Previliged account
- Port mentioning is as same as the before case `-PA21,22,12` and so on.
- Expects a `RST` flag set TCP response accepting that the Host is UP.

#### UDP Ping [-PU]
- `UDP` Packet sent to a port is not expected to get any replay because `UDP` Never bother about the end user recieveing the packet.
- If the host is up, UDP doesn't probably send any packet, but if its down, `Host UNreachable` Message is sent back accepting the exsistance of the device.

#### Answers
1. TCP SYN Ping
2. TCP ACK ping
3. -PS23

## Task 8 Reverse DNS lookup
- `-n` flag to not to perform reverse DNS lookup. Because Nmap by default does this for the hosts that are online.
- If you want to perform the `DNS lookup` for all the devices (Including offline), you can go with the flag `-R`.

#### Answers
1. -R

## Summary
- Remember any response from the target indicated that the host is `Online`
- Remember that this is `host discovery` which is generally different from `Port scanning`
- If you were only intersted in the `host discovery` Remmeber to add `-sn` or Nmap will proceed with port scan of 1st `1000` ports on the targets that are discovered.
![image](https://github.com/user-attachments/assets/e01e071b-f17c-408a-9d4e-f1fbb1bb7cc5)
![image](https://github.com/user-attachments/assets/890b00f2-61ae-4aaa-9fcb-51ef33c82514)
