import numpy as np
import pandas as pd
examdata={"name":["aarav","yaksh","ram","sita","jhon","jerry","emily","bose","geoffry","lakshman"],
          "score":[np.nan,30,90,50,40,50,np.nan,49,50,40],"attempts":[1,2,3,1,4,2,1,1,1,2],"qualify":["yes","no","no","yes","yes","yes","yes","no","yes","yes"]}
labels=["a","b","c","d","e","f","g","h","i","j"]
df=pd.DataFrame(examdata,index=labels)
print("Summary of basic information about this data frame and its data")
print(df.info())