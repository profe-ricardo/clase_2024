import bcrypt
import time

def main():
    password = input("Ingrese una contraseña: ").encode('utf-8')
    print("contraseña registrada:", password.decode('utf-8'))

    salto = bcrypt.gensalt()
    secured_password = bcrypt.hashpw(password, salto)

    print("contraseña segura:", secured_password.decode('utf-8'))
    
    validation_password = input("Ingrese la contraseña a validar: ").encode('utf-8')

    if bcrypt.checkpw(validation_password, secured_password):
        print("Contraseña correcta")
    else:
        print("Error de contraseña")

    confirmacion = input("¿Desea volver a probar? (s/n): ")
    time.sleep(1)

    if confirmacion == "s":
        print("Recargando...")
        time.sleep(2)
        print("-------------------------------")
        main()
    else:
        time.sleep(1)
        print("Adios")

main()