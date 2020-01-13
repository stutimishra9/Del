#API-1->IP
#api1=http://127.0.0.1:8080/ip
import bottle
app=bottle.Bottle()
@app.route('/ip',method='GET')
def api_ip():
    import sqlite3
    con=sqlite3.connect('mydb.sqlite3')
    cur=con.cursor()
    cur.execute('SELECT IP FROM LOGDATA')
    result=cur.fetchall()
    result=[i[0] for i in result]
    D={k:v for k,v in enumerate(result)}
    return D
#API2-http://127.0.0.1:8080/emp
@ app.route('/emp',method='post')
def empdetails():
    details=bottle.request.params
    details=dict(details)
    return details
app.run()
