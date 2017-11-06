import numpy as np
import scipy.misc


# Create images with random rectangles and bounding boxes.
num_imgs = 100

img_size = 1250
min_object_size = 8
max_object_size = 14
num_objects = 70

bboxes = np.zeros((num_imgs, num_objects, 4))
imgs = np.ones((num_imgs, img_size, img_size))  # set background to 0




for i_img in range(num_imgs):
    img_name = 'img_' + str(i_img) + '.jpg'
    for i_object in range(num_objects):
        w, h = np.random.randint(min_object_size, max_object_size, size=2)
        x = np.random.randint(0, img_size - w)
        y = np.random.randint(0, img_size - h)
        imgs[i_img, x:x + w, y:y + h] = 0.  # set rectangle to 1
        bboxes[i_img, i_object] = [y, x, y + h, x + w]
        if w == h:
            string = './data/imgs/' + img_name + ','
            for number in bboxes[i_img, i_object]:
                string += str(int(number)) + ','
            with open("../my_data.txt", "a") as myfile:
                myfile.write(string + 'rectangle\n')
        else:
            string = './data/imgs/' + img_name + ','
            for number in bboxes[i_img, i_object]:
                string += str(int(number)) + ','
            with open("../my_data.txt", "a") as myfile:
                myfile.write(string + 'rectangle\n')

    scipy.misc.imsave('../data/imgs/img_' + str(i_img) + '.jpg', imgs[i_img])






