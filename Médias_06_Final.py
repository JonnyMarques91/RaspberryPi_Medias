﻿import tkinter as tk
import rpi_backlight as bl
import random
import time
import sys
import serial
import RPi.GPIO as GPIO

#Congiguração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Ctes. de tempo
T100ms = 0.1
T10s = 10
TEMPO_USUARIO = 30

#ID Alunos
ALUNO_1 = 1
ALUNO_2 = 2
ALUNO_3 = 3

#Dimensões
lPeq = 9
lMed = 12
lGde = 30
aPeq = 1

#Fonte
Arialb = "Arial bold"
Font_Size = 7

#Cores
Az = ["DodgerBlue4","DodgerBlue3"]
Am = ["goldenrod4","goldenrod3"]
Vm = ["IndianRed4","IndianRed3"]
Cz = ["white","light grey"]
Dd = ["gray26","gray36"]
Br = "White"
Pt = "black"

#Colunas
p1 = "P1"
p2 = "P2"
p3 = "SUB1"
p4 = "P3"
p5 = "P4"
p6 = "SUB2"

#Dados dos Alunos
r1 = "Aluno: "
r3 = "Curso: "
r5 = "Série: "
r7 = "Período: "
r9 = "2018"

#Vetores Globais
vNotas = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]  #Melhorar...

#Tela
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

def Change_Screen(Index, scrShow):

    #Tempo permitido de acesso do usuário
    Screen_Timer = TEMPO_USUARIO

    if (Index == ALUNO_1):

        lbl_dados = []
        lbl_disciplinas = []
        lbl_resultado = []
        lbl_Notas_1, lbl_Notas_2, lbl_Notas_3, lbl_Notas_4, lbl_Notas_5, lbl_Notas_6 = [],[],[],[],[],[]

        # Disciplinas do Aluno 1
        d1 = "ECA411 - Sistemas de Controle I"
        d2 = "EEE403 - Eletrônica de Potência"
        d3 = "EEN212 - Instrumentação e Automação"
        d4 = "EEN221 - Telecomunicações"
        d5 = "EEN941 - Altas Frequências I"
        d6 = "EFH104 - Gerenciamento Industrial"
        d7 = "EFH107 - Direito Empresarial"
        d8 = "EFH108 - Pilotagem - Mil. Falcon"

        r2 = "Han Solo"
        r4 = "Engenharia Eletrônica"
        r6 = "5ª"
        r8 = "Noturno"
    
        sDisciplinas = ["Disciplinas", d1, d2, d3, d4, d5, d6, d7, d8]
        sProvasCol = [p1, p2, p3, p4, p5, p6]
        sDados = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

        # Para cada item contido no vetor
        for disciplina in sDisciplinas:
            i = sDisciplinas.index(disciplina)  # i <- index do vetor
            Alterna_icor = i%2                  # Alterna entre os indices pares e ímpares
            lbl_disciplinas.append(tk.Label(Screen, text = disciplina, font = (Arialb,Font_Size), fg = Br, bg = Am[Alterna_icor], width = lGde, height = 2))  # Cria um label para cada index
            lbl_disciplinas[i].grid( row = i, column = 1)   # Ordena os labels sequencialmente em linhas
        
        for i in range(len(sDisciplinas)-1):

            #i = sDisciplinas.index(disciplina)  # i <- index do vetor
            Alterna_icor = i%2                  # Alterna entre os indices pares e ímpares
            # Atribui valores randomicos aos labels das notas
            lbl_Notas_1.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_2.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_3.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_4.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_5.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_6.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))

            # Posiciona verticalmente os Labels das notas
            lbl_Notas_1[i].grid(row = i+1, column = 2)
            lbl_Notas_2[i].grid(row = i+1, column = 3)
            lbl_Notas_3[i].grid(row = i+1, column = 4)
            lbl_Notas_4[i].grid(row = i+1, column = 5)
            lbl_Notas_5[i].grid(row = i+1, column = 6)
            lbl_Notas_6[i].grid(row = i+1, column = 7)

        for c in sProvasCol:
            # Alternância das Cores
            if (len(sProvasCol)%2 == 0):    jAux = sProvasCol.index(c) + 1
            else:   jAux = sProvasCol.index(c)
            Alterna_jcor = jAux%2
            # Varredura em Colunas
            j = sProvasCol.index(c)
            lbl_resultado.append(tk.Label(Screen, text = c , font = (Arialb,Font_Size), fg = Br , bg = Am[Alterna_jcor] , width = lPeq , height = 2))   # Cria um label para cada index
            lbl_resultado[j].grid(row = 0 , column = j+2)    # Ordena os labels sequencialmente em colunas 
            
        for dado in sDados:
            k = sDados.index(dado)
            Alterna_kcor = k%2
            lbl_dados.append(tk.Label(Screen, text = dado , font = (Arialb,Font_Size), fg = Br , bg = Dd[Alterna_kcor] , width = lGde , height = 2))
            lbl_dados[k].grid(row = k, column = 0)

    if (Index == ALUNO_2):

        lbl_dados = []
        lbl_disciplinas = []
        lbl_resultado = []
        lbl_Notas_1, lbl_Notas_2, lbl_Notas_3, lbl_Notas_4, lbl_Notas_5, lbl_Notas_6 = [],[],[],[],[],[]

        #Disciplinas do Aluno 2
        d1 = "EEE281 - Instalações Elétricas"
        d2 = "EEE402 - Conversão de Energia"
        d3 = "EEN211 - Eletromagnestismo II"
        d4 = "EEN251 - Microcontroladores"
        d5 = "EFH113 - Emp. e Gestão"
        d6 = "ETE204 - Sistemas e Sinais"
        d7 = "ETE802 - Fen. de Transportes"
        d8 = "PAE205 - Manutenção - Mil. Falcon"

        r2 = "Chewbacca"
        r4 = "Ciclo Básico"
        r6 = "1ª"
        r8 = "Noturno"
    
        sDisciplinas = ["Disciplinas", d1, d2, d3, d4, d5, d6, d7, d8]
        sProvasCol = [p1, p2, p3, p4, p5, p6]
        sDados = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

        # Para cada item contido no vetor
        for disciplina in sDisciplinas:
            i = sDisciplinas.index(disciplina)  # i <- index do vetor
            Alterna_icor = i%2                  # Alterna entre os indices pares e ímpares
            lbl_disciplinas.append(tk.Label(Screen, text = disciplina, font = (Arialb,Font_Size), fg = Br, bg = Az[Alterna_icor], width = lGde, height = 2))  # Cria um label para cada index
            lbl_disciplinas[i].grid( row = i, column = 1)   # Ordena os labels sequencialmente em linhas
        
        for i in range(len(sDisciplinas)-1):

            #i = sDisciplinas.index(disciplina)  # i <- index do vetor
            Alterna_icor = i%2                  # Alterna entre os indices pares e ímpares
            # Atribui valores randomicos aos labels das notas
            lbl_Notas_1.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_2.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_3.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_4.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_5.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_6.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))

            # Posiciona verticalmente os Labels das notas
            lbl_Notas_1[i].grid(row = i+1, column = 2)
            lbl_Notas_2[i].grid(row = i+1, column = 3)
            lbl_Notas_3[i].grid(row = i+1, column = 4)
            lbl_Notas_4[i].grid(row = i+1, column = 5)
            lbl_Notas_5[i].grid(row = i+1, column = 6)
            lbl_Notas_6[i].grid(row = i+1, column = 7)

        for c in sProvasCol:
            # Alternância das Cores
            if (len(sProvasCol)%2 == 0):    jAux = sProvasCol.index(c) + 1
            else:   jAux = sProvasCol.index(c)
            Alterna_jcor = jAux%2
            # Varredura em Colunas
            j = sProvasCol.index(c)
            lbl_resultado.append(tk.Label(Screen, text = c , font = (Arialb,Font_Size), fg = Br , bg = Az[Alterna_jcor] , width = lPeq , height = 2))   # Cria um label para cada index
            lbl_resultado[j].grid(row = 0 , column = j+2)    # Ordena os labels sequencialmente em colunas 
            
        for dado in sDados:
            k = sDados.index(dado)
            Alterna_kcor = k%2
            lbl_dados.append(tk.Label(Screen, text = dado , font = (Arialb,Font_Size), fg = Br , bg = Dd[Alterna_kcor] , width = lGde , height = 2))
            lbl_dados[k].grid(row = k, column = 0)

    if (Index == ALUNO_3):
        lbl_dados = []
        lbl_disciplinas = []
        lbl_resultado = []
        lbl_Notas_1, lbl_Notas_2, lbl_Notas_3, lbl_Notas_4, lbl_Notas_5, lbl_Notas_6 = [],[],[],[],[],[]

        #Disciplinas do Aluno 3
        d1 = "EFB105 - Cálculo I"
        d2 = "EFB106 - Geometria Analítica"
        d3 = "EFB205 - Física I"
        d4 = "EFB403 - Algoritmos e Programação"
        d5 = "EFB502 - Química"
        d6 = "EFB603 - Introdução à Engenharia"
        d7 = "EFB813 - Desenho"
        d8 = "EFB352 - Métodos Numéricos"
        
        r2 = "Luke Skywalker"
        r4 = "Ciclo Básico"
        r6 = "1ª"
        r8 = "Diurno"
    
        sDisciplinas = ["Disciplinas", d1, d2, d3, d4, d5, d6, d7, d8]
        sProvasCol = [p1, p2, p3, p4, p5, p6]
        sDados = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

        # Para cada item contido no vetor
        for disciplina in sDisciplinas:
            i = sDisciplinas.index(disciplina)  # i <- index do vetor
            Alterna_icor = i%2                  # Alterna entre os indices pares e ímpares
            lbl_disciplinas.append(tk.Label(Screen, text = disciplina, font = (Arialb,Font_Size), fg = Br, bg = Am[Alterna_icor], width = lGde, height = 2))  # Cria um label para cada index
            lbl_disciplinas[i].grid( row = i, column = 1)   # Ordena os labels sequencialmente em linhas
        
        for i in range(len(sDisciplinas)-1):

            #i = sDisciplinas.index(disciplina)  # i <- index do vetor
            Alterna_icor = i%2                  # Alterna entre os indices pares e ímpares
            # Atribui valores randomicos aos labels das notas
            lbl_Notas_1.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_2.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_3.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_4.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_5.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
            lbl_Notas_6.append(tk.Label(Screen, text = random.choice(vNotas), font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))

            # Posiciona verticalmente os Labels das notas
            lbl_Notas_1[i].grid(row = i+1, column = 2)
            lbl_Notas_2[i].grid(row = i+1, column = 3)
            lbl_Notas_3[i].grid(row = i+1, column = 4)
            lbl_Notas_4[i].grid(row = i+1, column = 5)
            lbl_Notas_5[i].grid(row = i+1, column = 6)
            lbl_Notas_6[i].grid(row = i+1, column = 7)

        for c in sProvasCol:
            # Alternância das Cores
            if (len(sProvasCol)%2 == 0):    jAux = sProvasCol.index(c) + 1
            else:   jAux = sProvasCol.index(c)
            Alterna_jcor = jAux%2
            # Varredura em Colunas
            j = sProvasCol.index(c)
            lbl_resultado.append(tk.Label(Screen, text = c , font = (Arialb,Font_Size), fg = Br , bg = Am[Alterna_jcor] , width = lPeq , height = 2))   # Cria um label para cada index
            lbl_resultado[j].grid(row = 0 , column = j+2)    # Ordena os labels sequencialmente em colunas 
            
        for dado in sDados:
            k = sDados.index(dado)
            Alterna_kcor = k%2
            lbl_dados.append(tk.Label(Screen, text = dado , font = (Arialb,Font_Size), fg = Br , bg = Dd[Alterna_kcor] , width = lGde , height = 2))
            lbl_dados[k].grid(row = k, column = 0)
        
    #Contagem até o logoff automático    
    while scrShow:

        if (Screen_Timer != 0): 
            print(Screen_Timer)
            bl.set_power(True)
            Screen_Timer -= 1
        else:
            scrShow = False
            bl.set_power(False)
            Main_Screen()

        #Labels para exibição do timmer
        lbl_Restante = tk.Label(Screen, text = "Tempo Restante para Consulta:" , font = (Arialb,Font_Size), width = lGde-3 , height = 1)
        lbl_Tempo = tk.Label(Screen, text = str(int(Screen_Timer)) + "  Segundos", font = (Arialb,Font_Size), width = lGde-3 , height = 1)
        lbl_Restante.grid(row = 12, column = 1)
        lbl_Tempo.grid(row = 13, column = 1)
        print(Screen_Timer)
        time.sleep(1)
        Screen.update()

#Função para transição de telas
def Select_Screen(scrIndex, Change_Request):
    Change_Screen(scrIndex, Change_Request)

#Teste de login - Aluno 1
def Button_1():
    Screen_Index = 1
    scrRequest = True
    Select_Screen(Screen_Index, scrRequest)
    scrRequest = False

#Teste de login - Aluno 2
def Button_2():
    Screen_Index = 2
    scrRequest = True
    Select_Screen(Screen_Index, scrRequest)
    scrRequest = False

#Teste de login - Aluno 3
def Button_3():
    Screen_Index = 3
    scrRequest = True
    Select_Screen(Screen_Index, scrRequest)
    scrRequest = False

def Button_4():
    DataEntry = tk.Entry(Screen, textvariable = ID_Aluno)
    verifica_ID = ID_Aluno.get()
    print(verifica_ID)
    Main_Screen()

def Logoff():
    Screen.quit()

#Função para leitura de dados via Serial - TESTE...
# def  readData(data):
#     ser = serial.Serial (port = ' / dev / ttyUSB0 ',
#     baudrate = 9600,
#     parity = serial.PARITY_NONE ,
#     stopbits = serial.STOPBITS_ONE ,
#     bytesize = serial.EIGHTBITS ,
#     timeout  = 0)

#     print('[serialPrinter]: Trying to read data from serial port...' )

#     if ser.isOpen():
#   try:
#       ser.flushInput()
#       ser.read(pesquisar como captar dado)        #Coletar o dado vindo da serial, e utilizar como entrada para login
#       print('[serialPrinter]: Data read succesfully!')    #Msg de confirmação
#   except Exception as Exc:
#       logMsg = '[serialPrintter]: Comunication error...'+str(Exc)
#       print('logMsg')

#Função para exibição da tela inicial
def Main_Screen():
    lbl_dados = []
    lbl_disciplinas = []
    lbl_resultado = []
    lbl_Notas_1, lbl_Notas_2, lbl_Notas_3, lbl_Notas_4, lbl_Notas_5, lbl_Notas_6 = [],[],[],[],[],[]

    # Disciplinas do Aluno 1
    d1 = "****"

    r2 = "*** Nome_Aluno ***"
    r4 = "*** Curso_Aluno ***"
    r6 = "*** Ano_Aluno ***"
    r8 = "*** Período_Aluno ***"
    
    sDisciplinas = ["*** Disciplinas ***", d1, d1, d1, d1, d1, d1, d1, d1]
    sProvasCol = [p1, p2, p3, p4, p5, p6]
    sDados = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

    # Para cada item contido no vetor
    for i in range(len(sDisciplinas)):

        Alterna_icor = i%2  # Alterna entre os indices pares e ímpares
        if (i != 0):
            lbl_disciplinas.append(tk.Label(Screen, text = "", font = (Arialb,Font_Size), fg = Br, bg = Vm[Alterna_icor], width = lGde, height = 2))  # Cria um label para cada index
            lbl_disciplinas[i].grid( row = i, column = 1)   # Ordena os labels sequencialmente em linhas
        else:
            lbl_disciplinas.append(tk.Label(Screen, text = "*** Disciplinas ***", font = (Arialb,Font_Size), fg = Br, bg = Vm[Alterna_icor], width = lGde, height = 2))  # Cria um label para cada index
            lbl_disciplinas[0].grid( row = 0, column = 1)   # Ordena os labels sequencialmente em linhas

    for i in range(len(sDisciplinas)-1):
        Alterna_icor = i%2
        # Atribui valores randomicos aos labels das notas
        lbl_Notas_1.append(tk.Label(Screen, text = "####", font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
        lbl_Notas_2.append(tk.Label(Screen, text = "####", font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
        lbl_Notas_3.append(tk.Label(Screen, text = "####", font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
        lbl_Notas_4.append(tk.Label(Screen, text = "####", font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
        lbl_Notas_5.append(tk.Label(Screen, text = "####", font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))
        lbl_Notas_6.append(tk.Label(Screen, text = "####", font = (Arialb,Font_Size), fg = Pt, bg = Cz[Alterna_icor], width = lPeq, height = 2))

        # Posiciona verticalmente os Labels das notas
        lbl_Notas_1[i].grid(row = i+1, column = 2)
        lbl_Notas_2[i].grid(row = i+1, column = 3)
        lbl_Notas_3[i].grid(row = i+1, column = 4)
        lbl_Notas_4[i].grid(row = i+1, column = 5)
        lbl_Notas_5[i].grid(row = i+1, column = 6)
        lbl_Notas_6[i].grid(row = i+1, column = 7)

    for c in sProvasCol:
        # Alternância das Cores
        if (len(sProvasCol)%2 == 0):    jAux = sProvasCol.index(c) + 1
        else:   jAux = sProvasCol.index(c)
        Alterna_jcor = jAux%2
        # Varredura em Colunas
        j = sProvasCol.index(c)
        lbl_resultado.append(tk.Label(Screen, text = c , font = (Arialb,Font_Size), fg = Br , bg = Vm[Alterna_jcor] , width = lPeq , height = 2))   # Cria um label para cada index
        lbl_resultado[j].grid(row = 0 , column = j+2)    # Ordena os labels sequencialmente em colunas 
            
    for dado in sDados:
        k = sDados.index(dado)
        Alterna_kcor = k%2
        lbl_dados.append(tk.Label(Screen, text = dado , font = (Arialb,Font_Size), fg = Br , bg = Dd[Alterna_kcor] , width = lGde , height = 2))
        lbl_dados[k].grid(row = k, column = 0)

    ID_Aluno = tk.StringVar()

    #Botões para teste de navegação entre usuários
    toggleButton1 = tk.Button(Screen, text="Tela 1", font = (Arialb,Font_Size), width = lGde-4, height = 1, command = Button_1)
    toggleButton2 = tk.Button(Screen, text="Tela 2", font = (Arialb,Font_Size), width = lGde-4, height = 1, command = Button_2)
    toggleButton3 = tk.Button(Screen, text="Tela 3", font = (Arialb,Font_Size), width = lGde-4, height = 1, command = Button_3)
    #Campo de entrada do ID
    DataEntry = tk.Entry(Screen, textvariable = ID_Aluno)

    #Botão do campo de entrada - TESTE...
    #EntryButton =  tk.Button(Screen, text="OK", font = ("Arial bold",11), width = lPeq, height = 1, command = Button_4)

    #Posicionamento dos botões no grid
    toggleButton1.grid(row = 12, column = 0)
    toggleButton2.grid(row = 13, column = 0)
    toggleButton3.grid(row = 14, column = 0)
    DataEntry.grid(row = 14, column = 1)
    #EntryButton.grid(row = 14, column = 2)

    #Botão de Logoff - TESTE...
    #logoffButton = tk.Button(Screen, text = "Logoff", font = (Arialb,11), width = lPeq-3, height = 1, command = Logoff)
    #logoffButton.grid(row = 13, column = 2)

    #Inicialização da porta serial
    ser = serial.Serial(port = '/dev/ttyAMA0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout = 0)
    ser.read()

    #Loop para Backlight e verificação do usuário
    while init_Screen:

        #Controle de Backlight
         if (GPIO.input(6) == True):
             bl.set_power(True)
             print("Tem")

         if (GPIO.input(6) == False):
             bl.set_power(False)    

         verifica_ID = ID_Aluno.get()
         #verifica_ID = ser.read()
         print(verifica_ID)

        #Login Aluno Han Solo
         if (verifica_ID == "Solo"):
             Button_1()

        #Login Aluno Chewbacca
         if (verifica_ID == "Chewie"):
            Button_2()

        #Login Aluno Luke Skywalker
         if (verifica_ID == "Skywalker"):
            Button_3()

         time.sleep(0.5)
         Screen.update()

#Inicializações gerais
CNT_Backlight = 0
init_Screen = True
Screen = tk.Tk()
tk.StringVar()
Screen.title("Médias 2018")
Main_Screen()
