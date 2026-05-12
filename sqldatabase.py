from sqlalchemy import *
from sqlalchemy.orm import * 

engine = create_engine('sqlite:///univ.db',echo=True)
base = declarative_base()

class Dept(base):
    def __init__(self,deptno,dname):
        self.deptno = deptno
        self.dname = dname
    __tablename__ = "dept"
    deptno = Column(Integer, primary_key = True)
    dname = Column(String(50))


base.metadata.create_all(engine)


