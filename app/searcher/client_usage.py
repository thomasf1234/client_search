import os, subprocess

#params = {'root_dir': '/home/ad/workspace', 'target_client': 'payment_service_client'}
#usage ClientUsage(params).search()    
class ClientUsage():
    def __init__(self, params):
        self.root_dir = params['root_dir']
        self.target_client = params['target_client'] 
        #put in exception raising for invalid directory 
                                                
    def search(self):
        unfiltered_sample = os.listdir(self.root_dir)
        filtered_sample = self.filter_by_gemfile(unfiltered_sample)
        final_sample = self.filter_by_target(filtered_sample)  
        return final_sample 
                  
    def filter_by_gemfile(self, unfiltered_sample):
        filtered_sample = []
        for directory in unfiltered_sample:
            gemfile_path = '%s/%s/Gemfile' % (self.root_dir, directory)
            if os.path.exists(gemfile_path):
                filtered_sample.append(directory)
        return filtered_sample  
               
    def filter_by_target(self, filtered_sample):
        final_sample = []
        for directory in filtered_sample:
            if self.contains_target(directory) == True:
                final_sample.append(directory)
        return final_sample  
                                      
    def contains_target(self, directory):
        grep_cmd = 'grep -i %s %s/%s/Gemfile' % (self.target_client, self.root_dir, directory)
        try:
            self.result = subprocess.check_output(grep_cmd, shell=True)
        except subprocess.CalledProcessError, e:
            if e.returncode == 1:
                self.result = ''
            else:
                raise e           
        if len(self.result) != 0: 
            return True
                
