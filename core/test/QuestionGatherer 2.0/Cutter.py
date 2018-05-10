import os
import cv2

path = "C:\\Users\\vince\\Desktop\\book7\\"
file_template = path + "{}.jpg"
out_template = "C:\\Users\\vince\\Desktop\\book7_c\\{}.jpg"
file_count = len(os.listdir(path))

adder = 0
for i in range(1, file_count):
    print(file_template.format(i), " -> ", out_template.format(i+adder), "&", out_template.format(i+1+adder))

    img = cv2.imread(file_template.format(i))

    img1 = img[0:1506, 0:1100]
    img2 = img[0:1506, 1100:2199]

    cv2.imwrite(out_template.format(i+adder), img1)
    cv2.imwrite(out_template.format(i+adder+1), img2)

    adder += 1
