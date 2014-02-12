import os, sys

def new(class_name, params):       
    module_to_call = map_to_module[_pascalcase_to_underscorecase(class_name)]
    return getattr(module_to_call, class_name)(params)

#__private__
def __init__():
    _map_to_module_setter(map_to_module) 

def _file_names():
    this_module_directory_path = _directory_path(_this_module.__file__)
    file_names = os.listdir(this_module_directory_path)
    file_names.remove('__init__.py')
    return file_names
  
def _module_names(file_names):
    module_names = []
    for e in _file_names():
        if e[-3:] == '.py':
            module_names.append(e[:-3])
    return module_names
            
def _modules(module_names):
    return map(__import__, module_names )    

def _map_to_module_setter(map_to_module):
    module_names = _module_names(_file_names())
    modules = _modules(module_names)
    _this_module.map_to_module = dict(zip( module_names, modules ))
   
def _pascalcase_to_underscorecase(string):
     s='' 
     for char in string: 
         if char.isupper(): 
             s +='_'
         s += char
     return s.lower()[1:]
     
def _directory_path(file_path):  
    i = 0
    for char in reversed(file_path):
        i+=1
        if char == '/':
            return file_path[:-i]
  
           
 
_this_module = sys.modules[__name__]
map_to_module = None  #make private and try to pass by reference
__init__()           
          
            
