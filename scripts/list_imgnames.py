import os


def main():
    """
    Write the names of the images present in the directory into a text file.
    
    Parameters
    ---------- 
    imgextension : str
        Extension of the image files.

    Returns
    -------
    imgnames.txt : text file
        Contains image names.

    """

    imgextension = "JPG"
    imgnames = [img for img in os.listdir('.') if img.endswith(imgextension)]
    imgnames.sort()

    with open('imgnames.txt','w') as f:
        f.write('\n'.join(imgnames))


if __name__ == "__main__":
    main()
