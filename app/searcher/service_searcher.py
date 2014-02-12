import subprocess
    
class ServiceSearcher():
    def __init__(self, params, excluded_dirs=['log','vendor','tmp','db','bin','spec','cache','doc','public','git']):
        self.service = params['service']
        self.target_method = params['target_method']
        self.excluded_dirs = excluded_dirs
                      
    def search(self):
        grep_cmd = 'grep %s --color=always -ir %s %s/' % (self.formatted_excluded_dirs(), self.target_method, self.service)
        print grep_cmd       
        try:
            self.result = subprocess.check_output(grep_cmd, shell=True) #try to bypass this by filtering the directories to search before hand
        except subprocess.CalledProcessError, e:
            if e.returncode == 1:
                self.result = ''
            else:
                raise e    
        return self.result
        
    def formatted_excluded_dirs(self):
        cmd = ''
        base_cmd = '--exclude-dir='
        for dir in self.excluded_dirs:
            cmd += base_cmd+dir+' '
        return cmd  
        
