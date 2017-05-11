sala = [['001','150','Disponivel'],['002','200','Ocupada']]

def adicionar_sala(cod_sala,lotacao,status): ############### PRONTO ################
    sala_inter=[cod_sala,lotacao,status]
    sala.append(sala_inter)
    print (" \n \n ========= Cadastrado com Sucesso ============")
    
def buscar_sala(cod_sala): ####################### PRONTO #######################
        for i in sala:
            if (i[0]== cod_sala):
                return i
        return

def definir_status_ocupada(cod_sala):####################### PRONTO #######################
    for t in range(len(sala)):
        for i in sala:
            if cod_sala == i[0]:
                i [t][2]=('Ocupada')
                return i

def remover_sala(cod_sala):####################### PRONTO #######################
        for tam in range(len(sala)):
            for s in sala:
                if s[0] == cod_sala:
                    del sala[tam]
                    print(" \n \n ========= Excluído com Sucesso ============")
                    return True
            print(" \n \n ========= Sala não encontrada ============")
            

def remover_todas_salas():####################### PRONTO #######################
    global sala
    sala=[]
    print(" \n \n ========= Excluído com Sucesso ============")
    return True

def listar_salas():####################### PRONTO #######################
    for i in sala:
        print(i)

def definir_status_ocupada(cod_sala):####################### PRONTO #######################
    for tam in range (len(sala)):
        for alt in sala:
            if alt[0] == cod_sala:
                sala[tam][2]= 'Ocupado'
                print(" \n \n ========= Alterado com Sucesso ============")
                return True
    print(" \n \n ========= Não encontrado ============")         

def definir_status_disponivel(cod_sala): ####################### PRONTO #######################
    for tam in range (len(sala)):
        for alt in sala:
            if alt[0] == cod_sala:
                sala[tam][2]= 'Disponivel' 
                print(" \n \n ========= Alterado com Sucesso ============")
                return True
    print(" \n \n ========= Não encontrado ============")
