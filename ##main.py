##main 
import funcionesBiblioteca as func




print ("Bienvenido a la Biblioteca personal. Eliga una opcion de las que se mostraran: ");
print("Opcion numero 1: Agregar Libros.");
print("Opcion numero 2: Ver todos los Libros.");
print("Opcion numero 3: Modificar un Libro.");
print("Opcion numero 4: Eliminar un Libro.");
print("Opcion numero 5: Guardar coleccion en un Archivo.");
print("Opcion numero 6: Salir del Programa.");
try:
    opcion =int(input("Ingrese una opcion de las que se muestran: "));
except ValueError:
    print("\nIngrese una opción válida\n")
else:
    if opcion==1:
        print("Usted ha seleccionado la opcion 1, Agregar un libro. ");
        func.agregarLibros();
    if opcion==2:
        print("Usted ha seleccionado la opcion 1, Agregar un libro. ");
        func.agregarLibros();
