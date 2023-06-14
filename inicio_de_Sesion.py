archivo=open('archivo.txt','w')
y=False
w=False
print("Bienvenido Nuevo usuario")
archivo.write("Bienvenido Nuevo usuario")
a=int(input('\n1.Iniciar sesion\n2.Registrarse\n'))
while a!=1 and a!=2:
    print("Opcion incorrecta... Vuelva a ingresar una opcion")
    a=int(input('\n1.Iniciar sesion\n2.Registrarse\n'))
while w==False:
    if y==False and a==1:
        print("No tienes un usuario registrado")
        a=int(input('\n1.Iniciar sesion\n2.Registrarse\n'))
        while a!=1 and a!=2:
            print("Opcion incorrecta... Vuelva a ingresar una opcion")
            a=int(input('\n1.Iniciar sesion\n2.Registrarse\n'))
    if a==1 and y==True:
        x=input("Usuario: ")
        z=input("Contraseña: ")
        if x!=ss or z!=pw:
            print("Usuario o contraseña incorrectos, intente nuevamente")
            x=input("Usuario: ")
            z=input("Contraseña: ")
        print("\nBienvenido ",ss," denuevo...")
        w=True
        archivo.write("\nBienvenido ")
        archivo.write(ss)
        archivo.write(" denuevo...")
        archivo.close()
    if a==2:
        name=input("Nombre: ")
        ss=input("Usuario: ")
        pw=input("Contraseña: ")
        print("\nUsuario registrado exitosamente!\n")
        y=True
        archivo.write("\nUsuario registrado exitosamente!\n")
        a=int(input('\n1.Iniciar sesion\n2.Registrarse\n'))
