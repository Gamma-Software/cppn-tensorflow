import numpy as np
import math
import random
import PIL
from PIL import Image
import pylab
from model import CPPN
import matplotlib.pyplot as plt
import images2gif
from images2gif import writeGif
from sampler import Sampler
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

sampler = Sampler(z_dim = 8, c_dim = 3, scale = 10.0, net_size = 32)
z1 = sampler.generate_z()
img_data = sampler.generate(z1)
sampler.save_png(img_data, "image.png")
