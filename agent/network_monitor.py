# agent/network_monitor.py
import psutil
import socket
from utils.helpers import get_hostname_from_ip

def monitor_connections():
    """
    Мониторит активные TCP соединения.
    Возвращает список кортежей (local_ip, remote_ip, remote_port)
    """
    connections = []
    for conn in psutil.net_connections():
        if conn.status == 'ESTABLISHED' and conn.type == socket.SOCK_STREAM:
            local_ip = conn.laddr.ip
            remote_ip = conn.raddr.ip if conn.raddr else None
            remote_port = conn.raddr.port if conn.raddr else None
            connections.append((local_ip, remote_ip, remote_port))
    return connections

def get_active_domains():
    """
    Получает список доменных имён из текущих подключений.
    """
    domains = set()
    for _, remote_ip, _ in monitor_connections():
        if remote_ip:
            try:
                domain = get_hostname_from_ip(remote_ip)
                if domain:
                    domains.add(domain)
            except Exception as e:
                continue
    return list(domains)