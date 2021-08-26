import sys
from sampler import Sampler
import argparse
import tensorflow.compat.v1 as tf
import os
import datetime
import matplotlib.pyplot as plt
import gc
import time
tf.disable_v2_behavior()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Personal information')

    parser.add_argument('--folder', dest='folder', type=str, help='Folder where the images are stored')
    parser.add_argument('--passwd', dest='passwd', type=str, help='pass of the ftp logging')
    parser.add_argument('--color', dest='color', type=str, help='color')
    parser.add_argument('--width', dest='width', type=int, help='width')
    parser.add_argument('--height', dest='height', type=int, help='height')
    parser.add_argument('--mode', default="3tan_sigmoid", dest='mode', type=str, help='3tan_sigmoid, 3tan_sqrt, tan_softplus, sigmoid_tan_softplus, 4residualtan')
    
    args = parser.parse_args()

    #sampler = Sampler(z_dim = 4, c_dim = 1 if args.color == "bw" else 3, scale = 8.0, net_size = 32)
    sampler = Sampler(z_dim = 6, c_dim = 3, scale = 8.0, net_size = 16) # NICE COLORS
    #sampler = Sampler(z_dim = 8, c_dim = 1, scale = 8.0, net_size = 16) # VERY GLORY
    #sampler = Sampler(z_dim = 6, c_dim = 1, scale = 8.0, net_size = 24)

    z1 = sampler.generate_z()
    z2 = sampler.generate_z()    
    sampler.save_anim_gif(z1, z2, n_frame=100, filename='output.gif')
