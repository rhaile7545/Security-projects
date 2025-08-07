import socket

def port_scan(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            print(f"[+] Port {port} is open")
        except:
            pass
        finally:
            sock.close()

if __name__ == "__main__":
    port_scan("127.0.0.1", range(20, 1025))
