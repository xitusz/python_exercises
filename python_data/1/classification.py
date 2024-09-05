from sklearn.datasets import load_iris, fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.svm import SVC


##################      Pré-processamento     ###################
# Coleta e Integração
iris = load_iris()

characteristics = iris.data
labels = iris.target

print("Caracteristicas:\n", characteristics[:2])
print("Rótulos:\n", labels[:2])
print('########################################################')

# Partição dos dados
charac_train, charac_test, lab_train, lab_test = train_test_split(characteristics, labels)

###################       Mineração        #####################

############---------- Arvore de Decisão -----------############
tree = DecisionTreeClassifier(max_depth=2)
tree.fit(X=charac_train, y=lab_train)

lab_predict = tree.predict(charac_test)
accuracy_tree = accuracy_score(lab_test, lab_predict)
############-------- Máquina de Vetor Suporte ------############
clf = SVC()
clf.fit(X=charac_train, y=lab_train)

lab_predict_svm = clf.predict(charac_test)
accuracy_svm = accuracy_score(lab_test, lab_predict_svm)

################      Pós-processamento     ####################
print("Acurácia Árvore de Decisão:", round(accuracy_tree, 5))
print("Acurácia SVM:", round(accuracy_svm, 5))
print('########################################################')

r = export_text(tree, feature_names=iris['feature_names'])
print("Estrutura da árvore")
print(r)