contador  =  0
sumatoria  =  0
numero  =  1
mientras  numero  ! =  0 :
    numero  =  int ( input ( "Ingrese un número entero (0 para parar la cuenta y obtener resultados):" ))
    si  numero  ! =  0 :
        sumatoria  + =  numero
        contador  + =  1
print ( "La sumatoria de los números ingresados ​​es:" , sumatoria )
print ( "El promedio de los números ingresados ​​es:" , sumatoria  /  contador )