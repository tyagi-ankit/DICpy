import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def main():
    """
    Show the grid on the reference image.
    
    Parameters
    ---------- 
    imgnames.txt : text file
        Contains names of images.
    
    """

    # Read reference image name
    f = open('imgnames.txt','r')
    name_refimg = f.readline().strip()
    f.close() 
    
    # embed reference image into the plot object
    fig, axis = plt.subplots()
    title = "ROI Grid"
    plt.title(title)
    refimg = mpimg.imread(name_refimg)
    nof_ypixels,nof_xpixels,nof_colors = np.shape(refimg)
    plt.imshow(refimg)
    # Maximize figure window
    figmng = plt.get_current_fig_manager()
    figmng.resize(*figmng.window.maxsize())
    
    # Read ROI grid coordinates
    gridx = np.loadtxt('gridx.dat')
    gridy = np.loadtxt('gridy.dat')
    
    nof_rows,nof_cols = np.shape(gridy)
    
    for row in range(nof_rows):
        plt.plot(gridx[row,:],gridy[row,:],color='green',linewidth=1.2)
    
    for col in range(nof_cols):
        plt.plot(gridx[:,col],gridy[:,col],color='green',linewidth=1.2)
    
    axis.set_xlim([0,nof_xpixels])
    axis.set_ylim([0,nof_ypixels])
    axis.invert_yaxis()
    plt.show()


if __name__ == "__main__":
    main()
