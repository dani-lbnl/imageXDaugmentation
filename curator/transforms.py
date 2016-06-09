from numpy import np
import skimage

def transformAffineBatch(im,nofTransforms):
    """
        this function generates nofTransfor random affine transformations and applies them to image im
    """
    listOfTransformedImages = [transform.warp(im,transform.AffineTransform(rotation = np.random.uniform(0,0.1*np.pi))) for par in listOfPars]
    return(listOfTransformedImages)
