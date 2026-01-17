
# PhoneNumber info search

A basic script that combines multiple tools into one
- Google search
- Number Verification API (NEED APIKEY)
- TrueCaller (NEED A ACCOUNT)



## Requirements

The script need you to have this module installed:

```bash
$ pip install requests
```

And an account with: https://www.truecaller.com 
## TOKENS

The script also requires a apikey from "Number Verification API" in:

https://apilayer.com/marketplace/number_verification-api?utm_source=apilayermarketplace&utm_medium=featured

![alt apiscreenshot](https://github.com/0xlibless/NumberPhoneInfo/blob/main/screenshot.png?raw=true)

Also past the key in TOKEN:

```PYTHON
# Peticion
payload = {}
headers= {
  "apikey": TOKEN
}
response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
result = response.json()
```
## How it works?
- The script sends a request to TrueCaller, which returns a lot of information
- Then several Google Chrome windows will open where you will find the weather of the location of the phone number, results of the telephone service, and TrueCaller, which if available, shows us the name of the person who owns the number
