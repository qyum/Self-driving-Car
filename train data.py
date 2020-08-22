
data_folder='/content/drive/My Drive/unzip_driving_dataset/driving_dataset'

train_data=os.path.join(data_folder,'data.txt')

from itertools import islice
from scipy import pi
x=[]
y=[]
split=0.8

with open(train_data) as f:
  #for line in islice(f,LIMIT):
  for line in f:

    image_name, angle = line.split()
        
    image_path = os.path.join(data_folder, image_name)
    x.append(image_path)
    angle_radians = float(angle) * (pi / 180)  #converting angle into radians
    y.append(angle_radians)

    #path,angle=line.strip.split()
    #full_path=os.path.join(data_folder,path)
    #x.append(full_path)
    #x.append('data_folder'+line.split()[0])
    #y.append(float(line.split()[1])*scipy.pi/180)


  print(len(x))
  
  y=np.array(y)
  print(y)
