import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def all_categorial_features(X):
    cat_feature_list = []
    for x in X.columns:
        if type(X[x][0]) == str:
            cat_feature_list.append(x)
    return cat_feature_list

def all_real_features(X):
    real_feature_list = []
    for x in X.columns:
        if type(X[x][0]) != str:
            real_feature_list.append(x)
    return real_feature_list

def bar_plot_feature_missing_ratio(X):
    missing_feature_dict = {}
    labels, values = [],[]
    for x in X.columns:
        tmp = X.shape[0] - sum(X[x].value_counts())
        if tmp:
            missing_feature_dict[x] = round(float(tmp)/X.shape[0],4)
    for key, value in sorted(missing_feature_dict.items(), key=lambda item: item[1]):
        labels.append(key)
        values.append(value)
    plt.figure(figsize=(12,6))
    plt.xticks(rotation='90')
    sns.barplot(labels, values)
    plt.show()
    return res
        
  

data = pd.read_csv('train.csv')
bar_plot_feature_missing_ratio(data)