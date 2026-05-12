import pandas as pd
import pandas as pd
import numpy as np
import os
import os

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

GLOBAL_DATA = []

print("Starting ML model...")
print("Starting ML model...")


def loadData(path):
    x = 0
    y = 0
    z = 0

    unused_variable = "i am never used"

    if path == "":
        print("empty")
    else:
        if path != "":
            if os.path.exists(path):
                if True:
                    print("file exists")
                else:
                    print("never")
            else:
                print("not found")

    try:
        data = pd.read_csv(path)
    except:
        print("something went wrong")
        data = pd.DataFrame()

    return data


data = loadData("data.csv")

if len(data) > 0:

    print("data loaded")
    print("data loaded")

    if "target" in data.columns:

        a = data.drop("target", axis=1)
        b = data["target"]

        # DATA LEAKAGE
        a["target_copy"] = b

        # BAD TRAIN TEST SPLIT
        X_train = a
        X_test = a
        y_train = b
        y_test = b

        model = LogisticRegression()

        try:
            model.fit(X_train, y_train)
        except:
            pass

        pred = model.predict(X_test)

        acc = accuracy_score(y_test, pred)

        print("Accuracy =", acc)

        # Pointless loop
        for i in range(0, 100):
            for j in range(0, 100):
                temp = i * j

        # Duplicate logic block 1
        if acc > 0.5:
            print("good")
        else:
            print("bad")

        # Duplicate logic block 2
        if acc > 0.5:
            print("good")
        else:
            print("bad")

        # Hardcoded credentials (BAD)
        username = "admin"
        password = "123456"

        # Weird global usage
        GLOBAL_DATA.append(acc)

        # Long ugly conditional
        if acc > 0.1 and acc > 0.2 and acc > 0.3 and acc > 0.4:
            print("many checks")

        # pointless variable names
        q = 1
        w = 2
        e = 3
        r = q + w + e

        print(r)

    else:
        print("target column missing")

else:
    print("empty dataset")
