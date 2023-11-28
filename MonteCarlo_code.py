import numpy as np
import matplotlib.pyplot as plt

class MonteCarlo:
    def __init__(self, radius, iterations, nthrows):
        self.radius = radius
        self.iterations = iterations
        self.nthrows = nthrows
        self.length = 2*radius
        self.coordinates = np.zeros((2, nthrows))
        
    def random_dart(self):
        x = np.random.choice(self.length)  
        y = np.random.choice(self.length)
        return x,y  
        
    def throw_darts(self):
        for i in range(self.nthrows):
            x,y = self.random_dart()
            self.coordinates [0] [i] = x
            self.coordinates [1] [i] = y
        return self.coordinates
    def check_circle(self):
    #want to check if the coordinate is smaller than the radius of the circle to confirm it is inside circle
        inside_circle = 0
        outside_circle = 0
        
        for i in range(self.nthrows):
            x = self.coordinates [0] [i]
            y = self.coordinates [1] [i]
            r = np.sqrt(x**2 + y**2)
            
        
            distance_x = x - self.radius
            distance_y = y - self.radius
        
            distance = np.sqrt(distance_x ** 2 + distance_y ** 2)
        
        
            if distance < self.radius:
                inside_circle += 1
                #print("inside")
                #print(distance)
            
        return inside_circle 
       
             
    def estimate_pi(self):
        #estimating pi with one experiment of nthrows
        self.throw_darts()
        circle_area = self.check_circle()
        square_area = self.nthrows
        pi = 4 * circle_area/square_area
        return pi 
     
    def monte_carlo_sim(self):
        results = []
        for i in range(self.iterations):
            estimate_of_pi = self.estimate_pi() 
            results.append(estimate_of_pi) 
        
        results = np.array(results) 
        pi_mean = np.mean(results)
        std_dev = np.std(results, ddof = 1)
        std_error = std_dev/np.sqrt(self.iterations)
        
        print (f'The estimated value of pi is: {pi_mean}')
        print (f'The standard error is: {std_error}')
            
    def visualization(self):
        #use coordinates in order to plot them onto the scatterplot
        plt.scatter(self.coordinates[0], self.coordinates[1], s=3, color='red')
        #adding aesthetic(s)/details to the scatterplot: title, labels, etc. 
        plt.title("Monte Carlo simulation")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
        