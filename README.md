# ImageXDaugmentation
- Motivation: one of the requirements to run CNN is to have a large dataset. But what if you have only a small labelled dataset? You can perform augmentation, which means that you can generate different images from your originally curated data.

### Data augmentation for curated data:
- data augmentation tool to embed additional variations to your dataset without the cost of collecting and annotating more data, but with assumptions that make sense
- how to propagate curated data in such a way to increase number of labelled data

### Team:
Dani Ushizima (materials)
Rahul Biswas (astronomy)
Valentina Staneva (biomedical)

### How everything started:
1) Brainstorming
- menu with options for image augmentation
- affine transformations: translation, scaling, homothety, similarity transformation,reflection, rotation, shear mapping, and compositions, projective
parameterization: should it be random?
http://scikit-image.org/docs/dev/api/skimage.transform.html#skimage.transform.AffineTransform
- filtering associated to transformations, e.g. mimicking out-of-focus
changes in illumination,
-occlusions, nonlinear transformations, time shifting, background substitution, periodicity, noise, PCA
- symmetries:
- bilateral
- radial
- biradial
- image is periodic?
- noise models:
- white noise
- speckle noise
- background substitution: how to best interpolate when there is no
- resizing by cropping
- padding
- PCA and then generate new images based on them
- tools/infographics that evaluates divergence from original set
- keep images in their original file format - then should it export LMDB?
- labels: objects within an image or 1 object per image
- specification of the input: curated data
- image + mask (sparse or not)
- image + csv
- transformations associated to elastic deformation, e.g., suggest that for material sciences, a subset of transformation would be more suitable than others
- Check Daniil's blog with needs before deep learning:
http://warmspringwinds.github.io/gsoc/2015/07/24/google-summer-of-code-creating-training-set/
- blog from winning Plankton classification challenge
http://benanne.github.io/2015/03/17/plankton.html
- documentation w/ illustrated pictures, e.g. why/how could I use radial symmetry? 
http://jwilson.coe.uga.edu/EMT668/EMAT6680.2002.Fall/Nazarewicz/7210_final_2/7210_Project/
2) Story-telling
User enter images that are all the same size, not necessary squared + (new_filename,class,orig_filename)
User define a set of image transformations
Output contains new set of images + csv (new_filename,class,orig_filename) + log (what was used during transformation)
