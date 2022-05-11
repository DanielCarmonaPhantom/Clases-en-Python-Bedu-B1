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

def sql_table(con, cur, name):
    """
    Crea una tabla con nombre en la base de datos
    """
    sql = f"CREATE TABLE {name}"
    cur.execute(sql)
    con.commit()

def main():
    """
    Función principal del script
    """
    con, cur = sql_connection(DB_NAME)

    print(con, cur)
    cur.close()
    con.close()


if __name__ == "__main__":
    main()