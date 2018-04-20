import requests
import json

class Virustotal():
	def __init__(self):
		self.host = "www.virustotal.com"
		self.base = "https://www.virustotal.com/vtapi/v2/"
		self.apikey = "0773f9eab42b642539f2b753fbd77e86b63445a507c6584f1bbb5194a06ccd86"

	def rscReport(self, rsc):
		base = self.base + 'file/report'
		parameters = {"resource":rsc, "apikey":self.apikey}
		r = requests.post(base, data=parameters)
		resp = r.json()
		results = parse_resp(resp)
		return results

def parse_resp(resp):
	buf = {}
	for item in resp:
		buf[item] = resp[item]

	return buf
