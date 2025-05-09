import numpy as np
import matplotlib.pyplot as plt
import pandas

#First function is to read the values of electric charges and their locations from a csv file, and populate a numpy array with their charge properties
def createChargeMatrix():



#Now take this numpy array(s) and process it
#Take in 2d matrix [r (charges), c (properties)] of elements of [x, y, q], where each element is a charge, x, y is the location and q is the charge of the charge in coulombs
def createVectorField(charges):
    #range is to find the max and min elements of y in the 2d matrix and then add some proportional padding to find the bounds of the graph of the vector field 
    #domain is the same as range but for the x properties of the charges
    #Step size: experiment with
    #use slicing and some min/max np func to find these, experiment with the padding once the graph is created to find the best amound, the initial estimate is going to be to add 10% to each side

    #Then use these ranges and domains and linspace along side meshgrid to create a coordinate grid to feed into the graph func
    #Then use the formula of /vec(E) to find the E_x and E_y return x,y,E_x and E_y, should use vectorize and an outside func to iterate 
    #over each charge and create the appropriate superposition of the electric field at that location
    CONST_K = 8.9875e9 #Coulombs constant

    range_min =  np.min(charges[:,1]) - (np.mean(charges[:,1]))*0.25
    range_max =  np.max(charges[:,1]) + (np.mean(charges[:,1]))*0.25
    domain_min = np.min(charges[:,0]) - (np.mean(charges[:,0]))*0.25
    domain_max = np.max(charges[:,0]) + (np.mean(charges[:,0]))*0.25  
    x, y = np.meshgrid(np.linspace(domain_min, domain_max, num = 1000), np.linspace(range_min, range_max, num = 1000), indexing='xy')

    #generate one vector field using a q and x pos
    E_x = np.array([])
    E_y = np.array([])


    for charge in charges:
        r = x - charge[0]
        E_temp = (charge[2])/(r**2) * np.abs(r)/r #q/r^2*unit(r)
        r = y - charge[1]
        E_temp = (r**2) * (1/charge[2]) * np.abs(r)/r #q/r^2*unit(r)
        
    
    
    

        
    



    

#Finally take in the vector field matrix and use it to generate a figure in matplotlib
def generateVectorField():



