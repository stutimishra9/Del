import flask
#how to create website
app=flask.Flask('Myapp')
#app.run()
@app.errorhandler(404)
def errorpage(err):
    return 'Page Under Construction'
@app.route('/')
def indexpage():
    return 'Welcome'
@app.route('/about')
def aboutpage():
    return '<b>This is about</b>'
@app.route('/login')
def loginpage():
    return '''<form action='/verify' method='post'>
    USERNAME:<input type='text' name='uname'/></br>
    PASSWORD:<input type='password' name='pw'/></br>
    <input type='submit' value='LOGIN'/>
    </form>'''
@app.route('/verify',methods=['post'])
def verifypage():
    u=flask.request.form.get('uname')
    p=flask.request.form.get('pw')
    if not(u=='abc' and p=='xyz'):
        return 'LOGIN FAILED'
    else:
        #return 'LOGIN SUCCESS'
        #bottle.TEMPLATE_PATH.append(r'C:\pytraining\bin')
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result=cur.fetchall()
        return flask.render_template('report.html',res=result)
@app.route('/download/<filename>')
def staticfile(filename):
    return flask.send_from_directory(directory=r'C:\Python Training\bin',filename=filename)
@app.route('/empid/<int:eid>')
def empid(eid):
    D={'name':'abc','EMP_ID':eid}
    return D
#@app.route('/nameid/<nid:re:[a-z0-9]+>')
#def nameid(nid):
 #    return str(nid)
@app.route('/logdata')
def logdata():
    return flask.redirect('/login')
@app.route('/passwords')
def passwords():
    return flask.abort(201,'AccessDenied')
app.run(host='192.168.3.253',port=8080)