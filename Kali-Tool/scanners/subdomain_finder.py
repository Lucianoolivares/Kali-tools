import requests
from colorama import Fore, Style

def buscar(dominio):
    print(f"\n{Fore.CYAN}[*] Investigando subdominios para: {dominio}...{Style.RESET_ALL}")
    # Usamos la API de crt.sh (Certificados SSL públicos)
    url = f"https://crt.sh/?q=%25.{dominio}&output=json"
    
    try:
        r = requests.get(url, timeout=20)
        data = r.json()
        subdominios = set()
        
        for entrada in data:
            nombres = entrada['name_value'].split('\n')
            for n in nombres:
                if "*" not in n: # Limpiamos comodines
                    subdominios.add(n.strip())
        
        for s in sorted(subdominios):
            print(f"{Fore.GREEN}[+] Encontrado: {s}{Style.RESET_ALL}")
            
        print(f"\n{Fore.YELLOW}[!] Éxito: {len(subdominios)} subdominios descubiertos.{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[-] Error en la conexión: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    objetivo = input("Escribe un dominio (ej: nasa.gov): ")
    buscar(objetivo)