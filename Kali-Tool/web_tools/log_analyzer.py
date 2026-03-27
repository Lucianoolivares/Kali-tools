import re
from colorama import Fore, Style

# Patrones de ataques comunes (SQL Injection, XSS, Path Traversal)
PATRONES_ATAQUE = {
    "SQL Injection": r"SELECT|UNION|INSERT|DELETE|DROP|--|OR 1=1",
    "XSS (Cross-Site Scripting)": r"<script>|alert\(|onerror=",
    "Path Traversal": r"\.\./\.\./|\.\.\\\.\.\\|etc/passwd",
    "Shell Shock / Command Injection": r"/bin/bash|/bin/sh|cat /etc/"
}

def analizar_log(linea):
    for ataque, patron in PATRONES_ATAQUE.items():
        if re.search(patron, linea, re.IGNORECASE):
            return ataque
    return None

def iniciar_monitoreo():
    print(f"{Fore.CYAN}[*] Analizador de Logs de Seguridad Iniciado...{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Monitoreando patrones de ataque conocidos...{Style.RESET_ALL}\n")
    
    # Simularemos la lectura de un log (puedes apuntarlo a un archivo real luego)
    logs_ejemplo = [
        '192.168.1.10 - - [20/Mar/2026] "GET /index.php?id=1 OR 1=1 HTTP/1.1" 200',
        '10.0.0.5 - - [20/Mar/2026] "GET /contact.html HTTP/1.1" 200',
        '172.16.0.45 - - [20/Mar/2026] "GET /admin/<script>alert(1)</script> HTTP/1.1" 403',
        '192.168.1.15 - - [20/Mar/2026] "GET /../../etc/passwd HTTP/1.1" 404'
    ]

    for linea in logs_ejemplo:
        resultado = analizar_log(linea)
        if resultado:
            print(f"{Fore.RED}[ALERTA] Ataque Detectado: {resultado}{Style.RESET_ALL}")
            print(f" > Línea sospechosa: {linea}\n")
        else:
            print(f"{Fore.GREEN}[OK] Tráfico normal: {linea[:50]}...{Style.RESET_ALL}")

if __name__ == "__main__":
    iniciar_monitoreo()