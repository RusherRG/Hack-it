import time
import os
import random
import subprocess
from subprocess import PIPE
from pymongo import MongoClient
mongodb_url = "mongodb://codecell:rush3rRg@ds333768.mlab.com:33768/crackathon"


from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
phase = "phase1"


def connect():
    client = MongoClient(mongodb_url)
    db = client.crackathon
    return db


def check_credentials(username, password):
    mega_db = connect().participants
    if mega_db.find_one({'username': username, 'password': password}):
        db = connect().round2
        user = db.find_one({'username': username, 'password': password})
        timer = time.time()
        print(user)
        if user:
            print(timer - user['time'] + 60*user['penalty'])
            return timer - user['time'] + 60*user['penalty']
        else:
            db.insert({'username': username, 'password': password, 'time': timer, 'penalty': 0})
            return 0
    return None


def run_code(q, lang, test_case, code_type):
    if lang in ['python', 'java']:
        output = subprocess.run(['python3', './Codes/{}/{}/{}.py'.format(phase, q, code_type)],
                                stdout=PIPE, input=test_case, encoding='ascii')
    elif lang == 'cpp':
        output = subprocess.run(['./Codes/{}/{}/{}'.format(phase, q, code_type)],
                                stdout=PIPE, input=test_case, encoding='ascii')
    else:
        output = ""
        return output
    return output.stdout


@app.route('/check_kar')
def diff():
    data = request.args.to_dict()
    print(data, "data")
    username = data['username']
    lang, q, test_case = data['lang'].strip(), data['q'].strip(), data['test_case']
    correct_output = run_code(q, lang, test_case, 'correct')
    wrong_output = run_code(q, lang, test_case, 'wrong')
    print(correct_output)
    print(wrong_output)
    if correct_output!=wrong_output:
        status = "green"
        message = "Yayayay!! You hacked it"
    else:
        db = connect().round2
        db.update_one({'username': username}, {'$inc': {'penalty': 1}})
        status = "red"
        message = ":/ Keep on trying or you'll be hacked"

    return jsonify({
        'status': status,
        'message': message
    })


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


@app.route('/',methods=['GET','POST'])
def index():
    try:
        data = request.args.to_dict()
        timer = check_credentials(data['username'], data['password'])
        print(timer)
        username = data['username']
        if timer!=None:
            data = {
                'username': username,
                'ps': [],
                'code': [],
                'lang': [],
                'timer': timer,
            }
            for i in range(3):
                with open('Codes/{}/Q{}/problem_statement.html'.format(phase, i)) as f:
                    ps = f.readlines()
                    ps = ' '.join(ps)
                with open('Codes/{}/Q{}/code.html'.format(phase, i)) as f:
                    code = f.readlines()
                    data['lang'].append(code[0])
                    code = ''.join(code[1:])
                data['ps'].append(ps)
                data['code'].append(code)
            print("start render")
            return render_template('index.html', data=data)
        else:
            return render_template('login.html')
    except Exception as e:
        print(e)
        return render_template('login.html')


@app.route('/bye')
def bye():
    data = request.args.to_dict()
    print(data)
    db = connect().round2
    username = data['username']
    del data['username']
    if data:
        db.update_one({'username': username}, {'$set': data}, upsert=True)
        return jsonify({'status': 'Success'})
    else:
        return jsonify({'status': 'Error'})


if __name__ == '__main__':
    app.run()
