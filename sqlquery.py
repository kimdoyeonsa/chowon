def pragma_on():
    sql="PRAGMA foreign_keys = ON"
    return sql
def createtbl():
    sql="""create table if not exists empleado(id integer primary key autoincrement not null, 
        nombre text not null, 
        dong_name text not null,
        edad integer not null, 
        regdate text default (strftime('%Y-%m-%d %H-%M-%S','now')) 
        )"""
    return sql
def sal_createtbl():
    sql="""create table if not exists sal_emple(id integer primary key autoincrement not null,
        sal_id integer not null,
        salario text,
        inPutOutput text not null,
        pay text not null,
        sal_regdate text default (strftime('%Y-%m-%d %H-%M-%S','now')),
        enddate text,
        CONSTRAINT sal_emple_fk FOREIGN KEY(sal_id) REFERENCES empleado(id) ON DELETE CASCADE ON UPDATE CASCADE
        )"""
    return sql
# def sal_foriegn():
#     sql="ALTER TABLE sal_emple ADD CONSTRAINT sal_emple_fk FOREIGN KEY(sal_id) REFERENCES empleado(id) ON DELETE CASCADE ON UPDATE NO ACTION"
#     return sql
def update():
    sql="update empleado set nombre=?,dong_name=?,edad=? where id=?"
    return sql
def sal_update():
    sql="update sal_emple set salario=?,inPutOutput=?,pay=? where id=?"
    return sql

def insert():
    sql="""insert into empleado (id, nombre, dong_name, edad) values (?, ?, ?, ?)"""
    return sql
def sal_insert():
    sql="""insert into sal_emple (id, sal_id, salario, inPutOutput,pay) values (?, ?, ?, ?,?)"""
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
def selectpage(keyfield,txt,currpage,perpage,orderby):
    sql=f"select * from empleado"
    if txt!="":
        sql+=" where "+keyfield+" like \"%" + txt + "%\""
    sql+=f" order by regdate {orderby} limit {(currpage-1)*perpage},{perpage} "
    return sql
def search(keyfield,txt):
    sql="select * from empleado where "+keyfield+" like '%" + txt + "%' order by id desc "
    return sql
def selectmax(tbl):
    sql=f"select ifnull(max(id),0) from {tbl}"
    return sql
def selectupdate(keyfield,txt,currpage,perpage):
    sql=f"select * from empleado"
    if txt!="":
        sql+=" where "+keyfield+" like '%" + txt + "%'"
    sql+=f" order by regdate desc limit {(currpage-1)*perpage},{perpage} "
    return sql
def selectuser(nombre,edad):
    sql=f"select * from empleado where nombre='{nombre}' and edad='{edad}'"
    return sql
def selectusercnt(nombre,edad):
    sql=f"select count(*) from empleado where nombre='{nombre}' and edad='{edad}'"
    return sql
def sal_emple_i_w(id):
    sql=f"select sal_e.id,sal_e.salario,sal_e.inPutOutput,sal_e.pay,sal_e.sal_regdate,sal_e.enddate from empleado as e inner join sal_emple as sal_e on e.id=sal_e.sal_id where sal_e.sal_id={id}"
    return sql
def sal_emple_i_w_p(currpage,perpage):
    sql=f"select sal_e.id,sal_e.salario,sal_e.inPutOutput,sal_e.pay,sal_e.sal_regdate,sal_e.enddate from empleado as e inner join sal_emple as sal_e on e.id=sal_e.sal_id where sal_e.sal_id=? limit {(currpage-1)*perpage},{perpage}"
    return sql
def sal_emple_count():
    sql=f"select count(*) from empleado as e inner join sal_emple as sal_e on e.id=sal_e.sal_id where sal_e.sal_id=?"
    return sql
def sal_delete():
    sql="delete from sal_emple where id=?"
    return sql
