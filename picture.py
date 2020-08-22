#histogram shows how much differences between train and validation/test data

plt.hist(train_y,bins=50,color='green',histtype='step')
plt.hist(test_y,bins=50,color='red',histtype='step')
plt.show()
