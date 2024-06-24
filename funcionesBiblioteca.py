import csv
##funcionesBibliotecaHola
libreria=[];
libro=[];
##Se agrega funcion de agregar libro.

def agregarLibros(libreria):
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
        libro={'titulo': titulo,
                'autor': autor,
                'fechaPublicacion': fechaPublicacion,
                'genero': genero};
        libreria.append(libro);
    print(f"\nLibro {titulo} se ha agregado correctamente.\n");
    return;

#Se imprimen los libros que hay en la colección.
def ver_libros(libreria):
    for i in libreria:
        print(i);

#Se modifica un libro en la colección, reemplazando su nombre.
def modificar_libro(libreria):
    try:
        titulo = input("Ingrese el nombre del libro que quiere modificar: ");
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
def eliminar_libro(libreria):
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


####Se incluye funcion de guardar archivo.

def guardarArchivo(libreria):
    print("\n// Ha seleccionado guardar colección\n\n");
    with open ('coleccionLibros.csv','w', newline = '') as coleccion:
        escritor = csv.writer(coleccion);
        escritor.writerow(libreria);


                    

#Nombres: Guillermo Cerda, Manuel Díaz y Martín Díaz