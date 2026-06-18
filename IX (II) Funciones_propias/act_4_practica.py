"""Se tiene una medida de tiempo expresada en horas, minutos y segundos con valores arbitrarios. 
Diseña una función que transforme dicha medida en una expresión correcta y la devuelva. 
Por ejemplo, dada la medida 4h 93m 102s, el programa deberá obtener como resultado 5h 34m 42s."""

from mis_funciones import corregir_tiempo as formato_hora


def main ():
    h,m,s = 26,86,79
    h,m,s = formato_hora(h,m,s)
    print(h,"h",m,"m",s,"s" )
main()
