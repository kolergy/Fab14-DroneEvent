################### WARNING #####################
# Vous devez installer le packet ivy-python	
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.py
#pip install ivy-python


from ivy.ivy import IvyServer
import time

class MyCameraServeur(IvyServer):
	
  dico_x = {}
  dico_y = {}
  dico_orientation = {}
  dico_time = {}

  def set_position_player(self, player, x, y, orientation, time):
    MyCameraServeur.dico_x[player] = x
    MyCameraServeur.dico_y[player] = y
    MyCameraServeur.dico_orientation[player] = orientation
    MyCameraServeur.dico_time[player] = time
  
  def __init__(self):
    IvyServer.__init__(self,'CAMERA')
    self.name = 'CAMERA'
    self.start('192.168.1.255:2010')       
    self.bind_msg(self.handle_demande_pos, 'DEMANDE POSITION')

  def handle_demande_pos(self, agent):
    player = agent.agent_name
    print ('L\'agent [' +  player + '] demande ca position')
    self.send_direct_message(player, 0,str(MyCameraServeur.dico_x[player]) + ' ' + str(MyCameraServeur.dico_y[player]) + ' ' + str(MyCameraServeur.dico_orientation[player]) + ' ' + str(MyCameraServeur.dico_time[player]))
    print('SentTo:'+ player + 'POS x:' + str(MyCameraServeur.dico_x[player]) + ' y:' + str(MyCameraServeur.dico_y[player]) + ' orientation:' + str(MyCameraServeur.dico_orientation[player]) + ' time:' + str(MyCameraServeur.dico_time[player]))


class MyCarClient(IvyServer):
  x = 0
  y = 0
  orientation = 0
  time = 0
  wait_for_reponse = True # Gestion attente reponse
  def __init__(self, name):
    IvyServer.__init__(self, name)
    self.name = name
    self.start('127.255.255.255:2010')
    time.sleep(1)

  def handle_direct_msg(self, client, num_id, msg):
    new_x, new_y, new_orientation, new_time = msg.split(' ')
    MyCarClient.x = int(new_x)
    MyCarClient.y = int(new_y)
    MyCarClient.orientation = int(new_orientation)
    MyCarClient.time = int(new_time)
    print ("Le serveur me dit que je suis en x:" + new_x + " en y:" + new_y + " en orienation:" + new_orientation + ". temps:" + new_time)
    MyCarClient.wait_for_reponse = False

  def refresh_postion(self):
    MyCarClient.wait_for_reponse = True 
    self.send_msg('DEMANDE POSITION')
    while (MyCarClient.wait_for_reponse) : # Gestion attente reponse
      time.sleep(0.0001)

  def get_x(self):
    return MyCarClient.x
  def get_y(self):
    return MyCarClient.y
  def get_orientation(self):
    return MyCarClient.orientation
  def get_time(self):
    return MyCarClient.time
