import time
import random
import sys

# Colores ANSI para la terminal
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'

def typing_effect(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def fake_hack():
    print(f"{GREEN}INICIALIZANDO PROTOCOLO DE INFILTRACIÓN...{WHITE}")
    time.sleep(1)
    
    typing_effect(f"{BOLD}ESTABLECIENDO CONEXIÓN CON SERVIDOR PROXY: 192.168.{random.randint(1,255)}.{random.randint(1,255)}", 0.02)
    time.sleep(0.5)
    
    actions = [
        "Bypassing Firewall...",
        "Injecting SQL Database...",
        "Decrypting RSA 2048-bit key...",
        "Accessing Kernel Mainframe...",
        "Downloading encrypted_assets.zip...",
        "Clearing system logs..."
    ]

    for action in actions:
        print(f"{GREEN}[OK] {WHITE}{action}")
        time.sleep(random.uniform(0.3, 1.2))

    # Efecto de "Carga"
    print(f"{RED}SALTANDO SEGURIDAD BIOMÉTRICA:{WHITE}")
    for i in range(0, 101, 10):
        sys.stdout.write(f"\rProgreso: [{ '#' * (i//10) }{ ' ' * (10-i//10) }] {i}%")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")

    # Lluvia de datos (Estilo Matrix)
    typing_effect(f"{BOLD}{GREEN}ACCESO CONCEDIDO. EXTRRAYENDO DATOS...", 0.05)
    time.sleep(1)

    try:
        while True:
            data_line = "".join(random.choice("0123456789ABCDEF ") for _ in range(80))
            print(f"{GREEN}{data_line}{WHITE}")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print(f"\n{RED}[!] SESIÓN FINALIZADA POR EL USUARIO{WHITE}")

if __name__ == "__main__":
    fake_hack()