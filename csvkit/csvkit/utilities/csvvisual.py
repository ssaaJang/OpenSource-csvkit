import csv
import matplotlib.pyplot as plt
import pandas as pd
from csvkit.cli import CSVKitUtility
import matplotlib.font_manager as fm
font_path = 'C:/Windows/Fonts/malgun.ttf'
plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()


class CSVVisual(CSVKitUtility):
    description = "Visualization"
    def add_arguments(self):
        self.argparser.add_argument(
            'inputfile',help="Input CSV file"
        )

        self.argparser.add_argument(
            '--x_axis' ,help="X축 column name"
        )

        self.argparser.add_argument(
            '--y_axis',help="y축 column name"
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

        plt.plot(x_data,y_data)
        plt.title('Visualization')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.show()
    
def launch_new_instance():
    utility = CSVVisual()
    utility.run()

if __name__ == '__main__':
    launch_new_instance()


