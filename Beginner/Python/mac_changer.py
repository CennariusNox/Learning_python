import re
import subprocess
import argparse

# Función para obtener los argumentos
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interfaz para cambiar la dirección MAC")
    parser.add_argument("-m", "--MAC", dest="new_mac", help="Introducir la dirección MAC")
    return parser.parse_args()

# Función para cambiar la MAC
def change_mac(interface, new_mac):
    print("[+] Cambiando direccion MAC para la interfaz " + interface + " a " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Función para obtener la MAC actual
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] No pudimos leer la direccion MAC")

options = get_arguments()

# Verificar si se proporcionaron los argumentos y mostrar mensajes de error
if not options.interface:
    print("[-] Por favor indique una interfaz, puede utilizar --help para más información")
elif not options.new_mac:
    print("[-] Por favor indique una MAC, puede utilizar --help para más información")
else:
    current_mac = get_current_mac(options.interface)
    print("Current MAC = " + str(current_mac)

    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] MAC cambiada correctamente a " + current_mac)
    else:
        print("[-] Error: La dirección MAC no cambió correctamente")
