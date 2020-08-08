# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:28:55 2020

@author: This_PC
"""






 

# pulp is one such library which is used for the optimization of linear programming
# import the library pulp 
import pulp as p 
import matplotlib.pyplot as plt #it is used for creating scatter line bars, charts, figure, scatter plots etc.
import numpy as np # a whole-some package for performing basic scientific operations 

#tutorial on matplitlib
# https://www.tutorialspoint.com/matplotlib/matplotlib_pyplot_api.htm

#########################################
# Very basic example of linear Programming 
##########################################


# 1.  Problem 1 
# Minimize :  Z = 3x + 5y
#Subject to the constraints: 
# 2x + 3y >= 12
# -x + y <= 3
# x >= 4
# y <= 3
# x, y >= 0

  
# Brief explanation on working of the functions
# First importing the library as p
# LpProblem is a function defined in the pulp, having two parameters name and declaration of maximize/minimizing of function
# LpVariable hold the variables of the objective functions. lower and upper bound of a variable can be defined,
   # if not defined then default value will be taken
# Lp_prob represents the objective function in terms of defined variables 
  # It holds all informtaion regarding variables and the problem 
  # using + sign will store the variables and its coefficients in there respective slots  
   
def example1():
    Lp_prob = p.LpProblem('Problem', p.LpMinimize)  
  
    # Create problem Variables  
    x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
    y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 
  
    # Objective Function 
    Lp_prob += 3 * x + 5 * y    # x, and y are defined variables 
  
    # Constraints: 
    Lp_prob += 2 * x + 3 * y >= 12 
    Lp_prob += -x + y <= 3
    Lp_prob += x >= 4
    Lp_prob += y <= 3
  
    # Display the problem 
    print(Lp_prob) 
  
    status = Lp_prob.solve()   # Calling the default Solver  (CBC - coin or branch and cut)
    print(p.LpStatus[status])   # The solution status  if 1-optimal, 0- no solution 
  
    # Printing the final solution 
    print(p.value(x), p.value(y), p.value(Lp_prob.objective)) 
    
    z = np.linspace(0, 200, 100) # store 10000 points in the range of 0, 600 in the form of list 
    #Constraints
    y1 = (12- 2*z)/3  # rewriting the constarints 
    y2 = 3+z
    # Make plot with the following arguments 
    plt.plot(z, y1, label=r'$2x+3y\geq12$')  
    plt.plot(z, y2, label=r'$-x+y\leq3$')
    # defining the rant=ge of both the axes
    plt.xlim((0, p.value(x)+ 10)) 
    plt.ylim((0, p.value(x)+ 10))
    #Labelling X and Y axis
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    # Fill feasible region
    y5 = np.minimum(y2, y1)
    plt.fill_between(z, y5, color='pink',alpha=0.5)
    plt.legend(bbox_to_anchor=(1.5, 1), loc=5, borderaxespad=0.)
    plt.show()

# Hard wired Programming can be extended up to multiple variables
##############################################################
# 2. Problem 2 

# Assest/ liability cash-flow matching
 # max w
 #c1+p1−e1= 150
 #c2+p2+ 1.003e1−1.01c1−e2= 100
 #c3+p3+ 1.003e2−1.01c2−e3=−200
 #c4−1.02p1−1.01c3+ 1.003e3−e4= 200
 #c5−1.02p2−1.01c4+ 1.003e4−e5=−50
 #−1.02p3−1.01c5+ 1.003e5−w=−300
 #0 ≤ ci ≤100,
 #1≤ i ≤5
 #pi>0,1≤i≤3
 #ei≥0,1≤i≤5


def example2():
    Lp_prob = p.LpProblem('Problem', p.LpMaximize) 
    #c = p.LpVariable.dicts(f"c[i]",(i for i in range(1,6)),lowBound=0, upBound=100)
    c= {i:p.LpVariable(name=f"c{i}", lowBound=0, upBound= 100) for i in range(1, 6)}
    e= {i:p.LpVariable(name=f"e{i}", lowBound=0) for i in range(1, 6)}
    pi= {i:p.LpVariable(name=f"pi{i}", lowBound=0) for i in range(1, 4)}
    w = p.LpVariable("w") 

    #objective function 
    Lp_prob += w

    # adding constraints
    Lp_prob += c[1]+pi[1]- e[1] == 150
    Lp_prob += c[2]+pi[2]+1.003*e[1]-1.01*c[1]-e[2] == 100
    Lp_prob += c[3]+pi[3]+1.003*e[2]-1.01*c[2]-e[3] == -200
    Lp_prob += c[4]-1.02*pi[1]-1.01*c[3]+1.003*e[3]-e[4] == 200
    Lp_prob += c[5]-1.02*pi[2]-1.01*c[4]+1.003*e[4]-e[5] == -50
    Lp_prob += -1.02*pi[3]-1.01*c[5]+1.003*e[5]-w == -300

    print(Lp_prob) 

  
    status = Lp_prob.solve()   # Solver 
    print(p.LpStatus[status])   # The solution status 
  
    # Printing the final solution
 

    for var in c.values():
        print(f"{var.name}: {var.value()}")

    for var in e.values():
        print(f"{var.name}: {var.value()}")
        
    for var in pi.values():
        print(f"{var.name}: {var.value()}")

    for name, constraint in Lp_prob.constraints.items():
        print(f"{name}: {constraint.value()}")
    
    print( p.value(Lp_prob.objective)) 
    
    

#############################################################################
    #Problem 3
    # Maximize :  Z = 500x + 450y
    #Subject to the constraints: 
    # x + 5/6 y <=10
    # x +2y <= 15
    # x <= 8
    # x, y >= 0


def example3():
    Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
  
    # Create problem Variables  
    x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
    y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 
  
    # Objective Function 
    Lp_prob += 500 * x + 450 * y    
  
    # Constraints: 
    Lp_prob += x + 5/6 * y <= 10
    Lp_prob += x + 2*y <= 15
    Lp_prob += x <= 8
  
    # Display the problem 
    print(Lp_prob) 
  
    status = Lp_prob.solve()   # Solver 
    print(p.LpStatus[status])   # The solution status 
  
    # Printing the final solution 
    print(p.value(x), p.value(y), p.value(Lp_prob.objective)) 

    ### for graphical represenation 
    z = np.linspace(0, 600, 10000)
    #Constraints
    y1 = (10- z)/(5/6)
    y2 = (15-z)/2
    # Make plot
    plt.plot(z, y1, label=r'$x+5/6y\leq10$')
    plt.plot(z, y2, label=r'$x+2y\leq15$')
    plt.xlim((0, p.value(x)+ 10))
    plt.ylim((0, p.value(x)+ 10))
    #Labelling X and Y axis
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    # Fill feasible region
    y5 = np.minimum(y2, y1)
    plt.fill_between(z, y5, color='pink',alpha=0.5)
    plt.legend(bbox_to_anchor=(1.5, 1), loc=5, borderaxespad=0.)
    plt.show()


###########################################################################
    ## starting point of a program
    # Main function calls three function that are defined above. 

if __name__=='__main__':
    # while is a conditional statement used to excuted statemnet within when a condition is triggered 
    while True:  
        str = int(input("Run example??"))  # Read an input from the user and convert it into int. 
        if str ==1:
            example1()
        else:
            if str ==2:
                example2()
            else:
                if str ==3:
                    example3()
                else:
                    break















