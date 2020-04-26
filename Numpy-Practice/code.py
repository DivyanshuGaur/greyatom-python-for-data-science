# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)


age=data[:,0]
#print(age)
max_age=(np.max(age))
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)

print(age_mean,age_std)

race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_5=[]

x=data[:,2]
race_0=np.where(x==0)[0]
race_1=np.where(x==1)[0]
race_2=np.where(x==2)[0]
race_3=np.where(x==3)[0]
race_4=np.where(x==4)[0]


len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

l=[len_0,len_1,len_2,len_3,len_4]
ll=l.copy()
l.sort()
minority_race=ll.index(l[0])
print(minority_race)


senior_citizens=age[data[:,0]>60]
working_hours=data[:,6]

working_hours_arr=working_hours[age>60]
working_hours_sum=np.sum(working_hours_arr)
print(working_hours_sum)

avg_working_hours=working_hours_sum/senior_citizens.size
avg_working_hours=(round(avg_working_hours,2))
print(avg_working_hours)


edu=data[:,1]

high=edu[edu>10]
low=edu[edu<=10]


inc=data[:,7]

pay_high=inc[edu>10]
avg_pay_high=np.mean(pay_high)
avg_pay_high=round(avg_pay_high,2)


pay_low=inc[edu<=10]
avg_pay_low=np.mean(pay_low)
avg_pay_low=round(avg_pay_low,2)

print(avg_pay_high,avg_pay_low)







































#Code starts here




