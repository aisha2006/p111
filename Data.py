# importing important modules
import statistics as st
import pandas as pd
import csv
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go


# finding the mean of population data
# plotting the population data on a graph
df = pd.read_csv("medium_data.csv")
time = df["reading_time"].tolist()
mean = st.mean(time)
stdev = st.stdev(time)
# print(mean)
fig_population = ff.create_distplot(
    [time],["reading time"], show_hist= False
)
# fig_population.show()

# taking samples of random values
# finding the mean of the sample
sample = []
def random_set_of_mean(counter):
    for i in range(1,counter):
        random_index = random.randint(0,len(time)-1)
        value = time[random_index]
        sample.append(value)

    mean_sample = st.mean(sample)
    return mean_sample

mean_sample = []
# adding traces of 1st, 2nd and 3rd stdevs' on the sample graph
# plotting the sample on a graph
def show_fig(mean_list):
    df_sample = mean_list
    mean_sample = st.mean(mean_list)
    stdev_sample = st.stdev(mean_list)
    first_stdev_start, first_stdev_end = mean_sample-stdev_sample,mean_sample+stdev_sample
    second_stdev_start, second_stdev_end = mean_sample-(2*stdev_sample),mean_sample+(2*stdev_sample)
    third_stdev_start, third_stdev_end = mean_sample-(3*stdev_sample),mean_sample+(3*stdev_sample)
    fig_sample = ff.create_distplot(
        [df_sample], ["mean of the sample"], show_hist= False
    )
    fig_sample.add_trace(go.Scatter(x=[mean_sample,mean_sample],y=[0,10],mode = "lines", name="mean"))
    fig_sample.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,7],mode="lines", name="stdev 1 START"))
    fig_sample.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,7],mode="lines", name="stdev 1 END"))
    fig_sample.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,7],mode="lines", name="stdev 2 START"))
    fig_sample.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,7],mode="lines", name="stdev 2 END"))
    fig_sample.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,7],mode="lines", name="stdev 3 START"))
    fig_sample.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,7],mode="lines", name="stdev 3 END"))
    fig_sample.show()

# calling all the functions
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()
