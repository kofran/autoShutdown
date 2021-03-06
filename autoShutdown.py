# -*- coding: 850 -*-
##Copyright 2015 Franco Borgazzi
##
##Licensed under the Apache License, Version 2.0 (the "License");
##you may not use this file except in compliance with the License.
##You may obtain a copy of the License at
##
##    http://www.apache.org/licenses/LICENSE-2.0
##
##Unless required by applicable law or agreed to in writing, software
##distributed under the License is distributed on an "AS IS" BASIS,
##WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##See the License for the specific language governing permissions and
##limitations under the License.

'''autoShutdown is a script to program the computer power-off
for Windows and Linux.'''

def licencia():
    print '''

Copyright 2015 Franco Borgazzi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

'''
    
def apagar(t):
    import os
    sisop = os.name
    if sisop == 'nt':
        comando = 'shutdown -s -t ' + str(t) 
        os.system(comando)
        print '''exito! si quieres cancelar el apagado automatico
        escriba cancelar, sino presione enter para salir'''
        a = raw_input()
        if a == 'cancelar':
            os.system('shutdown -a')
            print 'exito!'
            limpiar()
        else:
            exit()
    elif sisop == 'posix':
        
        t = t / 60 # convert seconds in minutes
        print '''Atencion:
        No cierre esta ventana o presiona Control + C
        o el apagado automatico se cancelara.
	A continuacion se le pedira ingresar su clave sudo
        Presione Enter(intro) para continuar...'''
        raw_input()
        comando = 'sudo shutdown -h +' + str(t) 
        os.system(comando)

def limpiar():
    # Clean terminal for windows and linux.
    import os
    sisop = os.name
    if sisop == 'nt':
        import subprocess as sp
        tmp = sp.call('cls', shell=True)
    elif sisop == 'posix':
        os.system('clear')
    
print '''
Apagado automatico version 1, para Linux, Windows
Requiere Python 2.7
'''

# Menu.
flag = 0

while flag == 0:
    print 'OPCIONES: S - SALIR, M - Minutos, H - Horas, D - Dias, L - Licencia'
    opcion = raw_input('Opcion: ')
        
    if opcion == 'S' or opcion == 's':
        print 'saliendo, presione enter para continuar...'
        raw_input()
        exit()        
    elif opcion == 'M' or opcion == 'm':
        t = input('Ingrese los minutos: ')
        # check if t is integer.
        if isinstance( t, (int, long) ) == True:
            
            #convert t to seconds
            t = int(t) * 60 
            apagar(t)
        else:
            limpiar()
            print 'Valor invalido, reintente'
            raw_input()
            limpiar()
    elif opcion == 'H' or opcion == 'h':
        t = input('Ingrese las horas: ')
        # check if t is integer.
        if isinstance( t, (int, long) ) == True:
            # convert hours to seconds.
            t = int(t) * 60 * 60
            apagar(t)
        else:
            limpiar()
            print 'Valor invalido, reintente'
            raw_input()
            limpiar()
    elif opcion == 'D' or opcion == 'd':
        t = input('Ingrese los dias: ')
        # check if t is integer.
        if isinstance( t, (int, long) ) == True:
            # convert days to seconds
            t = int(t) * 24 * 60 * 60
            apagar(t)
        else:
            limpiar()
            print 'Valor invalido, reintente'
            raw_input()
            limpiar()
    elif opcion == 'L' or opcion == 'l':
        licencia()
        raw_input('Enter para continuar...')
        limpiar()
    else:
        limpiar()
        print 'No ingreso una opcion valida'
        raw_input()
        limpiar()
