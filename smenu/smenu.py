#######################################################################################
## Script Info:		smenu.py - Class with functions draw simples menus with sub-level 
##
#######################################################################################
## Create Author:	Fausto Branco
## Create Date:		2018-04-12
## Actual Version:  1.0.0
## Description:		
#######################################################################################
## Log Changes:
## Date:            2018-04-12
## Author:          Fausto Branco
## Version:         1.0.0
## Description:     Initial Version
#######################################################################################

import sys
import signal
import os
import select
import keypress

lst_Menus = []

obj_keypress = keypress.Get_Key()
__version__ = '1.0.0'

class smenu():
    def __init__(self, Menus):   
        """

        """
        global lst_Menus
        lst_Menus = Menus
        self.rows = 0
        self.columns = 0

    def get_limits(self):
        lrows, lcolumns = os.popen('stty size', 'r').read().split()
        self.rows = int(lrows)
        self.columns = int(lcolumns)

    def print_reset(self):
        #Clear all lines from int_LineStartPrint to end
        for idx,i in enumerate(range(1, 16)):
            sys.stdout.write("\033[" + str(i) + ";1H\033[K")
            sys.stdout.flush()

    def print_Options(self, Menu, Level):
        self.print_reset()
        print("\033[01;01H")
        pos_Column = 1 + 0 * Level
        pos_Line = 1 + 0 * Level
        self.get_limits()
        str_fmt = '{:<' + str(self.columns - pos_Column) + '}'
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (pos_Line + 2, pos_Column, str_fmt.format('Menu: ' + str(Menu))))
        lst_ItensMenu = [''] * 10
        for index in range(0, len(lst_Menus[Menu])):
            lst_ItensMenu[int(lst_Menus[Menu][index]['Item']) - 1] = str(lst_Menus[Menu][index]['Title'])
        for index in range(0, 10):
            if str(lst_ItensMenu[index]) <> '':
                if index == 9:
                    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (pos_Line + 4 + index, pos_Column, str_fmt.format('   [0] ' + str(lst_ItensMenu[index]))))
                else:
                    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (pos_Line + 4 + index, pos_Column, str_fmt.format('   [' + str(index + 1) + '] ' + str(lst_ItensMenu[index]))))
            else:        
                sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (pos_Line + 4 + index, pos_Column, str_fmt.format(' ')))
        sys.stdout.flush()
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (pos_Line + 14, pos_Column, str_fmt.format('Option: ')))
        sys.stdout.write("\x1b7\x1b[%d;%df" % (pos_Line + 14, pos_Column + 8))

    def show_menu(self, Menu, Level = 0):
        result_Keypress = ''   
        while result_Keypress <> 'Esc':
            self.print_Options(Menu, Level) 
            result_Keypress = obj_keypress.keypress()
            if result_Keypress in '1234567890':
                lst_Menu_Action = [d for d in lst_Menus[Menu] if d['Item'] in result_Keypress]
                if len(lst_Menu_Action) > 0:
                    if lst_Menu_Action[0]['Action'].startswith('{') and lst_Menu_Action[0]['Action'].endswith('}'):
                       str_Retorno = self.show_menu(lst_Menu_Action[0]['Action'][1:-1], Level + 1) 
                       if str_Retorno <> None:
                          return str_Retorno 
                    else:
                       return lst_Menu_Action[0]['Action']
                       #exec(lst_Menu_Action[0]['Action'])


