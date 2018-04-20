import os
import socket

# deleting infected files
# you can modify this creating own quarantinate folder and storing all those infected files rather than deleting them

def delete(file_loc,threats_cleaned):
    try:
        if os.path.isfile(file_loc):
            os.remove(file_loc)
            # print(" %s is Deleted"% filename)
            threats_cleaned += 1
            return threats_cleaned
    except PermissionError:
        threats_cleaned +=0
        return threats_cleaned
    except:
        threats_cleaned += 0
        return threats_cleaned
