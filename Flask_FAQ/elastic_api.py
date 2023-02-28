from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

import json

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
        operator = []
        operator.append(data)
        
        print(data)
        for x in operator:
            y = x.split()
            
            if 'and:' in y:      
                y.remove('and:')
                print(y)
                
                for z in y:
                    print(z)

                    self.search_and(z)
            
            else:
                self.search_or(data)
            
        # print(data)
        # x = data.split()
        # for i in x:
        #     if 'and:' in i:
        #         x.remove('and:')
              
        #         print(x)
                #print(x[1:])
                #self.search_and(data)
                
    def search_or(self,data):
        # See Link https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/examples.html
        # See link https://dylancastillo.co/elasticsearch-python/
        print("OR")
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
                
        jsonString = json.dumps(resp['hits']['hits'])
        jsonFile = open("D:\Flask\Flask_FAQ\static\json\data.json","w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
    def search_and(self,data):
        print("AND")
        # See Link https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/examples.html
        # See link https://dylancastillo.co/elasticsearch-python/
        resp = self.es.search(
        index = "hotlinefaq",
        body={     
            "query": {
            "multi_match": {
            "query": data,
            "fields": ["Process", "Customer", "Subject", "Description", "Topic"],
            "operator": "and",
            "type": "cross_fields"
            },
        },    
        })
                
        jsonString = json.dumps(resp['hits']['hits'])
        jsonFile = open("D:\Flask_Tutorial\Flask_FAQ\static\json\data.json","w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
    def update(self,tic, pro, cus, sub, top, des, sup):
        # See Link https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/examples.html
        doc = {
            'Ticket' : tic,
            'Process' : pro,
            'Customer' : cus,
            'Subject' : sub,
            'Topic' : top,
            'Description' : des,
            'Support' : sup,
        }
        resp = self.es.update(index="hotlinefaq",id=127, doc=doc) 
        
    def add(self,tic, pro, cus, sub, top, des, sup):
        # See Link https://www.elastic.co/guide/en/cloud/current/ec-getting-started-python.html
        self.es.index(
            index = "hotlinefaq",
            document = {
            'Ticket' : tic,
            'Process' : pro,
            'Customer' : cus,
            'Subject' : sub,
            'Topic' : top,
            'Description' : des,
            'Support' : sup,
        }    
        )
            
    def all(self):
        resp = self.es.search(
            index = "hotlinefaq",
            body={
                "query": {
                    "match_all": {}
                }
            }
        )
               
        value = resp['hits']['total']['value']
        
        return value
    
    def refresh(self):
        self.es.indices.refresh(index="hotlinefaq")
        
if __name__ == "__main__":
    init = elastic()
    init.connect()
    
    #init.search('"XP018" "ESD"')
    
    #init.search_and("XR013")
    
    #init.update("00","xt018","lukas","esd","esd clamp","guideline","refer to guideline")
    
    #init.all()
    
    #init.add("00","xt018","james","esd","esd clamp","guideline","refer to guideline")

        
        
        