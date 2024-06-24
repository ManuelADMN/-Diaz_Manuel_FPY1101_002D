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
                fechaPublicacion=int(input("\n/Ingrese el titulo del libro:  "));
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


def guardarArchivo():
    print("\n// Ha seleccionado guardar colección\n\n");
    with open ('coleccionLibros.txt','w') as coleccion:
        for libro in libreria:
            coleccion.write(f"Titulo del libro: {titulo} Autor del libro: {autor} Fecha de Publicación: {fechaPublicacion} Genero del Libro: {genero} ");
            print("\nSe ha generado correctamente... Abriendo\n");
    with open ('coleccionLibros.txt','r') as coleccion:
        
                    
        

