import numpy as np

def gradient_decent(x,y):
    m_curr = b_curr = 0
    iteration = 1000000
    n = len(x) # length of the data poitns
    learning_rate = 0.0002
    for i in range(iteration):
        y_predicted = m_curr *x + b_curr
        cost = (1/n)*sum([val*val for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted)) # derivative of m 
        bd = -(2/n)*sum((y-y_predicted)) # derivative of b
        m_curr = m_curr - learning_rate *md
        b_curr = b_curr - learning_rate *bd
        print("m {}, b {}, cost {} , iteration {}".format(m_curr,b_curr,cost,i))


math  = np.array([92, 56, 88 ,70 ,80, 49 ,65 ,35, 66, 67 ])
cs  = np.array([98 ,68, 81, 80,83 ,52, 66 ,30 ,68 ,73])

gradient_decent(math,cs)