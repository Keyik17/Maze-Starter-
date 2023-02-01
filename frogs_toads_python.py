import time

#Returns two lists of inputs to True or Fals if the arrays match
def ArrayComparison(lilypad, solution):
    if lilypad == solution:
        return True 
    else:
        return False

#Defines and prints the array
def array(lilypad):
    for i in range(len(lilypad)):
        print(lilypad[i],end=" ")

lilypad = ['T','T','T',' ','F','F','F']
solution = ['F','F','F',' ','T','T','T']
turn = 1

#While the defined array is False continue until the solution
while ArrayComparison(lilypad, solution) != True:
    time.sleep(0.05)
    array(lilypad)
    print()
    
    for i in range(len(lilypad)):
		    if lilypad[i] == ' ':
			#Halfway point, switch turns or will lead to dead end
			    if lilypad[0] == 'F' and lilypad[1] == 'T' and lilypad[2] == ' ' and lilypad[3] == 'T' and lilypad[4] == 'F' and lilypad[5] == 'T' and lilypad[6] == 'F':
				    turn = 3 - turn

      
			#Jump Toad
			    if i-2>=0 and lilypad[i-1] == 'F' and lilypad[i-2] == 'T':
				    lilypad[i-2] = ' '
				    lilypad[i] = 'T'
				    break
		    
			#Jump Frog
			    if i+2<=6 and lilypad[i+1] == 'T' and lilypad[i+2] == 'F':
				    lilypad[i+2] = ' '
				    lilypad[i] = 'F'
				    break

			#Slide Toad
			    if turn == 1 and i-1>=0 and lilypad[i-1] == 'T':
				    lilypad[i-1] = ' '
				    lilypad[i] = 'T'
				    turn = 3 - turn
				    break

			#Slide Frog
			    if turn == 2 and i+1<=6 and lilypad[i+1] == 'F':
				    lilypad[i+1] = ' '
				    lilypad[i] = 'F'
				    turn = 3 - turn
				    break
#I apologize for not being able to complete the 3rd function.I had no idea on how to complete it.

array(lilypad)
print()
print("Yaaay! Complete. Good Job!")
