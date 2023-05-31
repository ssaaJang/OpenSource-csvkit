import csv
from github import Github

from csvkit import CSVKitReader
from csvkit.cli import CSVKitUtility

class CSVGit(CSVKitUtility):
    description = 'Upload CSV files to Github'
    

    def add_arguments(self):
        self.argparser.add_argument(
            'inputfile', dest='inputfile', help='Input CSV File'
        )
        self.argparser.add_argument(
            '-re','--repo',dest='repo',help = 'Repository Name'
        )
        self.argparser.add_argument(
            '-to','--token', dest='token', help = 'Input your Github Token'
        )

    def mian(self):
        inputfile = self.args.inputfile
        repository = self.args.repo
        token = self.args.token
        
         