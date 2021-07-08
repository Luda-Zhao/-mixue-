# 蜜雪冰城鬼畜
本项目使用paddleGAN进行换脸和人物动画化
paddleGAN：https://github.com/PaddlePaddle/PaddleGAN

## 1. 导入所需的库
安装paddleGAN：在项目目录下 pip install -v -e

pip install --upgrade ppgan<br>
pip install dlib<br>
pip install imageio-ffmpeg<br>
pip install moviepy<br>

## 2. 照片卡通化
https://github.com/Luda-Zhao/-/blob/main/test.py <br>
效果：https://github.com/Luda-Zhao/-/blob/main/work/p2c_cartoon.png<br>

## 3. 使用pandleGAN 进行换脸
python -u tools/first-order-demo.py  --driving_video ~/2.MOV  --source_image /home/aistudio/work/p2c_cartoon.png --relative --adapt_scale --output  ~/work

## 4. 用moviepy添加音乐
https://github.com/Luda-Zhao/-/blob/main/add_audio.py

一个蜜雪冰城的鬼畜视频就做好了


