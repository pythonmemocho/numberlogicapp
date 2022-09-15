import random

from flask import Flask, render_template, request, redirect, url_for

from _python._class import Number, NumbersBord

app = Flask(__name__)

count = 31
n = bin(count)[2:]
nums_of_bords = len(str(n))

numbers = [Number(i,nums_of_bords) for i in range(1,count+1)]
bords = [NumbersBord(i, ind) for ind, i in enumerate(range(nums_of_bords))]

for num in numbers:
    for n in num.number_group:
        bords[n-1].insert_nums(num.number)

_round = None
ans_dict = None


@app.route('/')
def index():
    global _round, ans_dict
    _round = 0
    ans_dict = dict()
    random.shuffle(bords)
    print(ans_dict)
    return render_template('index.html')

@app.route('/choice/<int:key>')
def choice(key):
    bord = bords[_round]
    return render_template('choice.html',bord=bord)

@app.route('/strage', methods=['POST'])
def strage():
    global _round
    ans = request.form['selector']
    if _round < nums_of_bords - 1:
        ans_dict[bords[_round].bord_index] = ans
        _round += 1
        return redirect(url_for('choice',key=_round))
    else:
        ans_dict[bords[_round].bord_index] = ans
        return redirect(url_for('answer'))

@app.route('/answer')
def answer():
    your_number = check_answer(ans_dict)
    return render_template('answer.html',your_number=your_number)

def check_answer(d:dict):
    ans = list("0"*nums_of_bords)
    d = sorted(d.items(),key=lambda x:x[0])
    for ind, value in enumerate(d):
        if value[1] == 'yes':
            ans[ind] = "1"
    ans = int("".join(ans),2)
    return ans



if __name__ == '__main__':
    app.run(debug=False)

