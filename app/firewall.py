import socket
from app.ai_detector import is_threat

def scan_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        is_malicious = is_threat(ip_address)
        return {
            "ip": ip_address,
            "status": "threat" if is_malicious else "safe"
        }
    except socket.error:
        return {
            "ip": ip_address,
            "status": "invalid"
        }
