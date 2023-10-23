import serial

#Definido porta serial e taxa de transmissao
porta_serial = ''
taxa_transmissao = 9600



#Criando objeto da calsse Serial para se comunicar com o arduino
arduino =  serial.Serial (9600, timeout = 1)



#Solicitando a conexão com o arduino
arduino.readline


#imprimindo a mensagem de conexão caso esteja correta 
print('Arduino Conectado')



#arduino a conexão com o arduino 
arduino.close()


