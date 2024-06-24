##main 
import funcionesBiblioteca as func




print ("Bienvenido a la Biblioteca personal. Eliga una opcion de las que se mostraran: ");
while True:
    print("Opcion numero 1: Agregar Libros.");
    print("Opcion numero 2: Ver todos los Libros.");
    print("Opcion numero 3: Modificar un Libro.");
    print("Opcion numero 4: Eliminar un Libro.");
    print("Opcion numero 5: Guardar coleccion en un Archivo.");
    print("Opcion numero 6: Salir del Programa.");
    try:
        opcion=int(input("Ingrese una opcion de las que se muestran: "));
    except ValueError:
        print("\nIngrese una opción válida\n")
    else:
        if opcion==1:
            print("Usted ha seleccionado la opcion 1, Agregar un libro. ");
            func.agregarLibros();
        elif opcion==2:
            print("Usted ha seleccionado la opcion 2, ver libros. ");
            func.ver_libros();
        elif opcion==3:
            print("Usted ha seleccionado la opcion 3, Modificar un libro. ");
            func.modificar_libro();
        elif opcion==4:
            print("Usted ha seleccionado la opcion 4, Eliminar un libro. ");
            func.eliminar_libro();
        elif opcion==5:
            print("Usted ha seleccionado la opcion 5, Guardar Coleccion. ");
            func.guardarArchivo();
        elif opcion==6:
            print("Usted ha seleccionado la opcion 6, Saliendo. ");
            break;
        else:
            print("Ingrese una opción válida");

