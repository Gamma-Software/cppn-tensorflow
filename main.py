import sys
from sampler import Sampler
import argparse
import tensorflow.compat.v1 as tf
import os
import datetime
import matplotlib.pyplot as plt
tf.disable_v2_behavior()

def send_image_ftp(passwd, files):
    import ftplib
    session = ftplib.FTP('mafreebox.freebox.fr')
    with open(passwd, "r") as f:
        session.login(f.readline().strip("\n"), f.readline().strip("\n"))
    session.cwd("PiValNas/abstract_art")
    folder_to_store = datetime.datetime.now().strftime("%Y_%m_%d")
    session.mkd(folder_to_store)
    for file in files:
        with open(file,'rb') as f:
            session.storbinary('STOR ' + os.path.join(folder_to_store, os.path.basename(file)), f)     # send the file
    session.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Personal information')

    parser.add_argument('--gif', dest='gif', default=False, type=bool)
    parser.add_argument('--folder', dest='folder', default="images/", type=str, help='Folder where the images are stored')
    parser.add_argument('--nb', dest='nb', default=20, type=int)
    parser.add_argument('--passwd', dest='passwd',  default="pass.txt", type=str, help='pass of the ftp logging')
    parser.add_argument('--color', dest='color', default="bw", type=str, help='color')
    parser.add_argument('--width', dest='width', type=int, default=512, help='width')
    parser.add_argument('--height', dest='height', type=int, default=512, help='height')
    parser.add_argument('--mode', default="3tan_sigmoid", dest='mode', type=str, help='3tan_sigmoid, 3tan_sqrt, tan_softplus, sigmoid_tan_softplus, 4residualtan')
    
    args = parser.parse_args()

    #sampler = Sampler(z_dim = 4, c_dim = 1 if args.color == "bw" else 3, scale = 8.0, net_size = 32)
    #sampler = Sampler(z_dim = 6, c_dim = 3, scale = 8.0, net_size = 16) # NICE COLORS
    #sampler = Sampler(z_dim = 8, c_dim = 1, scale = 8.0, net_size = 16) # VERY GLORY
    sampler = Sampler(z_dim = 6, c_dim = 1 if args.color == "bw" else 3, scale = 8.0, net_size = 24)

    files = list()

    if args.gif:
        z1 = sampler.generate_z()
        z2 = sampler.generate_z()
        sampler.save_anim_gif(z1, z2, n_frame=100, filename=args.folder+"output.gif")
        files.append(args.folder+"output.gif")
    else:
        z = sampler.generate_z()
        for i in range(args.nb):
            sampler.reinit()
            sampler.save_png(sampler.generate(z, x_dim=500, y_dim=500, mode=args.mode, scale=8), args.folder+"/image"+str(i)+".png")
            files.append(args.folder+"/image"+str(i)+".png")
            i += 1

        for i in range(args.nb):
            sampler.reinit()
            sampler.save_png(sampler.generate(z, x_dim=500, y_dim=500, mode="4residualtan", scale=8), args.folder+"/image"+str(args.nb+1+i)+".png")
            files.append(args.folder+"/image"+str(args.nb+1+i)+".png")
            i += 1

        #fig = plt.figure()
        for i in range(args.nb):
            sampler.reinit()
            sampler.save_png(sampler.generate(z, x_dim=500, y_dim=500, mode="3tan_sqrt", scale=8), args.folder+"/image"+str(args.nb*2+1+i)+".png")
            files.append(args.folder+"/image"+str(args.nb*2+1+i)+".png")
            #plt.subplot(331+i)
            #plt.imshow(sampler.generate(sampler.generate_z()), cmap='Greys')
            #plt.axis('off')
            #fig.savefig("images/"+"3tan_sqrt"+".png", dpi=fig.dpi)
            #files.append("images/"+"3tan_sqrt"+".png")
            i += 1
    
    send_image_ftp(args.passwd, files)
