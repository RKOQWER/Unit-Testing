from fixtures.mydb import MyDB
import pytest

@pytest.fixture(scope="module")

def cur():

    db=MyDB()
    conn=db.connect()
    curs=conn.cursor()
    yield curs

    curs.close()
    conn.close()

def test_jhon_id(cur):
    id=cur.execute("select id from employee_db where name='Jhon'")

    assert id==123

def test_tom_id(cur):
    id=cur.execute("select id from employee_db where name='Tom'")

    assert id==1234