import statistics
import pandas as pd
import random
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv('data.csv')
data=df['Math_score'].tolist()
population_mean=statistics.mean(data)
population_standard_deviation=statistics.stdev(data)
print('THE MEAN IS',population_mean)
print('THE STDEV IS',population_standard_deviation)
def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    sample_mean=statistics.mean(data_set)
    return(sample_mean)
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
sample_mean=statistics.mean(mean_list)
sample_stdev=statistics.stdev(mean_list)
print('the sample mean is',sample_mean)
print('the sample stdev is',sample_stdev)
first_stdev_start,first_stdev_end=sample_mean-sample_stdev,sample_mean+sample_stdev
second_stdev_start,second_stdev_end=sample_mean-(2*sample_stdev),sample_mean+(2*sample_stdev)
third_stdev_start,third_stdev_end=sample_mean-(3*sample_stdev),sample_mean+(3*sample_stdev)

fig=ff.create_distplot([mean_list],['SAMPLE MATH SCORE'],show_hist=False)
fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.2],mode='lines',name='SAMPLE MEAN'))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1 START'))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1 END'))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2 START'))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2 END'))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 3 START'))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 3 END')) 


df1=pd.read_csv('intervention.csv')
data1=df1['Math_score'].tolist()
intervention_mean1=statistics.mean(data1)
print('THE INTERVENTION 1 MEAN IS',intervention_mean1)
fig.add_trace(go.Scatter(x=[intervention_mean1,intervention_mean1],y=[0,0.17],mode='lines',name='INTERVENTION 1 MEAN'))



z_score1=(intervention_mean1-sample_mean)/sample_stdev

print(z_score1)

fig.show() 