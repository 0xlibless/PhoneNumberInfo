import requests
import time 
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("""
Phone number info
Press any key to continue
""")
input("")

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

print("Formato: +123456789012")
numero = input("Inserte el numero aqui: ")
url = f"https://api.apilayer.com/number_verification/validate?number={numero}"

# Peticion
payload = {}
headers= {
  "apikey": TOKEN
}
response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
result = response.json()

# Imprime todos los valores del resultado
for item, value in result.items():
    print(f"{item}: {str(value)}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Abriendo pestañas en chrome")
time.sleep(2)

# Valor ubicacion
pais = result["country_name"].replace(" ", "+")
pais2 = result["country_code"]
ubicacion = result["location"].replace(" ", "+")
servicio = result["carrier"].replace(" ", "+")
busqueda = f"{ubicacion}+{pais}" 

# Chrome
os.system(f"google-chrome --new-tab https://www.google.com/search?q={busqueda}+weather --new-tab https://www.google.com/search?q={servicio} --new-tab https://www.truecaller.com/search/{pais2}/{numero}")
