import game_data
import art
import random
import os

os.system('clear')



print(art.logo)

flag=True
score=0

while flag==True:

  def genrand():
    rand1=random.randint(0,len(game_data.data)-1)
    rand2=random.randint(0,len(game_data.data)-1)
    return(rand1,rand2)

  rand1,rand2=genrand()
  while rand1==rand2:
    rand1,rand2=genrand()
  
  os.system('clear')
  
  print("Great..!! Your current Score is :-"+str(score))
  print("Compare A : "+game_data.data[rand1]['name']+" a ,"+game_data.data[rand1]['description']+" from "+game_data.data[rand1]['country'])
  print(game_data.data[rand1]['follower_count'])
  
  print(art.vs)

  print("Compare B : "+game_data.data[rand2]['name']+" a ,"+game_data.data[rand2]['description']+" from "+game_data.data[rand2]['country'])
  print(game_data.data[rand2]['follower_count'])
  
  user=input("Who has more followers ? A or B ? :- ")
  if user=="A":
    if(int(game_data.data[rand1]['follower_count'])>int(game_data.data[rand2]['follower_count'])):
      print("correct")
      score+=1
    else:
      os.system('clear')
      print("Wrong.!! Game Over!!")
      print(score)
      flag=False

  elif user=="B":
    if(int(game_data.data[rand2]['follower_count'])>int(game_data.data[rand1]['follower_count'])):
      print("correct")
      score+=1
    else:
      os.system('clear')
      print("Wrong.!! Game Over!!")
      print(score)
      flag=False



  
