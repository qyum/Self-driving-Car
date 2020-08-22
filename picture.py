#histogram shows how much differences between train and validation/test data

plt.hist(train_y,bins=50,color='green',histtype='step')
plt.hist(test_y,bins=50,color='red',histtype='step')
plt.show()


#for baseline model..................

train_mean_y=np.mean(train_y)
print(train_mean_y)
print(np.mean(np.square(test_y-train_mean_y)))
print(np.mean(np.square(test_y- 0.0 )))
