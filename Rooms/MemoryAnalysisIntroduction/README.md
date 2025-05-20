# Memory Analysis Introduction
- https://tryhackme.com/room/memoryanalysisintroduction

## Structure and Divisions of RAM
- Kernal space and User space
- Kernal space for Operating system processes
- User space for User specific processes.
- Each process will have its own memory Devided to 4 regions,
    - `Stack` - Basic temporary data
    - `Heap` - Dynamic memory
    - `Executable` - Executable code
    - `Data Sectors` - Global Variables
**Understanding this structure is important in identifying where forensic artifacts might be located. For instance, encryption keys are often found on the heap, while shell commands may be on the stack**

![image](https://github.com/user-attachments/assets/ac33f3ef-7e78-4366-bb53-ce9ce5cdeb53)

## RAM for Forensic Analysts
The analysis of RAM offers a snapshot of what a system is doing at a particular moment. This includes:

- Running processes and loaded executables
- Open network connections and ports
- Logged-in users and recent commands
- Decrypted content, including encryption keys
- Injected code or fileless malware

## Memory Dumps
Creating a memory dump depends on the operating system in use. The goal is to capture RAM content without significantly altering it during acquisition.

On Windows, tools like built-in crash dumps, Sysinternals’ RAMMap, or third-party utilities such as WinPmem and FTK Imager can be used to generate full or selective memory captures. Some methods include kernel mode dumps located at %SystemRoot%\MEMORY.DMP and hibernation files stored as %SystemDrive%\hiberfil.sys. We can find more about it in the Analysing Volatile Memory room.

On Linux and macOS, analysts can use tools like LiME (Linux Memory Extractor) or dd with access to /dev/mem or /proc/kcore, depending on kernel protections. These methods will be covered in more detail later in the room.

Tools like **Mimikatz** are often used by red teamers and attackers to extract credentials directly from memory, making memory dumps an important defensive focus.

```
# Kcore file
-r-------- 1 root root 128T May 20 09:53 kcore
```

## Types of Memory Dumps
- Full Memory Dump: Captures all RAM, including user and kernel space. Useful for complete forensic investigations and malware analysis.
- Process Dump: Captures the memory of a **single running process**. Helpful for reverse engineering or isolating malicious behavior within a specific application.
- Pagefile and Swap Analysis: Systems offload some memory content to disk when RAM is full. On Windows, this is stored in pagefile.sys, and on Linux, in the swap partition or swapfile. These can contain fragments of data that were once in RAM, offering additional context.

#### Task 3
1. Mimikatz
2. full
3. lime
4. hiberfil.sys
5. DKOM
