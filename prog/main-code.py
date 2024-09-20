from skimage.data import shepp_logan_phantom
from skimage.transform import radon, iradon, rescale
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
# for density
activity_level = 0.1;
# accssesinf ture object
true_object = shepp_logan_phantom();
true_object = rescale(activity_level * true_object, 0.5)
# six figures 2 rows 3 cloumns , 20 width and 10 length
fig, axs = plt.subplots (2, 3, figsize=(20, 10)) 
# show first plot object using gray scale for processing
axs [0, 0].imshow(true_object, cmap='Greys_r');
axs [0, 0].set_title('Object')

# Generate sinogram .
#using numby to go thruogh fron 0 degree to 180 degree
azi_angles = np.linspace(0.0, 180.0, 180, endpoint=False)
# apply radon transfrom on true object for mlutiple angles for the entire circular phantum
sinogram = radon(true_object, azi_angles, circle=False)
#show the sinogram plot in the first raw sec cloumn
axs [0, 1].imshow(sinogram.T, cmap='Greys_r');

axs [0, 1].set_title('Sinogram')

# applying the melem algrorithm

# iteration 0 (k = 0) first iteration
mlem_rec = np.ones(true_object.shape);
 # all ones array of sinogram for back projuction A^T 
sino_ones = np.ones (sinogram.shape)
# applying backprojuction by using iradon
sens_image = iradon(sino_ones, azi_angles, circle=False, filter_name=None)

for iter in range(20):
# forward projection of mlem_rec at iteration k (A x^k)
  fp = radon(mlem_rec, azi_angles, circle=False)
  # ratio sinogram m\(A x^k)
  ratio = sinogram / (fp+ 0.000001)
  # sensitivty range we obtain by applying also back projction -> other A^t
  correction = iradon (ratio, azi_angles, circle=False, filter_name=None) / sens_image
 
  axs [1, 0].imshow(mlem_rec, cmap='Greys_r');
  axs [1, 0].set_title('MLEM recon')
  axs [1, 1].imshow(fp.T, cmap='Greys_r');
  axs [1, 1].set_title('FP of recon')
  axs [0, 2].imshow(ratio.T, cmap='Greys_r');
  axs [0, 2].set_title('Ratio Sinogram')
  axs [1, 2].imshow(correction, cmap='Greys_r');
  axs [1, 2].set_title('BP of ratio')

  mlem_rec = mlem_rec * correction
  axs[1, 0].imshow(mlem_rec, cmap='Greys_r');
  axs[1, 0].set_title('MLEM recon image It=%d' % (iter+1))
  display(fig)
  clear_output(wait = True)
  plt.pause(0.5)
