#!/usr/bin/env python
# coding: utf-8

# # Sudoko Solver using Backtracking

# In[12]:


# Dimensions of Sudoko Board
# 9x9 Sudoko Board
# 81 Numbers
# 1-9 Digits are Allowed


# In[13]:


# Dimension of each subboard = 3x3
subboardDim = 3

# Dimension of Sudoko Board
# 9x9 Board will contain 9 subboards
boardDim = 9


# In[14]:


sudokoBoard = [
               [5,3,0,0,7,0,0,0,0], 
               [6,0,0,1,9,5,0,0,0], 
               [0,9,8,0,0,0,0,6,0],
               [8,0,0,0,6,0,0,0,3],
               [4,0,0,8,0,3,0,0,1],
               [7,0,0,0,2,0,0,0,6],
               [0,6,0,0,0,0,2,8,0],
               [0,0,0,4,1,9,0,0,5],
               [0,0,0,0,8,0,0,7,9]
              ]


# In[15]:


numAllowed = list(range(1,10,1))
print(numAllowed)


# # Function Definitions

# In[16]:


# Function to Print Sudoko Board
def displayBoard(sudokoBoard):
    for i in sudokoBoard:
        for j in i:
            print(j,end=" ")
        print()
    print()


# In[17]:


# Function to check if the cell is empty or not

def isEmpty(sudokoBoard,row,column):
    # Check if the sudoko cell is valid
    # Check the following conditions
    # The cell should not contain any number, it should be either empty or should contain 0
    return not sudokoBoard[row][column]
        


# In[18]:


# Function to check if the value is allowed in the cell

def isValid(sudokoBoard,row,column,value):
    # Check if value exist in the row
    # Check if value exist in the column
    # Check if the value exist in the Sudoko Subboard
    for i in range(0,boardDim):
        if(sudokoBoard[row][i] == value):
            return False
        
    for i in range(0,boardDim):
        if(sudokoBoard[i][column] == value):
            return False
    
    # Dimensions of Sudoko Subboard
    subBoardRow = row//subboardDim
    subBoardCol = column//subboardDim
    
    for i in range(subBoardRow*subboardDim,(subBoardRow+1)*subboardDim,1):
        for j in range(subBoardCol*subboardDim,(subBoardCol+1)*subboardDim,1):
            if(sudokoBoard[i][j] == value):
                return False
            
    return True


# In[19]:


# Function to solve Sudoko Problem

def sudokoSolver(sudokoBoard,row,column):
    if row >= boardDim:
        displayBoard(sudokoBoard)
    
    else:
        if(isEmpty(sudokoBoard,row,column)):
            for i in numAllowed:
                if(isValid(sudokoBoard,row,column,i)):
                    sudokoBoard[row][column] = i
                    
                    # Proceed for next cell
                    if column < boardDim - 1:
                        sudokoSolver(sudokoBoard,row,column+1)
                    elif column == boardDim - 1:
                        sudokoSolver(sudokoBoard,row+1,0)
                
                        
                    # Backtracking Step
                    sudokoBoard[row][column] = 0
            
        elif(not isEmpty(sudokoBoard,row,column)):
            if column < boardDim - 1:
                        sudokoSolver(sudokoBoard,row,column+1)
            elif column == boardDim - 1:
                sudokoSolver(sudokoBoard,row+1,0)
            
    
    


# In[20]:


# Display Sudoko Board
print("Original Sudoko Board:")
displayBoard(sudokoBoard)

# Sudoko Solver
print("Sudoko Solver:")
sudokoSolver(sudokoBoard,0,0)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




