import os
import searcher
    
class SearchManager():
    
    def __init__(self, params):
        self.target_method = params['target_method']
        self.services_to_search = params['services_to_search']  
         
    def initiate_search(self):
        self.results = []
        for service in self.services_to_search:
            result = searcher.new('ServiceSearcher', {'service' : service, 'target_method' : self.target_method}).search()     
            self.results.append(result)
        return self.results
