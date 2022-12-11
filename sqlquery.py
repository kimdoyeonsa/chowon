
def createtbl():
    sql="""create table if not exists empleado(id integer primary key autoincrement not null, 
        nombre text not null, 
        dong_name text not null,
        edad integer not null, 
        salario text not null,
        inPutOutput text not null,
        pay text not null,
        regdate text default (strftime('%Y-%m-%d %H-%M-%S','now')) 
        )"""
    return sql
def update():
    sql="update empleado set nombre=?,dong_name=?,edad=?,salario=?,inPutOutput=?,pay=? where id=?"
    return sql
def insert():
    sql="""insert into empleado (id, nombre, dong_name, edad, salario, inPutOutput, pay) values (?, ?, ?, ?, ?, ?, ?)"""
    return sql
def deleteall():
    sql="delete from empleado"
    return sql
def delete():
    sql="delete from empleado where id=?"
    return sql
def selectall():
    sql="select * from empleado"
    return sql
def selectcount():
    sql="select count(*) from empleado"
    return sql
def selectid():
    sql="select * from empleado where id=?"
    return sql
def select():
    sql="select * from empleado order by id desc limit 15"
    return sql
def selectpage(keyfield,txt,currpage,perpage):
    sql=f"select * from empleado"
    if txt!="":
        sql+=" where "+keyfield+" like '%" + txt + "%'"
    sql+=f" order by regdate asc limit {(currpage-1)*perpage},{perpage} "
    return sql
def search(keyfield,txt):
    sql="select * from empleado where "+keyfield+" like '%" + txt + "%' order by id desc "
    return sql
def selectmax():
    sql="select ifnull(max(id),0) from empleado"
    return sql
def selectupdate(keyfield,txt,currpage,perpage):
    sql=f"select * from empleado"
    if txt!="":
        sql+=" where "+keyfield+" like '%" + txt + "%'"
    sql+=f" order by regdate desc limit {(currpage-1)*perpage},{perpage} "
    return sql
