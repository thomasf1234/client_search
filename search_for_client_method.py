#!/usr/bin/python

#usage:    main payment_service_client get_external_ids


import sys, os 

if len(sys.argv) != 3:
    print '2 arguments are required, the client first and then the client method.' 
    exit()

HOME = os.getenv("HOME")
CURRENT_DIRECTORY = os.getcwd()
TARGET_CLIENT = sys.argv[1]
TARGET_METHOD = sys.argv[2]

#move the following into an initialiser, i.e. to append all paths to PYTHONPATH
sys.path.append(HOME+'/client_search/app/searcher')
sys.path.append(HOME+'/client_search/app')
#print sys.path
import searcher
import app

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





