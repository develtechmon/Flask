from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

class elastic:
    
    def __init__(self):
        self.cert = "d05aaa8eba62fbb871cd966a29d0a9ba3336e29fbb6463deab015c1d985a246e"
        self.pwd  = "Eldernangkai92"
        
    def connect(self):
        self.es = Elasticsearch(
            "https://localhost:9200",
            ssl_assert_fingerprint=self.cert,
            basic_auth=("elastic", self.pwd)  
        )
        if self.es.ping(): print("Connected to server")  
        else: print("Failed to connect")
        
    def search(self,data):
        resp = self.es.search(
        index = "hotlinefaq",
        body={     
            "query": {
            "multi_match": {
            "query": data,
            "fields": ["Process", "Customer", "Subject", "Description", "Topic"],
            "operator": "or",
            "type": "cross_fields"
            },
        },    
        })
        
        return (resp)
        
    
if __name__ == "__main__":
    init = elastic()
    init.connect()
    
    resp = init.search('"XR013", "IO"')
    print(resp)