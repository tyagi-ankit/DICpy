import numpy as np


def findpeak(f, subpixel):
    """
    Find extremum of a matrix.

    XPEAK, YPEAK, MAX_F = FINDPEAK(F, SUBPIXEL) finds the extremum of F, MAX_F,
    and its location (XPEAK, YPEAK). F is a matrix. MAX_F is the maximum
    absolute value of F, or an estimate of the extremum if a sub-pixel extremum
    is requested.

    SUBPIXEL is a boolean that controls if FINDPEAK attempts to estimate the
    extremum location to sub-pixel precision. If SUBPIXEL is false, FINDPEAK
    returns the coordinates of the maximum absolute value of F and MAX_F is
    np.amax(np.abs(F)). If SUBPIXEL is true, FINDPEAK fits a 2nd order
    polynomial to the 9 points surrounding the maximum absolute value of F. In
    this case, MAX_F is the absolute value of the polynomial evaluated at its
    extremum.

    Note
    ----    
    Even if SUBPIXEL is true, there are some cases that result in FINDPEAK
    returning the coordinates of the maximum absolute value of F:
    #. When the maximum absolute value of F is on the edge of matrix F.
    #. When the coordinates of the estimated polynomial extremum would fall
    outside the coordinates of the points used to constrain the estimate.

    """

    # Get the absolute peak pixel.
    max_f = np.amax(np.abs(f))
    ypeak, xpeak = np.argmax(np.abs(f))

    if (subpixel and xpeak!=0 and xpeak!=np.shape(f)[1] and ypeak!=0 and
            ypeak!=np.shape(f)[0]):  # Not on the edge.
        # Fit a 2nd order polynomial to 9 points.
        # Using 9 pixels centered on ypeak, xpeak
        u = f[ypeak-1:ypeak+1, xpeak-1:xpeak+1]
        u = u.flatten('F')  # Flatten in column-major (Fortran-style).
        x = np.array([-1, -1, -1, 0, 0, 0, 1, 1, 1])
        y = np.array([-1, 0, 1, -1, 0, 1, -1, 0, 1])

        # u(x,y) = A(1) + A(2)*x + A(3)*y + A(4)*x*y + A(5)*x^2 + A(6)*y^2
        X = np.column_stack((np.ones(9),  x,  y,  x*y,  x**2,  y**2))
        
        # u = X*A.
        A = np.linalg.solve(X, u)

        # Get the absolute maximum, where du/dx = du/dy = 0
        x_offset = (2*A[1]*A[5] - A[2]*A[3]) / (A[3]**2 - 4*A[4]*A[5])
        y_offset = (A[1]*A[3] - 2*A[2]*A[4]) / (4*A[4]*A[5] - A[3]**2)

        if np.abs(x_offset)<1 and np.abs(y_offset)<1:
            # adjusted peak falls inside the set of 9 points fit.
            # Return only one-thousandth of a pixel precision.
            x_offset = np.around(1000*x_offset)/1000
            y_offset = np.around(1000*y_offset)/1000    
            
            xpeak = xpeak + x_offset
            ypeak = ypeak + y_offset    
            
            # Calculate extremum of fitted function.
            max_f = np.array([1, x_offset, y_offset, x_offset*y_offset,
                              x_offset^2, y_offset^2]) * A
            max_f = np.abs(max_f)

    return xpeak, ypeak, max_f
