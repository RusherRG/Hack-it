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
    correct_output = run_code('Correct', lang, script_file, test_case)
    wrong_output = run_code('Wrong', lang, script_file, test_case)
    return {
        'answer': correct_output==wrong_output
    }

@app.route('/output_de', methods=['GET'])
def get_output():
    data = request.get_json()
    lang, script_file, test_case = data['lang'], data['script_file'], data['test_case']
    try:
        output = run_code('Wrong', lang, script_file, test_case)
        return {
            'output': output,
            'status': 'Success'
        }
    except:
        return {'status': 'Failed'}
    
def run_code(code_type, lang, script_file, test_case):
    if lang=='Python':
        output = subprocess.run(['python3', './Codes/{}/{}/{}'.format(code_type, lang, script_file)], \
            stdout=PIPE, input=test_case, encoding='ascii')
    elif lang=='CPP':
        output = subprocess.run(['./Codes/{}/{}/{}'.format(code_type, lang, script_file.split('.')[0])], \
            stdout=PIPE, input=test_case, encoding='ascii')
    else:
        output = subprocess.run(['java', '-cp', './Codes/{}/{}'.format(code_type, lang), script_file.split('.')[0]], \
            stdout=PIPE, input=test_case, encoding='ascii')
    return output.stdout

if __name__=='__main__':
    app.run()
