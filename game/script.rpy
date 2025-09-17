# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define JacobApellido = Character("Jacob Apellido Ruiz Otro nombre")

layeredimage jacob:
    zoom 0.5
    
    always "images/Jacopo/jacopo base.png"
    
    group expression:
        pos(301,202)
        attribute expr1 default:
            "images/Jacopo/jacopo 1.png"
        attribute expr2:
            "images/Jacopo/jacopo 6.png"
        attribute expr3:
            "images/Jacopo/jacopo 10.png"


# El juego comienza aquí.

label start:

    scene white
    show jacob expr1
    JacobApellido "Hola"
    show jacob expr2
    JacobApellido "¿Tengo algo raro en la cara?"

    scene white leafs
    show jacob expr3
    JacobApellido "Pero ahora estoy un poco mejor..."


    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    #show eileen happy

    # Presenta las líneas del diálogo.

    #e "Has creado un nuevo juego Ren'Py."

    #e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
