import requests
import json
from config import api_key

# <----API for VirusTotal report by md5 hash------->

class Virustotal():
	def __init__(self):
		self.host = "www.virustotal.com"
		self.base = "https://www.virustotal.com/vtapi/v2/"
		self.apikey = api_key

	def rscReport(self, rsc):
		base = self.base + 'file/report'
		parameters = {"resource":rsc, "apikey":self.apikey}
		r = requests.post(base, data=parameters)
		resp = r.json()
		results = parse_response(resp)
		return results

def parse_response(resp):
	buf = {}
	for item in resp:
		buf[item] = resp[item]
	return buf
