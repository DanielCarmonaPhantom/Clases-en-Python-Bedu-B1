import sqlite3

DB_NAME = 'db.sqlite3'

def sql_connection(db_name):

    try:
        conection = sqlite3.connect(db_name)
    except sqlite3.Error:
        print("Error")
        sys.exit(1)
        
    cur = conection.cursor()

    return (conection, cur)

def sql_table_product(con, cur):
    """
    Crea una tabla con nombre en la base de datos
    """
    sql = "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)"
    cur.execute(sql)
    con.commit()

def sql_insert(con, cur, entities):
    """
    Inserta datos en una tabla
    """
    sql = 'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)'  
    cur.execute(sql, entities)    
    con.commit()

def main():
    """
    Función principal del script
    """
    con, cur = sql_connection(DB_NAME)

    print(con, cur)

    print(sql_table_product(con, cur))

    cur.close()
    con.close()


if __name__ == "__main__":
    main()