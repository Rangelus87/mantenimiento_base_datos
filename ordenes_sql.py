import mysql.connector
class Comandos_sql:

    def abrir(self):
        conexión = mysql.connector.connect(host="localhost",user="root",passwd="",database="Bd1")

        return conexión
        
        
        
    def carga(self, datos):     
        conexión1 = self.abrir()
        cursor = conexión1.cursor()
        
        sql = "insert into articulos(descripcion, precio) values(%s,%s)"
        cursor.execute(sql, datos)
        conexión1.commit()
        conexión1.close()
        return cursor.lastrowid


    def consulta(self, dato):
        conexión1 = self.abrir()
        cursor = conexión1.cursor()

        sql=f"select descripcion, precio from articulos where codigo='{dato}'"
        cursor.execute(sql)
        conexión1.close()

        return cursor.fetchall()

    def eliminar(self, dato):
        conexión1 = self.abrir()
        cursor = conexión1.cursor()

        sql= f"delete from articulos where codigo={dato}"
        cursor.execute(sql, dato)
        conexión1.commit()
        conexión1.close()

    def modificar(self, descrip, precio,dato):
        conexión1 = self.abrir()
        cursor = conexión1.cursor()
        
        sql = f"update articulos set descripcion='{descrip}', precio='{precio}' where codigo='{dato}'"
        cursor.execute(sql)
        conexión1.commit()
        conexión1.close()



    def listar(self):
        conexión1 = self.abrir()
        cursor1 = conexión1.cursor()

        cursor1.execute("select codigo, descripcion, precio from articulos")
        conexión1.close()

        return cursor1.fetchall()
