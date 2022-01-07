from data_processing import *

def image_list(path):
    '''
    :param path:
        ①图片所在的文件夹
        ②图片列表
        ③包含图片路径的txt文件夹
    :return: 目录下所有格式的图片文件地址列表，txt中的所有图片地址列表
    '''
    image_read(path)

def label_list(image_paths):
    '''
    :param image_paths:  需要对应的图片label 的图片列表
    :return:  图片对应的label列表
    '''
    img2label_paths(image_paths)