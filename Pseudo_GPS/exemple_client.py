################### WARNING #####################
# Vous devez installer le packet ivy-python	
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.py
#pip install ivy-python


import lib_com_fab14 # Il faut lib_com_fab14.py dans le même dossier
import sys
import time

# Recuperation du nom dans le premier argument donné au script 
cmd_line_arguments = sys.argv[1:]    
if(len(cmd_line_arguments) == 0):
	print( "Give a name ! ");
	print( "exemple ./client.py P1");
	quit()
		
name = cmd_line_arguments[0] 

#Connexion au serveur Ivy avec le nom donné en param
my_client_car = lib_com_fab14.MyCarClient(name)

# Main loop du client 
while True:
  print("demande !")
  my_client_car.refresh_postion() # on demande la pos au serveur
  print("x : " + str(my_client_car.get_x())) #on lit les dernière info récupéré
  print("y : " + str(my_client_car.get_y()))
  print("orientation : " + str(my_client_car.get_orientation()))
  print("time : " + str(my_client_car.get_time()))
  time.sleep(1)


