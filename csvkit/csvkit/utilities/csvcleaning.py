import csv
from csvkit.cli import CSVKitUtility
import pandas as pd
import numpy as np
import warnings

class CSVCleaning(CSVKitUtility):
    description = "Automatic Data Cleaning"

    def add_arguments(self):
        self.argparser.add_argument(
            'inputfile', help ='Input CSV file'
        )
        self.argparser.add_argument(
            '-o','--outputfile', help ='Output CSV file'
        )

    def main(self):
        inputfile = self.args.inputfile
        outputfile = self.args.outputfile

        df = pd.read_csv(inputfile)
        warnings.filterwarnings("ignore", message="The default value of numeric_only")
       
        
        # 결측치 평균으로 채움 (NaN, Empty)
        df_cleaning = df.fillna(df.mean())

        # 이상치 식별 후 데이터 클리닝
        #df_cleaning = df_cleaning[(df_cleaning - df_cleaning.mean()).abs() < 3 * df_cleaning.std()]
        df_cleaning = df_cleaning[(df_cleaning - df_cleaning.mean(numeric_only=True)).abs() < 3 * df_cleaning.std(numeric_only=True)]
        
        #콘솔에서 outputfile이 지정되었다면 저장
        if outputfile:
            df_cleaning.to_csv(outputfile,index=False,encoding='utf-8-sig')
        else:
            print(df_cleaning)
def launch_new_instance():
    utility = CSVCleaning()
    utility.run()

if __name__ == '__main__':
    launch_new_instance()