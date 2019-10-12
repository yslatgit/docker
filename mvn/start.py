#!/bin/python
import os,sys
os.system("docker run --rm -it -v /home/worker/windowsfile/LocalWarehouse/:/Localhouse -v /home/worker/yuanma/:/data %s"%(sys.argv[1]))
