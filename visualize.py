from subprocess import call
import os
#import cv2
from google.colab.patches import cv2_imshow
#check if on windows OS
#windows = False
#if os.name == 'nt':
   # windows = True

sess = tf.InteractiveSession()
saver = tf.train.Saver()
saver.restore(sess, "./save/model.ckpt")

img = cv2.imread('steering_wheel_image.jpg', 0) 
 
#here, second parameter '0' specifies that img.shape will return only height and
#width of the image and not the number of channels. It is a colored image so number of channels = 3, which it will not return.
rows, cols = img.shape

i = 0

while(cv2.waitKey(10) != ord('q')):
    #full_image = cv2.imread("driving_dataset/" + str(i) + ".jpg")
    full_image = cv2.imread(test_x[i])
    image = ((cv2.resize(full_image[-150:], (200, 66)) / 255.0).reshape((1, 66, 200, 3)))
    #degrees = y.eval(feed_dict={x: [image],keep_prob: 1.0})[0][0] * 180.0 / 3.14159265
    degrees = sess.run(y, feed_dict = {x: image, keep_prob: 1.0})[0][0] *180 /3.14159265
    if not windows:
        call("clear")
    print("Predicted steering angle: " + str(degrees) + " degrees")
    cv2_imshow( full_image)
    #make smooth angle transitions by turning the steering wheel based on the difference of the current angle
    #and the predicted angle
    smoothed_angle += 0.2 * pow(abs((degrees - smoothed_angle)), 2.0 / 3.0) * (degrees - smoothed_angle) / abs(degrees - smoothed_angle)
    M = cv2.getRotationMatrix2D((cols/2,rows/2),-smoothed_angle,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2_imshow( dst)
    i += 1

cv2.destroyAllWindows()


