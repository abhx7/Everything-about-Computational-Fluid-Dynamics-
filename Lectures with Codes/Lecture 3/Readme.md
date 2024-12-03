# Notes

- Standard error [formula]
- Statistical error propagation in Addition
  - Chopping
    
    ![Equation](https://quicklatex.com/cache3/de/ql_08d5fad754bc908658a2ac515e955dde_l3.png)

  -  Rounding
    
     ![Equation](https://quicklatex.com/cache3/48/ql_9c20a688b3e44100a6e049826502ba48_l3.png)

- Condition Number : Ratio of relative error in f(x) to that of relative error in x. It relates to the problem's sensitivity to change in input values. Numerically unstable if the uncertainity of input values are magnified by numerical method.
-  Algorithm condition number vs Problem condition number (problems arise due to limitiation in digitized number representation)

- Roots of Non Linear Equations - with prior knowledge to find real roots only or finding all roots
  - Bracketing Methods: systematically reduce width of bracket, track error for convergence, Heron's method for root finding
    - Bisection (keep dividng the interval in 2 where atleast one root lies)
    - False position (one of the end points may remain fixed; can be modified by 'modifiying' it after a few iterations)
    
    Results are function dependent and are mostly expensive
  - Open methods: systematic trial and error scheme, computationally efficient but no guarantee on convergence
    - Open-point iteration (Fixed point or Picard iteration) :  rewrite the non linear equation f(x) as a linear combination of x and f(x), the c value should be chosen appropriately in x + c*f(x); the stop criteria is an or condition between if input change is less than epsilon or output of f(x) change is less than epsilon, the first should not be applied if the function is very flat and the other if the function is too steep
    - Newton-Raphson Method
    - Secant method
  - Roots of Polynomial
    - Open methods
    - Special methods             
