from support.api import *
import time

def connect(hash):
    try:
        v = Virustotal()
        results = v.rscReport(hash)
        return results["positives"]/results["total"]*100
    except KeyError:
        return 0
    except json.decoder.JSONDecodeError:
        time.sleep(60)
        return connect(hash)
