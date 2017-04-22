# Pi_Monte_Carlo
A custom program to approximate Pi using a Monte Carlo simulation.
<br><br>
The approximation was built under the idea that:
<ol>
<li>The area of a square is 4r^2
<li>The area of a circle is pi*r^2
<li>The probability that a point will land inside the circle is (Area of Circle)/(Number of points used)
</ol>
With all this in mind, one can generate a random set of (x,y) and determine whether or not the set falls inside of the circle or not. Thus, if x^2 + y^2 <= 1 then add one to the circle count. 
<br><br>
At the end, you can find pi by isolating it...<br><br>
P(set will be inside of the circle) = (pi*r^2)/(4r^2) = pi/4 => pi = 4 * P(set inside of circle). Where as an algo, P(set inside...) is the circle count / number of points used.
