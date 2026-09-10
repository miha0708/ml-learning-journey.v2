import pandas as pd
import numpy as np


df = pd.read_csv('titanic.csv')
# print(df)

# print(df.shape) #(891, 12)
# print(df.info())
#я хз как сделать 3 пункт одним запросом сразу для всех, могу только для каждого столбца отдельно
# print(len(df['Sex'].unique())) #2
# print(len(df['Pclass'].unique())) #3
# print(len(df['Embarked'].unique())) #4

# print(df)

# new_df = df.groupby(['Sex', 'Pclass']).agg({'PassengerId': 'size', 'Survived': 'sum'})
# new_df['Passengers'] = new_df['PassengerId']
# new_df['SurvivalRate'] = round(((new_df['Survived'] / new_df['Passengers']) * 100), 1)
# print(new_df)


df['FamilySize'] = df['SibSp'] + df['Parch']
df['isAlone'] = df['FamilySize'].apply(lambda x: x == 0)
# print(len(df[df['isAlone']])) #537 одни


# print(df)

# new_df_family = df.groupby('FamilySize')['Survived'].agg('sum')
# new_df_family = df.groupby('FamilySize').agg({
#     'PassengerId': 'size',
#     'Survived': 'sum'
# })
# new_df_family.rename(columns={'PassengerId': 'TotalPassengers', 'Survived': 'TotalSurvived'})
# new_df_family['SurvivedRate'] = round(new_df_family['Survived'] / new_df_family['PassengerId'] * 100, 1)
# new_df_family.sort_values(by=['SurvivedRate'], inplace=True)
# print(new_df_family) #заметим, что меньше всего выжили пассажиры с семьей в 7+, а больше всего с 1-3 членами семьи

def checkAge(age):
    if age < 18:
        return 'Child'
    elif 18 < age < 60:
        return 'Adult'
    elif age >= 60:
        return 'Senior'
    else:
        return 'Oops, your age is NaN'
df['AgeGroup'] = df['Age'].apply(checkAge)

# new_age_df = df.groupby('AgeGroup').agg({'PassengerId': 'size', 'Survived': 'sum', 'Fare': 'mean'})
# new_age_df.rename(columns={'PassengerId': 'TotalPassengers'}, inplace=True)
# new_age_df['SurvivedRate'] = round(new_age_df['Survived'] / new_age_df['TotalPassengers'] * 100, 1)
# print(new_age_df)

medianAge = df['Age'].median()
popularEmbarked = df['Embarked'].value_counts() #S - наиболее часто встречается
df['Age'] = df['Age'].fillna(medianAge)
df['Embarked'] = df['Embarked'].fillna('S')
#а что проверять то в этих столбцах, если я все заполнил?

# print(df)
labels_fare = ['Low', 'Medium', 'High', 'Extreme']
df['CategoryFare'] = pd.qcut(df['Fare'] , q=4, labels=labels_fare)

# new_df_group_fare = df.groupby('CategoryFare').agg({'PassengerId': 'size', 'Age': 'mean', 'Survived': 'sum'})
# new_df_group_fare = new_df_group_fare.rename(columns={'PassengerId': 'TotalPassengers', 'Survived': 'TotalSurvived'})
# new_df_group_fare['Age'] = round(new_df_group_fare['Age'], 1)
# new_df_group_fare['SurvivalRate'] = round(new_df_group_fare['TotalSurvived'] / new_df_group_fare['TotalPassengers'] * 100, 1)
# print(new_df_group_fare)


# print(df['Name'])
def namefunc(name):
    name = name.split(', ')[1]
    name_mini = name.split(' ')[0]
    return name_mini

df['NameMini'] = df['Name'].apply(namefunc)
# print(df['NameMini'].value_counts(ascending=False))
#Mr. - 517 самое поппулярное
# Don.           1 наименее популярные
# Mme.           1
# Ms.            1
# Lady.          1
# Sir.           1
# Capt.          1
# the            1
# Jonkheer.      1

# new_df_miniName = df.groupby('NameMini').agg({'Age': np.mean, 'PassengerId': 'size', 'Survived': 'sum'})
# new_df_miniName.rename(columns={'PassengerId': 'TotalPassengers', 'Survived': 'TotalSurvives'}, inplace=True)
# new_df_miniName['Age'] = new_df_miniName['Age'].round()
# new_df_miniName['SurvivalRate'] = round(new_df_miniName['TotalSurvives']/new_df_miniName['TotalPassengers'] * 100)
# print(new_df_miniName)

# print(df)

# check_dangerous_class = df.groupby('Pclass').agg({'PassengerId': 'size', 'Survived': 'sum'})
# check_dangerous_class.rename(columns={'PassengerId': 'TotalPassengers', 'Survived': 'TotalSurvives'}, inplace=True)
# check_dangerous_class['SurvivalRate'] = round(check_dangerous_class['TotalSurvives'] / check_dangerous_class['TotalPassengers'] * 100, 1)
# check_dangerous_class.sort_values(by=['SurvivalRate'], ascending=False)
# print(check_dangerous_class) #самый опасный - 3 класс, а самый безопасный - 1
#         TotalPassengers  TotalSurvives  SurvivalRate
# Pclass                                              
# 1                   216            136          63.0
# 2                   184             87          47.3
# 3                   491            119          24.2

#еще 3 пункта примерно по похожей схеме, уже лень, идея та же

# print(df)
new_df_embarked_pclass = df.groupby(['Embarked', 'Pclass']).agg({'PassengerId': 'size', 'Survived': 'sum', 'Age': 'mean', 'Fare': 'mean'})
new_df_embarked_pclass = new_df_embarked_pclass.rename(columns={'PassengerId': 'TotalPassengers', 'Survived': 'TotalSurvives'})
new_df_embarked_pclass['SurvivalRate'] = round(new_df_embarked_pclass['TotalSurvives'] / new_df_embarked_pclass['TotalPassengers'] * 100, 1)
# print(new_df_embarked_pclass) #брал несколько столбцов сразу для будущего pivot


# new_df_pivot = pd.pivot_table(new_df_embarked_pclass,
#     index='Embarked',
#     columns='Pclass',
#     values=['SurvivalRate', 'Age', 'Fare'],
#     aggfunc={'Age': 'mean', 'Fare': 'mean', 'SurvivalRate': 'mean'}
# )

# print(new_df_pivot)

print(df)

most_dang_df = df[(df['Sex'] == 'male') & (df['Pclass'] == 3) & ((df['Age'] < 18) | (df['Age'] > 60)) & (df['FamilySize'] == 0) & (df['Survived'] == 0)]
most_dang_df.drop(columns=['PassengerId', 'Survived', 'Pclass', 'Sex', 'AgeGroup', 'CategoryFare', 'NameMini'], inplace=True)
most_dang_df.drop(columns=['SibSp', 'isAlone', 'Parch', 'Ticket', 'Cabin'], inplace=True)
most_dang_df.sort_values(by=['Age'], inplace=True)
print(most_dang_df)