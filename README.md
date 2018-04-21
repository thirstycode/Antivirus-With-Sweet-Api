# Antivirus-With-API
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)
<br>
<br>
**Scans The Computer For Viruses With All Antivirus Software's Results**<br>
**Please Check Working OF  VirusTotal, You'll Get To Know What I'm Talking About**
<br>
### Installation:

```bash
1. git clone https://github.com/thirstycode/antivirus-with-sweet-api
2. cd antivirus-with-sweet-api
3. pip install -r requirements.txt
```
### Getting Your VirusTotal API Key:


* Register For VirusTotal (Free Account) From [Here :](https://www.virustotal.com/#/join-us).
* After registering login into it.
* Now go to 'Settings' . Or Just click [here !](https://www.virustotal.com/#/settings/profile).
* Goto ApiKey Section OR Just click [here !](https://www.virustotal.com/#/settings/apikey).
* Copy your API key and paste in config.py

#### Execute It:
```bash
1. python scan.py
```
## Disclaimer :
- Pro's :
  - This Antivirus Will Never Expire. 😃
  - It'll Always Be Updated Since VirustTotal Is Always Updated
  - It Can Detect All Malwares, Viruses, Trojans , everything 😃
- Con's :
  - BIG unfortunate update : VirusTotal API has been restricted to 5 back to back scans.
  - So I have added wait time of 60 seconds after every  5th file scanned.
  - I suggest you to use this script to scan for specific folders rather than to scanning whole computer as it'll take much time
- Get log reports is TODO in script.
- PS : I'm not responsible for any harm to your computer [<pre>¯\_(ツ)_/¯</pre>](https://github.com/thirstycode/antivirus-with-sweet-api) 😜
