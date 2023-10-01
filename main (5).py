






#define the base class player
class player:
  def play (self):
    print ("the player is playing cricket".)
# Define the derived class Batsman
class Batsman (player):
  def Play (self):
    print ("the batsman is batting.")
# Define the derived class Bowler
class Bowler(player):
  def play (self):
      print ("the bowler is bowling.")
# create a subjects or Batsman and Bowler class
batsman= Batsman ()
bowler= Bowler()
# call the play() method for each object
batsman.play()
bowler.play()