# Kali-Tool

Laboratorio de ciberseguridad desarrollado en **Kali Linux** enfocado en automatización de tareas

## Herramientas actuales

### Sub-Domain Hunter (OSINT)
Script de reconocimiento pasivo que busca subdominios en registros de certificados SSL públicos.
* **Uso:** `python3 scanners/subdomain_finder.py`

###  Security Log Analyzer (Defensa)
Analizador de logs que detecta patrones de ataques comunes como SQL Injection, XSS y Path Traversal en tiempo real.
* **Uso:** `python3 web_tools/log_analyzer.py`

---

## 🛠️ Configuración del entorno
Este proyecto utiliza un entorno virtual (`venv`) para gestionar dependencias de forma segura.

1. **Clonar y entrar:** `cd Kali-Tool`
2. **Activar venv:** `source venv/bin/activate`
3. **Instalar requisitos:** `pip install -r requirements.txt`
