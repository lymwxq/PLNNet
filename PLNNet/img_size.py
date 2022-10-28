
from PIL import Image

file_path = 'data/a_b_learnable_K_3inter_800_0.05812668800354004.jpg'

img = Image.open(file_path)
imgSize = img.size
w = img.width
h = img.height
f = img.format
img.close()

print('size =',imgSize,';长度 =',w,';宽度 =',h,';图片格式为 ：',f)



im = Image.open('data/target.png')#返回一个Image对象

print('宽：%d,高：%d'%(im.size[0],im.size[1]))