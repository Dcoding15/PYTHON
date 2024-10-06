# Simple Linear Regression

'''
Linear Regression Function: -
Regression Line Slope: -
y = m*x + c
            where, y -> predictated value or dependent variable
                   m -> slope or coefficient
                   x -> independent variable
                   c -> intercept at y
Hypothesis: -
theta_h(x) = theta_0 + theta_1*x_1 + ... +  theta_n*x_n
                                  where, theta_h(x)             -> hypothesis function
                                         theta_0                -> y-intercept
                                         theta_1, ... , theta_n -> slope of regression line
                                         x_1, ... , x_n         -> independent variables

Cost Function or Squared Error Function: -
J(theta_0,theta_1) = 1/(2*i) summation(theta_h(x_i) - y_i)^2
                                                             where, m -> no. of datapoints
                                                                    i -> starts from 0 to m

Convergence Theorem: -
theta_j := theta_j - lamda(derivative of theta_j(J(theta_0,theta_1))
                                                                    where, theta_j -> theta object which is minima of gradient descent
                                                                           lamda   -> learning rate which is best at low value
'''
