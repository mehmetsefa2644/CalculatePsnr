from skimage import data,io,filters,measure
import numpy,math

# define a function for calculating psnr
def psnr(img):
    mse = numpy.mean(img)
    return 10*math.log10((255*255)/mse)

# read the image
image = io.imread('cameraman.png')

# apply three filters
filterSobel = filters.sobel(image)
filterGaussian = filters.gaussian(image)
filterHessian = filters.hessian(image)

# calculate psnr's
sobelPsnr =  psnr(filterSobel)
gaussianPsnr = psnr(filterGaussian)
hessianPsnr = psnr(filterHessian)

# print psnr's
print(sobelPsnr)
print(gaussianPsnr)
print(hessianPsnr)

# save images
io.imsave('sobel.png', filterSobel)
io.imsave('hessian.png', filterHessian)
io.imsave('gaussian.png', filterGaussian)
