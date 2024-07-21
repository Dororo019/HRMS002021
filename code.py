import pymongo
import pandas as pd 
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


client = pymongo.MongoClient("mongodb+srv://upasana:1234@cluster0.eoztq.mongodb.net/blockchain?retryWrites=true&w=majority")
db = client["blockchain"]
col = db["health details"]

df = pd.read_csv (r'diabetes.csv')
print (df.head(3))

print(df['Outcome'].value_counts())

X = df.iloc[:,1:10].values
Y = df.iloc [:,0].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25 , random_state = 0)

from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
sc2 = StandardScaler()

X_train = sc1.fit_transform(X_train)
X_test = sc2.fit_transform(X_test)


def models(X_train,Y_train):
    
    #Logistic Regression
    from sklearn.linear_model import LogisticRegression
    log = LogisticRegression(random_state=0)
    log.fit(X_train, Y_train)

    print('Logistic Regression Training Accuracy:',log.score(X_train, Y_train))

    return log

print(X_train[2])
model = models(X_train, Y_train)
pred = model.predict(X_test)
print(pred)
print()
print(Y_test)


a = col.find_one({'patient_address': '0x9a1b1149b51A1cbB381B96BbD935328263C382dB'})

x = a['outcome'].reshape(-1, 1)
#print(x)

x1 = [[6,148,72,35,0,33.6,0.627,50]]
x2 = pd.DataFrame(x1, columns  = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
print(x2.head(1))
x3 = x2.iloc[:,0:8].values
print(x3)
x4 = sc1.transform(x3)
print(x4)
pred_ = model.predict(x4)
print(pred_)

y = model.predict(sc1.transform(x.reshape(-1, 1)))
pred_1 = model.predict(y)
print(pred_1)
