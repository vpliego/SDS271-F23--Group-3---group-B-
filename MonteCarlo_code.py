import numpy as np
class MonteCarlo:
    def __init__(self, radius, iterations, nthrows):
    # Initializing a monteCarlo method with radisu,iterations, and nthrows as parameters
        self.radius = radius
        self.iterations = iterations
        self.nthrows = nthrows
        self.length = 2*radius
   # initlaizlize a 2D NumPy array as the attribute of the MonteCarlo class.
        self.coordinates = np.zeros((2, nthrows))
    def random_dart(self):
    # Generating the random coordinates(x,y) for the nthrows for the monteCarlo stimulation. It returns the coordiantes.
        x = np.random.choice(self.length)
        y = np.random.choice(self.length)
        return x,y
    def throw_darts(self):
    # Creates random numbers of dart throws and store them in the coordinates
        for i in range(self.nthrows):
            x,y = self.random_dart()
            self.coordinates [0] [i] = x
            self.coordinates [1] [i] = y
    def check_circle(self):
    #want to check if the coordinate is smaller than the radius of the circle to confirm it is inside circle

    # Checks for thif the coordinate is smaller than the radius of the circle to confirm it is
        #inside the circle. Then it returns an integer the number of darts inside circle.
        inside_circle = 0
        outside_circle = 0
    # The for loop iterates through each nnumber of throws and updates the coordinates
        for i in range(self.nthrows):
            x = self.coordinates [0] [i]
            y = self.coordinates [1] [i]
    # Radius is used to find the distance of coordinates from origin.
            r = np.sqrt(x*2 + y*2)
            distance_x = x - self.radius
            distance_y = y - self.radius
            distance = np.sqrt(distance_x ** 2 + distance_y ** 2)
        # if distance < radius of the circle the point falls inside the circle.
            if distance < self.radius:
                inside_circle += 1
                #print("inside")
                #print(distance)
        return inside_circle
    
    def estimate_pi(self):
        # estimating pi with one experiment of nthrows, using Montecarlo stimulation.It returns a float(pi_value)
        self.throw_darts()
        circle_area = self.check_circle()
        square_area = self.nthrows
    # knowing the ratio of area for a circle is pi/4, we find the pi value as following
        pi = 4 * circle_area/square_area
        return pi
    
    def monte_carlo_sim(self):
        #create a list where the results can be stored inside
        results = []
        #for loop that uses the range of number of iterations to estimate pi, then append this to the results list.
        for i in range(self.iterations):
            estimate_of_pi = self.estimate_pi() 
            results.append(estimate_of_pi) 
        #turn the results list into an array
        results = np.array(results) 
        #calculate the mean
        pi_mean = np.mean(results)
        #calculate std deviation
        std_dev = np.std(results, ddof = 1)
        #calculate std error using std deviation.
        std_error = std_dev/np.sqrt(self.iterations)
        
        #print these values
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
        
        
