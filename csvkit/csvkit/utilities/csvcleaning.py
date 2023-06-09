import csv
from csvkit.cli import CSVKitUtility
import pandas as pd

class CSVCleaning(CSVKitUtility):
    description = "Automatic Data Cleaning"

    def add_arguments(self):
        self.argparser.add_argument(
            'inputfile', dest ='inputfile', help ='Input CSV file'
        )
        self.argparser.add_argument(
            '--o','--outputfile', dest='outputfile', help ='Output CSV file'
        )

    def main(self):
        inputfile = self.args.inputfile
        outputfile = self.args.outputfile

        df = pd.read_csv(inputfile)

        # 결측치 평균으로 채움 (NaN, Empty)
        df_cleaning = df.fillna(df.mean())

        # 이상치 식별 후 데이터 클리닝
        df_cleaning = df_cleaning[(df_cleaning - df_cleaning.mean()).abs() < 3 * df_cleaning.std()]

        #콘솔에서 outputfile이 지정되었다면 저장
        if outputfile:
            df_cleaning.to_csv(outputfile,index=False)
        else:
            print(df_cleaning)
def launch_new_instance():
    utility = CSVCleaning()
    utility.run()

if __name__ == '__main__':
    launch_new_instance()