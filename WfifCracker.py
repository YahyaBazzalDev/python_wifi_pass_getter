import subprocess
NetInput = input("Enter the name of the network you want to crack: ")
if NetInput == "":
    print("Network not found")
    exit()
network_name = NetInput
result = subprocess.run(['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear'], stdout=subprocess.PIPE)
output = result.stdout.decode()
print(f"Network Info: {output}")
for line in output.split('\n'):
    if "Key Content" in line:
        print(f"The password is: {result.stdout.decode().split(':')[1].strip()}")
        print(line.split(":")[1].strip())