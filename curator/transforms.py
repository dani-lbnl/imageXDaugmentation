from numpy import np
import skimage

def transformAffineBatch(im,nofTransforms):
    """
        this function generates nofTransfor random affine transformations and applies them to image im
    """
    listOfPars = [np.vstack((np.reshape(random_pars,(2,3)),[0,0,1])) for i in range(nofTransforms)]
    listOfTransformedImages = [transform.warp(im,transform.AffineTransform(rotation = np.random.uniform(0,0.1*np.pi))) for par in listOfPars]
    return(listOfTransformedImages)
