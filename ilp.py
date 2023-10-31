import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from statistics import mean


liver_df = pd.read_csv("C:\\Users\\raks2\\Documents\\project csv files\\indian_liver_patient.csv")
liver_df.rename({"Dataset":"liver_dis"},axis='columns', inplace=True)

print(liver_df)

male_patients_df = pd.DataFrame(liver_df.loc[(liver_df["Gender"] == "Male") & (liver_df["liver_dis"] == 2)])
female_patients_df = pd.DataFrame(liver_df.loc[(liver_df["Gender"] == "Female")& (liver_df["liver_dis"] == 2)])


# no of patients by gender 
patient_ratio_df = pd.DataFrame({"Male" : len(male_patients_df.index), "Female": len(female_patients_df.index)}, index = [0]).T
patient_ratio_df.reset_index(inplace = True)
print(patient_ratio_df)
fig_01 = px.pie(data_frame=patient_ratio_df,names="index",values=0 , title = "NO. OF PATIENTS BY GENDER",
 color_discrete_sequence=px.colors.sequential.Burg_r, labels={"index":"Gender", '0':"Patients"})
fig_01.show()



#average alkaline phosphotase
male_records = pd.DataFrame(liver_df.loc[(liver_df["Gender"] == "Male")])
female_records = pd.DataFrame(liver_df.loc[(liver_df["Gender"] == "Female")])
avg_alkp_ratio = pd.DataFrame({"Male": mean(male_records["Alkaline_Phosphotase"]),
 "Female" : mean(female_records["Alkaline_Phosphotase"]) }, index=[1]).T
avg_alkp_ratio.reset_index(inplace = True)
print(avg_alkp_ratio)
fig_02 = px.bar(data_frame=avg_alkp_ratio, x = "index", y=1,labels={"index":"Gender", "1":"Average Alkaline Phosphotase"},
 color_discrete_sequence=px.colors.sequential.Agsunset, title = "AVERAGE ALKALINE PHOSPHOTASE BY GENDER",width=450)
fig_02.update_layout(xaxis_title = "Gender", yaxis_title=  "Alkalinr Phosphotase")
fig_02.show()



#average total proteins by gender
avg_pro_ratio  = pd.DataFrame({"Male" : male_records["Total_Protiens"], "Female": female_records["Total_Protiens"]})
avg_pro_ratio.reset_index(drop  = True, inplace = True)
print(avg_pro_ratio)
fig_03 = px.scatter(data_frame=avg_pro_ratio,
 title = "TOTAL PROTIENS BY GENDER", labels={"variable":"Gender", "value":"Total Protiens", "index":"ID"})
fig_03.update_layout(xaxis_title = "Gender", yaxis_title="Total Protiens")
fig_03.show()

#a and g rattio
fig_04 = px.scatter(data_frame=liver_df, x = "Gender",y = "Albumin_and_Globulin_Ratio", title = "ALBUMIN AND GLOBULIN RATIO", color="Gender"
)
fig_04.update_layout(xaxis_title = "Gender", yaxis_title = "A&G RATIO")
fig_04.show()





