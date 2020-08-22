num_images=len(x)
print(num_images)
#split_index=int(len(y)*0.8)
#print(split_index)
#train_x=x[:split_index]

#shuffle list of images
#c = list(zip(x, y))
#random.shuffle(c)
#x, y = zip(*c)

train_x=x[:int(len(x)*0.8)]
train_y=y[:int(len(x)*0.8)]
print(len(train_x))
print(len(train_y))

test_x= x[-int(len(x)*0.2):]
test_y= y[-int(len(x)*0.2):]
print(len(test_x))
print(len(test_y))


num_train_images=len(train_x)
num_val_images=len(test_x)
