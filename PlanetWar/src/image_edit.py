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
	img_path = os.path.join(os.getcwd(), "../images/multboard.jpg")
	dst_path = os.path.join(os.path.split(img_path)[0], 'board1.bmp')
	src_img = Image.open(img_path)
	board = cut_image(src_img, (20, 20, 95, 100))
	board.save(dst_path)
