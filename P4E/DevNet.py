from scapy.all import ARP, Ether, srp
import socket

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def scan_network(ip_range):
    # Create an ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and receive responses
    result = srp(packet, timeout=2, verbose=False)[0]

    # Parse the responses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    try:
        local_ip = get_local_ip()
        ip_range = local_ip.rsplit('.', 1)[0] + '.1/24'
        devices = scan_network(ip_range)

        print("Devices on the network:")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    except Exception as e:
        print(f"An error occurred: {e}")