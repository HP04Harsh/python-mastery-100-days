from sqlalchemy import *
from sqlalchemy.orm import *
from sqldatabase import Dept


engine = create_engine('sqlite:///univ.db')
Session = sessionmaker(bind=engine)

session = Session()

dept = session.query(Dept).all()
for d in dept:
    print(d.deptno,d.dname)


print(dept)

session.commit()
session.close()