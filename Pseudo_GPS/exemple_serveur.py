################### WARNING #####################
# Vous devez installer le packet ivy-python	
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.py
#pip install ivy-python

import lib_com_fab14 # Il faut lib_com_fab14.py dans le même dossier

cameraServeur = lib_com_fab14.MyCameraServeur()

# Mise à jour de la position d'un joueur : nom du jour, x , y
cameraServeur.set_position_player("P1",10,100,1,111)
cameraServeur.set_position_player("P2",10,200,2,222)
cameraServeur.set_position_player("P3",10,300,3,333)
cameraServeur.set_position_player("P4",10,400,4,444)
	
