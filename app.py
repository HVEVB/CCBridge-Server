from flask import request, Flask
import json

app = Flask(__name__)
codedict = {}

@app.route('/fromcomputercraft', methods=["GET", "POST"])
def from_comp():
    code = request.form.get('code')
    content = request.form.get('cont')
    file = request.form.get('file')
    print(file)
    print(content)
    print(code)
    if not code == None and not content == None and not file == None:
        if code in codedict:
            codedict[code]['files'][file] = content
        else:
            codedict[code] = {'files': {}}
            codedict[code]['files'] = {file: content}
        print(codedict)
        codedict[code]['changedcc'] = False
        codedict[code]['changedvs'] = True
        return "OK"
    else:
        return "KO"

@app.route('/fromvscode', methods=["GET", "POST"])
def from_vscode():
    print(request.form)
    code = request.form.get('code')
    content = request.form.get('cont')
    file = request.form.get('file')
    print(file)
    print(content)
    print(code)
    if not code == None and not content == None and not file == None:
        if code in codedict:
            codedict[code]['files'][file] = content
        else:
            codedict[code] = {'files': {}}
            codedict[code]['files'] = {file: content}
        print(codedict)
        codedict[code]['changedcc'] = True
        codedict[code]['changedvs'] = False
        return "OK"
    else:
        return "KO"

@app.route('/tovscode')
def to_vscode():
    code = request.args.get('code')
    codedict[code]['changedvs'] = False
    return json.dumps(codedict[code])

@app.route('/checkcc')
def checkcc():
    code = request.args.get('code')
    if codedict[code]['changedcc']:
        return "true"
    else:
        return "false"

@app.route('/tocomputercraft')
def to_computercraft():
    code = request.args.get('code')
    codedict[code]['changedcc'] = False
    return json.dumps(codedict[code])


if __name__ == '__main__':
    app.run()