import math
import numpy as np


def main():
    """
    Create grid in the region of interest.
    
    Parameters
    ---------- 
    gridgap : int
        Number of pixels denoting the size of the square grid.
    ROI_corners.dat : text file
        Containing the coordinates of the top-left and bottom-right corners of
        the region of interest.
    
    Returns
    -------
    gridx.dat : text file
        Contains the x coordinates of the grid.
    gridy.dat : text file
        Contains the y coordinates of the grid.
    
    """

    gridgap = 50
    
    with open("ROI_corners.dat",'r') as f:
        ROI_corners = f.read().splitlines()
    
    grid_TLX = float(ROI_corners[0].split()[1])
    grid_TLY = float(ROI_corners[1].split()[1])
    grid_BRX = float(ROI_corners[2].split()[1])
    grid_BRY = float(ROI_corners[3].split()[1])
    
    nof_gridcols = math.ceil((grid_BRX - grid_TLX)/gridgap) - 1.0
    nof_gridrows = math.ceil((grid_BRY - grid_TLY)/gridgap) - 1.0
    
    grid_TLX_new = (grid_TLX+grid_BRX)/2.0 - nof_gridcols*gridgap/2.0
    grid_TLY_new = (grid_TLY+grid_BRY)/2.0 - nof_gridrows*gridgap/2.0
    grid_BRX_new = (grid_TLX+grid_BRX)/2.0 + nof_gridcols*gridgap/2.0
    grid_BRY_new = (grid_TLY+grid_BRY)/2.0 + nof_gridrows*gridgap/2.0
    
    gridx_vec = np.linspace(grid_TLX_new,grid_BRX_new,nof_gridcols+1)
    gridy_vec = np.linspace(grid_TLY_new,grid_BRY_new,nof_gridrows+1)
    
    gridx,gridy = np.meshgrid(gridx_vec,gridy_vec)
    
    np.savetxt('gridx.dat',gridx,delimiter='\t')
    np.savetxt('gridy.dat',gridy,delimiter='\t')


if __name__ == "__main__":
    main()
