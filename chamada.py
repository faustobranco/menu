import smenu

lst_Menus = {'Main': [{'Item': '1', 'Title': 'List Nodes', 'Action': 'function1("List Nodes")'}, 
                      {'Item': '2', 'Title': 'YAML Operations', 'Action': '{YAML}'}, 
                      {'Item': '3', 'Title': 'JVM Operations', 'Action': '{JVM}'}, 
                      {'Item': '4', 'Title': 'Restart Services', 'Action': 'function1("Restart Services")'}, 
                      {'Item': '0', 'Title': 'Exit',   'Action': 'menu_exit()'}], 
             'YAML': [{'Item': '1', 'Title': 'List All Keys', 'Action': 'function1("List All Keys")'},
                      {'Item': '2', 'Title': 'Get Key value from all Nodes', 'Action': 'function1("Get Key value from all Nodes")'},
                      {'Item': '3', 'Title': 'Change Key value on all Nodes', 'Action': 'function1("Change Key value on all Nodes")'}], 
             'JVM': [{'Item': '1', 'Title': 'List jvm.options GC1 Heap Size', 'Action': 'function1("List jvm.options GC1 Heap Size")'},
                     {'Item': '2', 'Title': 'Change jvm.options GC1 Heap Size', 'Action': 'function1("Change jvm.options GC1 Heap Size")'}]}

obj_SMenu = smenu.smenu(lst_Menus)

def function1(sParameter):
    print('\033[16;05H' + sParameter)


def MainMenu():
    print "\033c"        
    str_retorno = obj_SMenu.show_menu('Main')  
    str_retorno = ''
    while str_retorno not in ('menu_exit', None):
        str_retorno = obj_SMenu.show_menu('Main') 
        if str_retorno not in ('menu_exit', None):
            exec(str_retorno)

MainMenu()