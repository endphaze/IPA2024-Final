from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.181"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}

#exam output GigabitEthernet1 up, GigabitEthernet2 up, GigabitEthernet3 down, GigabitEthernet4 administratively down -> 2 up, 1 down, 1 administratively down
def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("sh ip int br", use_textfsm=True)
        
        for interface in result:
            # print(interface)
            int_name = interface["interface"]
            if int_name.startswith("GigabitEthernet") :
                status = interface["status"]
                if status == "up":
                    ans += f"{int_name} {status}"
                    up += 1
                elif status == "down":
                    ans += f"{int_name} {status}"
                    down += 1
                elif status == "administratively down":
                    ans += f"{int_name} {status}"
                    admin_down += 1
            else:
                break
            ans += ", "
        ans += f"-> {up} up, {down} down, {admin_down} administratively down"
        
    return ans

print(gigabit_status())