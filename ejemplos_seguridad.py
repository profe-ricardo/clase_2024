import bcrypt

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
main()