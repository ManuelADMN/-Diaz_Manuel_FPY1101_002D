##funcionesBibliotecaHola
libreria=[];

def agregarLibros():
    print("\n// Ha seleccionado agregar libro\n");
    try:
        titulo=input("\n/Ingrese el titulo del libro:  ");
    except TypeError:
        print("Ingrese un nombre válido..")
    else:
        try:
            autor=input("\n/Ingrese el autor del libro:  ");
        except TypeError:
            print("Ingrese un nombre válido..")
        else:
            try:
                fechaPublicacion=int(input("\n/Ingrese la fecha del libro:  "));
            except ValueError:
                print("Ingrese una fecha válida..")
            else:
                try:
                    genero=input("\n/Ingrese el genero del libro:  ");
                except TypeError:
                    print("Ingrese un genero válido..");
                else:
                    libro={'titulo': titulo,
                           'autor': autor,
                           'fechaPublicacion': fechaPublicacion,
                           'genero': genero};
                    libreria.append(libro);
                    return;
                print(f"\nLibro {titulo} se ha agregado correctamente.");

#Se imprimen los libros que hay en la colección.
def ver_libros():
    for i in libreria:
        print(i);

#Se modifica un libro en la colección, reemplazando su nombre.
def modificar_libro():
    try:
        libro = input("Ingrese el nombre del libro que quiere modificar: ");
    except TypeError:
        print("Libro inválido. Intente nuevamente.");
    else:
        try:
            libroModificar = input("Ingrese el nuevo nombre del libro: ");
        except TypeError:
            print("Libro inválido. Intente nuevamente.");
        else:
            for i in libreria:
                if (i == libro):
                    libreria.remove(libro);
                    libreria.append(libroModificar);
                    print("Modificado exitosamente.");
                else:
                    print("Libro no encontrado.");

#Se elimina un libro de la colección
def eliminar_libro():
    try:
        libro = input("Ingrese el nombre del libro que quiere eliminar: ");
    except TypeError:
        print("Libro inválido. Intente nuevamente.");
    else:
        for i in libreria:
            if (i == libro):
                libreria.remove(libro);
                print(f"Libro {libro} eliminado");
            else:
                print("Libro no encontrado.");


def guardarArchivo():
    print("\n// Ha seleccionado guardar colección\n\n");
    with open ('coleccionLibros.txt','w') as coleccion:
        for libro in libreria:
            coleccion.write(f"Titulo del libro: {titulo} Autor del libro: {autor} Fecha de Publicación: {fechaPublicacion} Genero del Libro: {genero} ");
            print("\nSe ha generado correctamente... Abriendo\n");
    with open ('coleccionLibros.txt','r') as coleccion:
        coleccionLeer=coleccion.read();
        print(coleccionLeer);

                    
agregarLibros();
ver_libros();