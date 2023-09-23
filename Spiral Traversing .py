import turtle
import random

turtle.bgcolor("black")     # changing the bg color of the turtle winow
pen = turtle.Turtle()

width = 5
height = 7

dot_distance = 25

pen.penup()
list_color = ["white","violet","blue","green","yellow","orange","red"]
pen.setpos(-250,250)

def spiral(m,n):
    
    pen.color(random.choice(list_color))
    
    '''
    a --> 2D list
    m --> totol no. of rows
    n --> totol no. of columns
    k --> starting row index
    l --> starting column index
    '''
    k = 0
    l = 0
    f = 0
    
    while(k < m and l < n):
        
        
        if f == 1:
            pen.right(90)
            
        
        #print the first row from the remaining rows
        for i in range(l,n):
            pen.dot()
            pen.forward(dot_distance)
            #print(a[k][i], end = " ")
        k += 1  
        f = 1
        
        pen.right(90)
        
        pen.color(random.choice(list_color)) 
        
        # print the last column from the remaining
        for i in range(k,m):
            pen.dot()
            pen.forward(dot_distance)
            #print(a[i][n-1],end = " ")
            
        n -= 1
        
        
        pen.right(90)
        
        pen.color(random.choice(list_color))
        
        # last row of the remaining
        if k < m :
            for i in range(n-1,l-1,-1):
                pen.dot()
                pen.forward(dot_distance)
                #print(a[m-1][i],end = " ")
               
            m -= 1
        
        
        pen.right(90)
        
        pen.color(random.choice(list_color))
        # first column of the remaining        
        if l < n:
            for i in range(m-1, k-1, -1):
                pen.dot()
                pen.forward(dot_distance)
                #print(a[i][l],end = " ")
            l += 1 
                
    
a = []

spiral(20,20)