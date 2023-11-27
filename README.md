# PROMPT

Write a class that does the following uses a Monte Carlo simulation to calculate $\pi$ using the ratio of areas for a square of side length 2 and a circle of radius 1. 

Remember that


$A_c= \pi R^2$

$A_s=L^2 = (2R)^2$

Your class should:

1. store the length, radius, number of monte carlo iterations, and number of dart throws as internal attributes (you can choose between class and instance attributes as you see fit)
2. simulate some large (but variable) number of dart throws inside the square
3. calculate how many of those throws also landed inside the circle if the circle is centered in the middle of the square
4. store the results of each experiment (set of dart throws) in a dataframe
5. use the relationship between the area of a circle and the area of a square to estimate pi from those two numbers (with error!)
6. create a visualization of the simulation (the dart throws on the circle/square)
7. return the estimate of pi along with the standard error on that estimation





# Class MonteCarlo

The class MonteCarlo aims to use a monte carlo simulation in order to estimate pi for each iteration of dart throwing that is simulated. This class will also work to count how many times the dart throws land inside the circle based on whether the distance of the dart coordinate is less than the radius of the circle. We do this using the following internal attributes and methods listed below. 


# List of class internal attributes: 

**radius:** This internal attribute will be used in a function called check_circle() which will check whether the dart throw falls within the circle or not. It will also be used in the internal attribute called length in order to calculate the length of the square. In order to check whether the coordinates of the dart throw is in the circle using the check_circle(), however, it will need the radius to do a simple calculation of seeing how far this point is from the radius. From there, it can be used to compute the actual distance of the coordinate and confirm whether the throw landed in the circle or not. 

**iterations:** This internal attribute will be used to specify how many iterations we will want to see the monte carlo simulation carry out with the dart throws.

**nthrows:** This internal attribute will take in a value for the number of throws the user is doing.

**length:** This internal attribute sets the value for the length of the square which is 2*radius. 

**coordinates:** This internal attribute creates an empty array of zeros that is two dimensional and will have a maximum value of nthrows.


# List of class internal methods: 

**__init__(self, radius, iterations, nthrows):** This is the constructor function and will initialize the class when an instance is created.

**random_dart(self):** This function will create random dart coordinates x,y for a dart throw and return x,y. 

**throw_darts(self):** This function will simulate the actual dart throws using the random_dart() and nthrows(number of throws) in order to store these coordinates in the "coordinates" internal attribute of the function. This function helps create the actual coordinates of the dart throws themselves as previously, our coordinates attribute was only an empty array of zeros. 

**check_circle(self):** This function does the main thing that this class is intended to do which is find how many times when a dart gets thrown, will it land inside this circle. So, this function finds whether the distance of our coordinates is less than the radius of the circle (as previously mentioned in the internal attributes portion, one of the uses of the radius attribute), and if it is then it'll increase the count for number of times the dart is inside the circle. 

**estimate_pi(self):** This function will be estimating pi based on what we know about the ratios of the area of a circle and area of a square to the number of dart throws.

**monte_carlo_sim(self):** This function will be doing the actual monte carlo simulation based on the number of iterations that are specified when the attribute is given a value for the number of iterations. 

**visualization(self):** This function will be responsible for creating a visualization of the simulation using the coordinates.

