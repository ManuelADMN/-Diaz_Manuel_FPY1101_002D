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
                    print("Ingrese un genero válido..")
                else:
                    libro={'titulo': titulo,
                           'autor': autor,
                           'fechaPublicacion': fechaPublicacion,
                           'genero': genero};
                    libreria.append(libro);
                print(f"\nLibro {titulo} se ha agregado correctamente.")
                    
        

