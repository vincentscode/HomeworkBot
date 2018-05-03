import os
import cv2

path = "C:\\Users\\vince\\Desktop\\book5\\"
file_template = path + "{}.png"
out_template = "C:\\Users\\vince\\Desktop\\book5_cut\\{}.png"
file_count = len(os.listdir(path))

adder = 0
for i in range(1, file_count+1):
    print(file_template.format(i), " -> ", out_template.format(i+adder), "&", out_template.format(i+1+adder))

    img = cv2.imread(file_template.format(i))

    img1 = img[12:860-11, 329:940]
    img2 = img[12:860-11, 940:1880-329]

    cv2.imwrite(out_template.format(i+adder), img1)
    cv2.imwrite(out_template.format(i+adder+1), img2)

    adder += 1
