from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'count' and 'count2' and 'count3' and 'count4' and 'count5' and 'count6' and 'count7' and 'count8' not in session:
        session['count'] = 0
        session['count2'] = 0
        session['count3'] = 0
        session['count4'] = 0
        session['count5'] = 0
        session['count6'] = 0
        session['count7'] = 0
        session['count8'] = 0

    percentage = {'1': 0, '2': 200}
    percentage2 = {'1': 0, '2': 100}
    percentage3 = {'1': 0, '2': 300}
    percentage4 = {'1': 0, '2': 400}
    percentage5 = {'1': 0, '2': 500}
    percentage6 = {'1': 0, '2': 600}
    percentage7 = {'1': 0, '2': 700}
    percentage8 = {'1': 0, '2': 800}
    if session['count'] > 0:
        percentage['1'] = session['count'] * 1
        percentage['2'] = 200 - percentage['1']

    if session['count2'] > 0:
        percentage2['1'] = session['count2'] * 1
        percentage2['2'] = 100 - percentage2['1']

    if session['count3'] > 0:
        percentage3['1'] = session['count3'] * 1
        percentage3['2'] = 300 - percentage3['1']

    if session['count4'] > 0:
        percentage4['1'] = session['count4'] * 1
        percentage4['2'] = 400 - percentage4['1']

    if session['count5'] > 0:
        percentage5['1'] = session['count5'] * 1
        percentage5['2'] = 500 - percentage5['1']

    if session['count6'] > 0:
        percentage6['1'] = session['count6'] * 1
        percentage6['2'] = 600 - percentage6['1']

    if session['count7'] > 0:
        percentage7['1'] = session['count7'] * 1
        percentage7['2'] = 700 - percentage7['1']

    if session['count8'] > 0:
        percentage8['1'] = session['count8'] * 1
        percentage8['2'] = 800 - percentage8['1']

    if request.method == 'POST':
        if request.form['action'] == 'elec':
            session['count'] += 1
            percentage['1'] = session['count'] * 1
            percentage['2'] = 200 - percentage['1']
            session['count2'] += 1
            percentage2['1'] = session['count2'] * 1
            percentage2['2'] = 100 - percentage2['1']

        elif request.form['action'] == 'soft':
            session['count'] += 1
            percentage['1'] = session['count'] * 1
            percentage['2'] = 200 - percentage['1']
            session['count3'] += 1
            percentage3['1'] = session['count3'] * 1
            percentage3['2'] = 300 - percentage3['1']

        elif request.form['action'] == 'nerd':
            session['count'] += 1
            percentage['1'] = session['count'] * 1
            percentage['2'] = 200 - percentage['1']
            session['count4'] += 1
            percentage4['1'] = session['count4'] * 1
            percentage4['2'] = 400 - percentage4['1']

        elif request.form['action'] == 'math':
            session['count'] += 1
            percentage['1'] = session['count'] * 1
            percentage['2'] = 200 - percentage['1']
            session['count5'] += 1
            percentage5['1'] = session['count5'] * 1
            percentage5['2'] = 500 - percentage5['1']

        elif request.form['action'] == 'inmun':
            session['count'] += 1
            percentage['1'] = session['count'] * 1
            percentage['2'] = 200 - percentage['1']
            session['count6'] += 1
            percentage6['1'] = session['count6'] * 1
            percentage6['2'] = 600 - percentage6['1']

        elif request.form['action'] == 'law':
            session['count'] += 1
            percentage['1'] = session['count'] * 1
            percentage['2'] = 200 - percentage['1']
            session['count7'] += 1
            percentage7['1'] = session['count7'] * 1
            percentage7['2'] = 700 - percentage7['1']

        elif request.form['action'] == 'coin':
            session['count'] += 1
            percentage['1'] = session['count'] * 1
            percentage['2'] = 200 - percentage['1']
            session['count8'] += 1
            percentage8['1'] = session['count8'] * 1
            percentage8['2'] = 800 - percentage8['1']

        elif request.form['action'] == 'reset':
            session['count'] = 0
            percentage['1'] = 0
            percentage['2'] = 200
            session['count2'] = 0
            percentage2['1'] = 0
            percentage2['2'] = 100
            session['count3'] = 0
            percentage3['1'] = 0
            percentage3['2'] = 300
            session['count4'] = 0
            percentage4['1'] = 0
            percentage4['2'] = 400
            session['count5'] = 0
            percentage5['1'] = 0
            percentage5['2'] = 500
            session['count6'] = 0
            percentage6['1'] = 0
            percentage6['2'] = 600
            session['count7'] = 0
            percentage7['1'] = 0
            percentage7['2'] = 700
            session['count8'] = 0
            percentage8['1'] = 0
            percentage8['2'] = 800

    return render_template('basic.html', percentage=percentage, percentage2=percentage2, percentage3=percentage3, percentage4=percentage4, percentage5=percentage5, percentage6=percentage6, percentage7=percentage7, percentage8=percentage8, per=round(session['count']/200*100, 2), per2=round(session['count2']/100*100, 2), per3=round(session['count3']/300*100, 2), per4=round(session['count4']/400*100, 2), per5=round(session['count5']/500*100, 2),per6=round(session['count6']/600*100, 2), per7=round(session['count7']/700*100, 2), per8=round(session['count8']/800*100, 2))

if __name__ == '__main__':
    app.run(debug=True)
