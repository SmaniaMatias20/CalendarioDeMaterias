from model.Materia import Materia
from .ConectionDB import ConectionDB
from tkinter import messagebox

def create_table():
    conection = ConectionDB()
    
    sentence = '''
    CREATE TABLE materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NULL,
    qualification VARCHAR(10) NULL,
    state VARCHAR(100) NULL
    )
    '''

    try:
        conection.cursor.execute(sentence)
        conection.close()
        tittle = 'Crear Registro'
        message = 'Se creó la tabla en la base de datos'
        messagebox.showinfo(title = tittle, message = message)
    except:
        tittle = 'Crear Registro'
        message = 'La tabla ya ha sido creada'
        messagebox.showwarning(title = tittle, message = message)

def eliminate_table():
    conection = ConectionDB()

    sentence = '''
    DROP TABLE materias
    '''
    try:
        conection.cursor.execute(sentence)
        conection.close()
        tittle = 'Eliminar Registro'
        message = 'La tabla se elimino con exito'
        messagebox.showinfo(title = tittle, message = message)
    except:
        tittle = 'Eliminar Registro'
        message = 'No hay tabla para borrar'
        messagebox.showerror(title = tittle, message = message)


    
def save(materia: Materia):
    conection = ConectionDB()

    sentence = f"""
    INSERT INTO materias (name, qualification, state) VALUES ('{materia.name}', '{materia.qualification}', '{materia.state}')
    """
    try: 
        conection.cursor.execute(sentence)
        conection.close()
    except:
        tittle = 'Conexion al Registro'
        message = 'No hay tabla para insertar los datos'
        messagebox.showerror(title = tittle, message = message)

def show():
    conection = ConectionDB() 

    list_materias = []

    sentence = """
    SELECT * FROM materias 
    """

    try:
        conection.cursor.execute(sentence)
        list_materias = conection.cursor.fetchall()
        conection.close()
    except:
        tittle = 'Obtener Registros'
        message = 'No hay tabla para obtener los datos'
        messagebox.showwarning(title = tittle, message = message)
        
    return list_materias

def edit(materia: Materia, id):
    conection = ConectionDB()

    sentence = f"""
    UPDATE materias
    SET name = '{materia.name}', qualification = '{materia.qualification}', state = '{materia.state}' 
    WHERE id = {id}
    """

    try:
        conection.cursor.execute(sentence)
        conection.close()
    except:
        tittle = 'Actualizar Registro'
        message = 'No se ha podido actualizar el registro'
        messagebox.showerror(title = tittle, message = message)

def eliminate(id):
    conection = ConectionDB()

    sentence = f"""
    DELETE FROM materias WHERE id = {id}
    """

    try:
        conection.cursor.execute(sentence)
        conection.close()
    except:
        tittle = 'Eliminar Registro'
        message = 'No se ha podido eliminar el registro'
        messagebox.showerror(title = tittle, message = message)



