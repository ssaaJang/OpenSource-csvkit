import csv
import requests
import openai
from csvkit.cli import CSVKitUtility

openai.api_key = "insert OpenAPI Key"

messages = []
def GPT(input_text):
        user_content = input_text
        messages.append({"role": "user", "content": f"{user_content}"})

        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        assistant_content = completion.choices[0].message["content"].strip() # chatGPT 에게 받은 대답

        messages.append({"role": "assistant", "content": f"{assistant_content}"})

class CSVGPT(CSVKitUtility):
    description = " If you have any questions about the data, ask the chatbot."
    
    def add_arguments(self):
        self.argparser.add_argument(
            'inputfile' , dest='inputfile',help = 'Input CSV File'
        )

    def main(self):
        inputfile = self.args.inputfile

        with open(inputfile,'r') as f:
            r = csv.reader(f)
            lines = [next(r) for _ in range(6)]
        for line in lines:
            print(line)
        
        #데이터를 GPT 에 먼저 넣어서 기억하도록 하기
        GPT(lines)
        

        while True:
            user_content = input("user : ")
            if user_content == 'q':
                break
            GPT(user_content)
        print('answer : ', messages)
    
def launch_new_instance():
    utility = CSVGPT()
    utility.run()


if __name__ == '__main__':
    launch_new_instance()



            



