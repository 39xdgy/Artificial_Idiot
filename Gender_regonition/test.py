from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

iris = load_iris()
'''
print(type(iris))
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
'''
X = iris.data
y = iris.target

print(X.shape, y.shape)

check = [[3,5,4,2], [5,4,3,2]]

knn = KNeighborsClassifier(n_neighbors = 1)
print(knn)


knn.fit(X,y)

output = knn.predict(check)
print(output)


knn = KNeighborsClassifier(n_neighbors = 5)

knn.fit(X,y)

output = knn.predict(check)

print(output)

logreg = LogisticRegression()

logreg.fit(X, y)

print(logreg.predict(check))
