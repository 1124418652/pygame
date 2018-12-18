# -*- coding: utf-8 -*-
import os
from PIL import Image


def cut_image(src_img, rect):
	"""
	cut a sub image from the src_img
	"""

	region = src_img.crop(rect)
	region = region.resize((60, 60))
	return region

if __name__ == '__main__':

	img_path2 = "../images/ufo.jpeg"
	src_img2 = Image.open(img_path2)
	src_img2 = src_img2.resize((60, 30))
	src_img2.save("../images/ufo.bmp")