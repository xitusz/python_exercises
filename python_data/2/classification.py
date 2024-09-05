from sklearn.tree import DecisionTreeClassifier


smooth = 1
irregular = 0
pear = 1
orange = 0

orchard = [[120, smooth], [140, smooth], [180, irregular], [200, irregular]]

result = [pear, pear, orange, orange]

# Decision tree
clf = DecisionTreeClassifier()

# Classifier
clf = clf.fit(orchard, result)

weight = 120
surface = 1

result_usu = clf.predict([[weight, surface]])

if result_usu == 1:
    print("Pear")
else:
    print("Orange")