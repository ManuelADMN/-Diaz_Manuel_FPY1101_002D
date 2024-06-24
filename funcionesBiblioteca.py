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
                titulo=input("\n/Ingrese el titulo del libro:  ");
            except TypeError:
                print("Ingrese un nombre válido..")
            else:
        

