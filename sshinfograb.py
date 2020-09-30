import paramiko
import time
from getpass import getpass


def send_cmd(conn,command):
    conn.send(command)
    
def get_output(conn):
    return conn.recv(65535).decode("utf-8")

def main():
    host_list = ["x.x.x.x"] #replace with ip
    passw = getpass()
    for host in host_list:
        conn_params = paramiko.SSHClient()
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting to " + host)
        conn_params.connect(
            hostname=host,
            port=22,
            username="xxxxxxxxxx", #replace with user
            password=passw,
            look_for_keys=False,
            allow_agent=False,
            )
        conn = conn_params.invoke_shell()
        time.sleep(1.0)
        print("Success!")
        commands = ["show inventory | include SN:"]
        for command in commands:
            output = conn.send(command+"\n")
            time.sleep(1.0)
            output = f"{get_output(conn)}"
            sn = output.split("SN: ") #more methods will be added. this one is also not finished.
            print(sn)
            conn.close()
            
main()
