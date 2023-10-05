from fixtures.mydb import MyDB

conn=None
cur=None

def setup_module(module):

    global conn
    global cur
    db=MyDB()
    conn=db.connect()

    cur=conn.cursor()

def teardown_module(module):
    cur.close()
    conn.close()

def test_jhon_id():
    id=cur.execute("select id from employee_db where name='Jhon'")

    assert id==123

def test_tom_id():
    id=cur.execute("select id from employee_db where name='Tom'")

    assert id==1234
