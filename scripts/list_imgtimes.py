from PIL import Image


def main():
    """
    Write the times of the images present in the directory into a text file.
    
    Parameters
    ---------- 
    imgnames.txt : text file
        Contains names of the images to be analyzed.

    Returns
    ------- 
    imgtimes.txt : text file
        Contains image times.

    """

    with open('imgnames.txt','r') as f:
        imgnames = f.read().splitlines()
    
    imgtimes = []
    for imgname in imgnames:
        obj_img = Image.open(imgname)
        imgtime = obj_img._getexif()[36867]
        imgtime = int(imgtime[11:13])*3600 + int(imgtime[14:16])*60 \
                      + int(imgtime[17:19])
        imgtimes.append(imgtime)
    
    with open("imgtimes.txt","w") as f:
        f.write('\n'.join(str(imgtime) for imgtime in imgtimes))


if __name__ == "__main__":
    main()


