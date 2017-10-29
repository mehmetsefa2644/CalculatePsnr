import skvideo.io
import skvideo.utils
import skimage.filters
import skimage.io
    
# define a function for calculating psnr
def psnr(img):
    mse = numpy.mean(img)
    return 10 * math.log10((255 * 255) / mse)

# read video
video = skvideo.io.vread('foreman.yuv')

# T is the number of total frames
T, M, N, C = video.shape

# apply gaussian filter for each frame
for x in range(1,T):
    video[x] = filters.gaussian(video[x])

# calculate psnr for each frame
for x in range(1,T):
    psnr += psnr(video[x])

# calculate the average psnr
averagePsnr = psnr/T

# print the average psnr
print(averagePsnr)

# visualize the first frame
skimage.io.imsave('foreman_frame1.png', video[0])


