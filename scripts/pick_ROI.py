import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle


def main():
    """
    Pick the top-left and bottom-right corner of the region of interest (ROI).
    
    Parameters
    ---------- 
    imgnames.txt : text file
        Contains the names of the images to be anaylized.
    
    Returns
    -------
    ROI_corners.dat : text file
        Contains the coordinates of the top-left and bottom-right corners of
        the region of interest.

    """

    with open('imgnames.txt','r') as f:
        name_refimg = f.readline().strip()

    refROI = drawROI(name_refimg)
    plt.show()


class drawROI(object):
    def __init__(self, imgname):
        fig, self.axis = plt.subplots()
        self.rect = Rectangle((0,0),1,1, facecolor='None', edgecolor='green',
                              linewidth=3)
        self.axis.add_patch(self.rect)
        figtitle = plt.title("L-click on top-left; drag to bottom-right." \
                             " a to accept, r to redo, q to quit.")
        img = mpimg.imread(imgname)
        plt.imshow(img)
        # Maximize figure window
        figmng = plt.get_current_fig_manager()
        figmng.resize(*figmng.window.maxsize())
        self.is_lclick_on=False
        self.TLX = None
        self.TLY = None
        self.BRX = None
        self.BRY = None
        self.axis.figure.canvas.mpl_connect('button_press_event',
                                            self.lclick_on)
        self.axis.figure.canvas.mpl_connect('button_release_event',
                                            self.lclick_off)
        self.axis.figure.canvas.mpl_connect('motion_notify_event',
                                            self.lclick_drag)
        self.axis.figure.canvas.mpl_connect('key_press_event', self.key_on)


    def key_on(self,event):
        if event.key=='q':
            plt.close(event.canvas.figure)
        elif event.key=='r':
            self.rect.set_width(1)
            self.rect.set_height(1)
            self.rect.set_xy((0,0))
            self.axis.figure.canvas.draw() 
        elif event.key=='a':
            with open('ROI_corners.dat','w') as f:
                f.write("%s: %i\n" %("TLX", self.TLX))
                f.write("%s: %i\n" %("TLY", self.TLY))
                f.write("%s: %i\n" %("BRX", self.BRX))
                f.write("%s: %i\n" %("BRY", self.BRY))
                plt.close(event.canvas.figure)


    def redrawRect(self,event):
        self.BRX = int(event.xdata)
        self.BRY = int(event.ydata)
        self.rect.set_width(self.BRX-self.TLX)
        self.rect.set_height(self.BRY-self.TLY)
        self.rect.set_xy((self.TLX,self.TLY))
        self.axis.figure.canvas.draw() 


    def lclick_on(self,event):
        self.is_lclick_on = True
        self.TLX = int(event.xdata)
        self.TLY = int(event.ydata)


    def lclick_drag(self,event):
        if self.is_lclick_on:
            self.redrawRect(event)


    def lclick_off(self,event):
        self.is_lclick_on=False
        self.redrawRect(event)


if __name__ == "__main__":
    main()
