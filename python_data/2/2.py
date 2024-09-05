from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


digits = load_digits()

print("Shape images:{}".format(digits.data.shape))
print("Shape target:{}".format(digits.target.shape))

x_train, x_test, y_train, y_test = train_test_split(digits.data,
                                                    digits.target, test_size=0.25, random_state=0)

pipe = make_pipeline(StandardScaler(), LogisticRegression())

pipe.fit(x_test, y_test)

prev = pipe.predict([x_test[0]])
real = y_test[0]

print("Prev:{} Real:{}".format(prev[0], real))