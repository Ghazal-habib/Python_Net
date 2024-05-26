import json
q = { }

s = 0

number=1

g = open("questions.txt",'r')
q = json.load(g)
g.close()

print("Enter t , f ")
name = input("Enter your name: ")

for i in q :
    
    print("Question",number,": ", i)
    answer = input("The answer is ")
  
    if answer == q[i] :
        s = s + 1
      
   
        
    number = number + 1


result={name:s}
n = open("score.txt",'w')
result = json.dump(result,n)
n.close()