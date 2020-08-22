 
#....load  batch data...................
import scipy.misc
from PIL import Image
import cv2
#numpy.array(Image.fromarray(arr).resize())
train_batch_pointer=0
val_batch_pointer=0

def train_batch(batch_size):
  global train_batch_pointer
  x_out=[]
  y_out=[]
  for i in range(0,batch_size):

    read_image = cv2.imread(train_x[(train_batch_pointer + i) %num_train_images])
    read_image_road = read_image[-150:]
    read_image_resize = cv2.resize(read_image_road, (200, 66))
    read_image_final = read_image_resize/255.0 
    x_out.append(read_image_final)


    
    #x=np.array(Image.fromarray(train_x[(train_batch_pointer + i) % num_train_images]).resize(-1,200, 66,3))
    #x_out.append(x/255)
    #x_out.append(cv2.resize(cv2.imread(train_x[(train_batch_pointer + i) % num_train_images])[-150:], (200, 66)) / 255.0)
    #x_out.append(scipy.misc.imresize(scipy.misc.imread(train_x[(train_batch_pointer+i)%num_train_images])[-150:], [200, 66]) / 255.0)
    y_out.append(train_y[(train_batch_pointer+i)%num_train_images])
  train_batch_pointer += batch_size
  return x_out,y_out


def val_batch(batch_size):
  global val_batch_pointer
  x_out=[]
  y_out=[]
  for i in range(0,batch_size):

    read_image = cv2.imread(test_x[(val_batch_pointer + i) %num_val_images])
    read_image_road = read_image[-150:]
    read_image_resize = cv2.resize(read_image_road, (200, 66))
    read_image_final = read_image_resize/255.0 
    x_out.append(read_image_final)





    #x_out.append(cv2.resize(cv2.imread(test_x[(val_batch_pointer + i) % num_train_images])[-150:], (200, 66)) / 255.0)
    #x_out.append(scipy.misc.imresize(scipy.misc.imread(test_x[(val_batch_pointer+i)%num_val_images])[-150:], [200, 66]) / 255.0)
    y_out.append(test_y[(val_batch_pointer+i)%num_val_images])

  val_batch_pointer += batch_size
  return x_out,y_out
