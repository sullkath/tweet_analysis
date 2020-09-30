import pandas as pd
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import csv as csv

columns=['VADER', 'word_overall_sent']
df = pd.read_csv("Raw_Data/all_sents_manual_incorp.csv", encoding="ISO-8859-1", usecols=columns)
print(df.head(10))

ac_score = accuracy_score(df['VADER'],df['word_overall_sent'])
print(ac_score)

classif = classification_report(df['VADER'],df['word_overall_sent'], output_dict=True)
print(classif)

classif_df = pd.DataFrame(classif)

classif_df.to_csv(r'C:\Users\sullkath\OneDrive\D2V Fellowship\COVID-19\COVID19docs_Project_Twitter\covid19docs\Raw_Data\accuracy_f1_all_annot.csv')
