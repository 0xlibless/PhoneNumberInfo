# PhoneNumber OSINT tool

Script para obtener informacion OSINT basica de uno o varios numeros de telefono.



## Caracteristicas

- Devuelve:
	- validez del numero
	- formato local e internacional
	- prefijo y codigo de pais
	- nombre del pais y ubicacion
	- operador
	- tipo de linea
	- zonas horarias
- Ademas de (en una pestaña de navegador):
	- busqueda de clima de la zona
	- busqueda del operador
	- consulta en Truecaller


## Instalacion

1. Clona el repositorio y entra a la carpeta:

```bash
git clone https://github.com/0xlibless/PhoneNumberInfo.git
cd PhoneNumberInfo
```

2. Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Puedes usar el script de forma interactiva o por argumentos.

### Modo interactivo

```bash
python main.py
```

El programa te pedira que pegues uno o varios numeros, por ejemplo:

```text
+123456789012, +123456789012
```

### Modo por argumento

```bash
python main.py --numero "+123456789012"
```

Con varios numeros:

```bash
python main.py -n "+123456789012, +123456789012"
```

Para evitar que se abra el navegador:

```bash
python main.py -n "+123456789012" --nobrowser
```