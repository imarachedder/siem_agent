# agent/utils/helpers.py
import socket

def get_hostname_from_ip(ip):
    """
    Попытка получить хостнейм по IP через обратный DNS-запрос.
    """
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return None