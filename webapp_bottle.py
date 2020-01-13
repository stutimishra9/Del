import bottle
#how to create website
app=bottle.Bottle()
#app.run()
@app.error(404)
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
@app.route('/verify',method='post')
def verifypage():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not(u=='abc' and p=='xyz'):
        return 'LOGIN FAILED'
    else:
        #return 'LOGIN SUCCESS'
        bottle.TEMPLATE_PATH.append(r'C:\pytraining\bin')
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result=cur.fetchall()
        return bottle.template('report.tpl',res=result)
@app.route('/download/<filename>')
def staticfile(filename):
    return bottle.static_file(root=r'C:\Python Training\bin',filename=filename)
@app.route('/empid/<eid:int>')
def empid(eid):
    D={'name':'abc','EMP_ID':eid}
    return D
@app.route('/nameid/<nid:re:[a-z0-9]+>')
def nameid(nid):
    return str(nid)
@app.route('/logdata')
def logdata():
    return bottle.redirect('/login')
@app.route('/passwords')
def passwords():
    return bottle.abort(201,'AccessDenied')
app.run(host='192.168.3.253',port=8080)