from fixtures.mydb import MyDB

def test_jhon_id():
    db=MyDB()
    conn=db.connect("server")
    cur=conn.cursor()
    id=cur.execute("select id from employee_db where name='Jhon'")

    assert id==123


def test_tom_id():

    db=MyDB()
    conn=db.connect("server")
    cur=conn.cursor()
    id=cur.execute("select id from employee_db where name='Tom'")

    assert id==1234

