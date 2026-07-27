# PhoneNumber OSINT tool

Script to obtain basic OSINT information from one or several phone numbers.


## Features

- Returns:
	- number validity
	- local and international format
	- prefix and country code
	- country name and location
	- operator
	- line type
	- time zones
- Additionally (in a browser tab):
	- weather search for the area
	- operator search
	- Truecaller query


## Installation

1. Clone the repository and enter the folder:

```bash
git clone https://github.com/0xlibless/PhoneNumberInfo.git
cd PhoneNumberInfo
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

You can use the script interactively or via arguments.

### Interactive Mode

```bash
python main.py
```

The program will ask you to paste one or several numbers, for example:

```text
+123456789012, +123456789012
```

### Argument Mode

```bash
python main.py --numero "+123456789012"
```

With several numbers:

```bash
python main.py -n "+123456789012, +123456789012"
```

To prevent the browser from opening:

```bash
python main.py -n "+123456789012" --nobrowser
```
