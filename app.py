import os
import random
import subprocess
from subprocess import PIPE

from flask import Flask, request
app = Flask(__name__)

@app.route('/file_bhej', methods=['GET'])
def file_utha(lang):
    codes = os.listdir("Codes/Wrong/{}".format(lang))
    script_file = codes[random.randint(0, len(codes)-1)]
    script = ""
    with open("Codes/Wrong/{}/{}".format(lang, script_file), 'r') as f:
        script = "".join(f.readlines())
    # Preprocess the script text as per html
    return script_file, script

@app.route('/check_kar', methods=['POST'])
def diff():
    data = request.get_json()
    lang, script_file, test_case = data['lang'], data['script_file'], data['test_case']
    if lang=="Python":
        correct_output = subprocess.run(['python3', './Codes/Correct/Python/'+script_file], \
            stdout=PIPE, input=test_case, encoding='ascii')
        wrong_output = subprocess.run(['python3', './Codes/Wrong/Python/'+script_file], \
            stdout=PIPE, input=test_case, encoding='ascii')
    elif lang=='CPP':
        correct_output = subprocess.run(['./Codes/Wrong/CPP/'+script_file.split('.')[0]], \
            stdout=PIPE, input=test_case, encoding='ascii')
        wrong_output = subprocess.run(['./Codes/Correct/CPP/'+script_file.split('.')[0]], \
            stdout=PIPE, input=test_case, encoding='ascii') 
    else:
        correct_output = subprocess.run(['java', script_file.split('.')[0], '-classpath' './Codes/Wrong/Java/'], \
            stdout=PIPE, input=test_case, encoding='ascii')
        wrong_output = subprocess.run(['java', script_file.split('.')[0], '-classpath ', './Codes/Correct/Java/'], \
            stdout=PIPE, input=test_case, encoding='ascii')

    return correct_output.stdout==wrong_output.stdout

if __name__=='__main__':
    app.run()
