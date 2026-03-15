import os
import time
import webbrowser
from urllib.parse import quote_plus
import argparse

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from phonenumbers.phonenumberutil import NumberParseException, PhoneNumberType, number_type


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def etiqueta_tipo_linea(valor):
    mapa = {
        PhoneNumberType.MOBILE: "mobile",
        PhoneNumberType.FIXED_LINE: "landline",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "fixed_line_or_mobile",
        PhoneNumberType.TOLL_FREE: "toll_free",
        PhoneNumberType.PREMIUM_RATE: "premium_rate",
        PhoneNumberType.SHARED_COST: "shared_cost",
        PhoneNumberType.VOIP: "voip",
        PhoneNumberType.PERSONAL_NUMBER: "personal_number",
        PhoneNumberType.PAGER: "paging",
        PhoneNumberType.UAN: "uan",
        PhoneNumberType.VOICEMAIL: "voicemail",
        PhoneNumberType.UNKNOWN: "unknown",
    }
    return mapa.get(valor, "unknown")


def obtener_info_telefono(numero_crudo):
    numero_parseado = phonenumbers.parse(numero_crudo, None)

    codigo_pais = phonenumbers.region_code_for_number(numero_parseado) or ""
    prefijo_pais = f"+{numero_parseado.country_code}" if numero_parseado.country_code else ""

    return {
        "valido": phonenumbers.is_valid_number(numero_parseado),
        "numero": str(numero_parseado.national_number),
        "formato_local": phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.NATIONAL),
        "formato_internacional": phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.E164),
        "prefijo_pais": prefijo_pais,
        "codigo_pais": codigo_pais,
        "nombre_pais": geocoder.country_name_for_number(numero_parseado, "es") or "N/A",
        "ubicacion": geocoder.description_for_number(numero_parseado, "es") or "N/A",
        "operador": carrier.name_for_number(numero_parseado, "es") or "N/A",
        "tipo_linea": etiqueta_tipo_linea(number_type(numero_parseado)),
        "zonas_horarias": ", ".join(timezone.time_zones_for_number(numero_parseado)) or "N/A",
    }


def main():
    clear()

    print("--------------------------------------------")
    print("Herramienta OSINT de numeros 2.0")
    print("Por 0xlibless")
    print("Remake")
    print("--------------------------------------------")

    parser = argparse.ArgumentParser(description="Herramienta OSINT de numeros 2.0")
    parser.add_argument("--numero", "-n", help="Numero/s de telefono", default="")
    parser.add_argument("--nobrowser", action="store_true", help="No abrir pestanas del navegador")
    args = parser.parse_args()

    if args.numero:
        numero_telefono = args.numero
    else:
        numero_telefono = input("Pega el/los numero/s aqui (formato: +123456789012, +123456789012): ").strip()

    numeros = [n.strip() for n in numero_telefono.split(",") if n.strip()]

    for numero in numeros:
        print(f"\n--- Analizando {numero} ---")

        try:
            resultado = obtener_info_telefono(numero)
        except NumberParseException as exc:
            print(f"Numero invalido: {exc}")
            continue

        print("\nInformacion:")
        for campo, valor in resultado.items():
            print(f"{campo}: {valor}")

        if not args.nobrowser:
            print("\nAbriendo pestanas del navegador...")
            time.sleep(1)

            consulta_clima = quote_plus(f"{resultado['ubicacion']} {resultado['nombre_pais']} clima")
            consulta_operador = quote_plus(resultado["operador"])
            numero_truecaller = resultado["formato_internacional"].replace("+", "")

            webbrowser.open_new_tab(f"https://www.google.com/search?q={consulta_clima}")
            webbrowser.open_new_tab(f"https://www.google.com/search?q={consulta_operador}")
            if resultado["codigo_pais"] and numero_truecaller:
                webbrowser.open_new_tab(
                    f"https://www.truecaller.com/search/{resultado['codigo_pais']}/{numero_truecaller}"
                )


if __name__ == "__main__":
    main()