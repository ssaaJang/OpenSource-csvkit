import csv
import matplotlib.pyplot as plt
import pandas as pd
from csvkit.cli import CSVKitUtility

class CSVVisual(CSVKitUtility):
    description = "Visualization"
    def add_arguments(self):
        self.argparser.add_argument(
            'inputfile', dest='inputfile',help="Input CSV file"
        )

        self.argparser.add_argument(
            '--x', dest='x_axis',help="X축 column name"
        )

        self.argparser.add_argument(
            '--y', dest='y_axis',help="y축 column name"
        )

    def main(self):
        inputfile = self.args.inputfile
        x_axis = self.args.x_axis
        y_axis = self.args.y_axis

        df = pd.read_csv(inputfile)

        # 시각화할 컬럼 이름
        ColName = [x_axis,y_axis]
        Col_data = df[ColName]

        x_data = Col_data[x_axis]
        y_data = Col_data[y_axis]

        plt.figure()
        df[ColName].plot()
        plt.title('Visualization')
        plt.xlabel(ColName[0])
        plt.ylabel(ColName[1])
        plt.show()
    
def launch_new_instance():
    utility = CSVVisual()
    utility.run()

if __name__ == '__main__':
    launch_new_instance()


