#!/usr/bin/python

#usage:    main payment_service_client get_external_ids


import sys, os 

sys.path.append('/home/ad/client_search/app/searcher')
sys.path.append('/home/ad/client_search/app')
#print sys.path
import searcher
import app

if len(sys.argv) != 3:
    print '2 arguments are required, the client first and then the client method.' 
    exit()

CURRENT_DIRECTORY = os.getcwd()
TARGET_CLIENT = sys.argv[1]
TARGET_METHOD = sys.argv[2]

client_search_params = {'root_dir': CURRENT_DIRECTORY, 
                        'target_client': TARGET_CLIENT, 
                        'target_method' : TARGET_METHOD}
                               
services_to_search = searcher.new('ClientUsage', client_search_params).search()

service_search_params = {'services_to_search': services_to_search, 
                         'target_method' : TARGET_METHOD}
                         
search_results = app.new('SearchManager', service_search_params).initiate_search()


strformat ={
         "stop" : "\x1b[00m", #not a colour, must be at end of string
         
         #style
         "bold" : "1",
         "normal" : "2",
             
         #colour 
         "default":"",
         "blue":   "34m",
         "cyan":   "36m",
         "green":  "92m",
         "red":    '91m'
         }

def formatColour(string, colour='default', style='normal'):
    s = "\x1b[0"+strformat[style]+";"+strformat[colour]+string+strformat['stop']
    return s
    
    
for result in search_results:
    print formatColour('#############################################################################','green') 
    print result





