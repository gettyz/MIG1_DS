from matplotlib import pyplot as plt
#ploting our canvas
plt.title('Машинки')
plt.xlabel('Значение Х1')
plt.ylabel('Значение X2')
plt.xlim(0,50)
plt.ylim(0,50)
plt.scatter(19, 13, c= 'orange')
plt.scatter(14, 17, c= 'blue')
plt.plot([0,20],[17, 17])
plt.plot([19, 19],[0, 20])

#tests commit
#test 2 good job
#test 3 very bad
#test on branch good
#i love eating
#ничего не пойму


plt.plot([0,35.25],[28.2, 0])
X = [0, 34/3]
Y = [40/5, 0]
plt.plot(X, Y)
plt.arrow(0, 0, 3, 5, width= 0.2)
plt.text(1.5, 1, 'Z(3,5)',fontsize=10)
plt.text(20, 1, 'X1 <= 17',fontsize=10)
plt.text(1.2, 19.5, 'X2 <= 19',fontsize=10)
plt.text(25, 10, '4X1 + 5X2 <= 141',fontsize=10)
plt.text(6.5, 4, 'перпендикуляр',fontsize=10)
#display the graph
plt.show()