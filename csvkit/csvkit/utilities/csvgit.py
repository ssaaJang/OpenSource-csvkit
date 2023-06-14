import csv
from github import Github

#from csvkit import CSVKitReader
from csvkit.cli import CSVKitUtility


class CSVGit(CSVKitUtility):
    description = 'Upload CSV files to Github'
    
    def add_arguments(self):
        self.argparser.add_argument(
            'inputfile', help='Input CSV File'
        )
        self.argparser.add_argument(
            '-re','--repo',help = 'Repository Name'
        )
        self.argparser.add_argument(
            '-to','--token', help = 'Input your Github Token'
        )

    def main(self):
        inputfile = self.args.inputfile
        repository = self.args.repo
        token = self.args.token

        gg = Github(token)
        repo = gg.get_repo(repository)
        '''
        with open(inputfile,'r') as f:
            ff = f.read()
        repo.upload_file(inputfile, 'Upload CSV files to Github', ff , branch ='main')
        '''
        with open(inputfile,'r') as f:
            content = f.read()
        repo.create_file(inputfile,'Upload CSV file',content,branch='main')        
        
        print(f'"{inputfile}" uploaded to GitHub')

def launch_new_instance():
    utility = CSVGit()
    utility.run()


if __name__ == '__main__':
    launch_new_instance()






        
         