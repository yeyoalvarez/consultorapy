import sqlite3
from sqlite3 import Error
from .connection import create_connection

def insertar_libro(data):
    conn = create_connection()
    sql = """ 
    INSERT INTO libro (fecha_carga, signatura, titulo, editorial, coleccion,edicion, isbn, lugar_impresion, notas, anho_impresion) 
    VALUES(date('now'), ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro añadido")
        return True, cur.lastrowid
    except Error as e:
        print("Eror al insertar libro:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def actualizar_libro(_id, data):
    conn = create_connection()

    sql = f""" UPDATE libro SET  
                            signatura = ?,
                            titulo = ?,
                            editorial = ?,
                            coleccion = ?,
                            edicion = ?,
                            isbn = ?
                            lugar_impresion = ?,
                            notas = ?,
                            anho_impresion = ?,
            WHERE book_id = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error al actualizar: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def listar_libros():
    conn = create_connection()
    sql = "SELECT * FROM libro"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error al listar: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def buscar_libro_registro(_id):
    conn = create_connection()
    #f antes para concatenar
    sql = f"SELECT * FROM libro WHERE id_libro = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book
    except Error as e:
        print("Error selecting book by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def buscar_libro_titulo(title):
    conn = create_connection()
    sql = f"SELECT * FROM libro WHERE title LIKE '%{title}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting book by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()