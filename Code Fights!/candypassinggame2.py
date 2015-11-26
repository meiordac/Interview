
def candyPassingGameTwo(N, M):
  players=[j for j in range(N)]
  h=0
  for i in range(len(M)):
    while M[i]>0:
      if h>=len(players):
	h=0
      M[i]-=1
      h+=1 
      if h>=len(players):
	h=0
      if M[i]==0 and len(players)>1:
	players.pop(h)
  if players[0]==0:
    return -1
  return players[0]
	  


print(candyPassingGameTwo(2,[1]))