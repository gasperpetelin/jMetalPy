## jMetalPy: Python version of the jMetal framework

I have just started a new project called jMetalPy. The initial idea is not to write the whole jMetal proyect in Python, but to "have fun": I'm starting with Python, and to learn this programming language I think that using jMetal as a case study would be nice.

Any ideas about how the structure the project, coding style, useful tools (I'm using PyCharm), or links to related projects are welcome. The starting point is the jMetal architecture:

![jMetal architecture](resources/jMetal5UML.png)

# Current status (May 9th 2017)
The current implementation contains the following features: 
* Algorithms (single-objective)
  * (mu+lamba)Evolution Strategy
  * (mu,lamba)Evolution Strategy
  * Generational Genetic algorithm
* Problems (multi-objective)
  * Kursawe
  * Fonseca
  * Schaffer
  * Viennet2
* Problems (single-objective)
  * Sphere
  * OneMax
* Encoding
  * Float
  * Binary
* Operators
  * SBX Crossover
  * Single Point Crossover
  * Polynomial Mutation
  * Bit Flip Mutation
  * Simple Random Mutation
  * Null Mutation
  * Uniform Mutation
  * Binary Tournament Selection

