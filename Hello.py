# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd

#from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
modeltraining = st.container()

with header:
    st.title('Gamma-ray burst (GRB) analysis')
    #st.text('I have gamma-ray sources and i want the app to illustre their parameters')


    
with dataset:
    #st.header('IM trying streamlit')
    st.text('This is the GRB dummy data. The GRB data is usually a few gigabytes and I am trying streamlit and GitHUb for the first time so I used dummy data')

    mydata = pd.read_csv('data_2.csv') 
    st.write(mydata.head())   
    st.subheader('')
    st.text('Provided we are dealing with the whole GRB data set, the distribution of one parameter (in this case t90) is essential')
    distribution = pd.DataFrame(mydata['t90'].value_counts())
    st.write(distribution)
    st.text('GRB data set, have a lot of parameters, here I only include 3')
    st.bar_chart(mydata, x="GRB_source", y=['Epeak', 't90','redshift'])

   
with modeltraining:
    st.header('Lets introduce a model for our data')
    st.text('Given the model, lets change the redshift and see what happens')
    sel_col, disp_col = st.columns(2)
    st.text('The redshift of GRBs is slightly above 0 and in a few cases its vey close to 10 hence the selected min and max values') 
    slide = sel_col.slider('Redshift selection', min_value=0, max_value=10, value=1)
    n_estimators = sel_col.selectbox('Number of estimators', options=[1,3,5,10],index=0)
    input_features = sel_col.text_input('Redshift','redshift')   
    #regr = RandomForestRegressor(max_depth = slide, n_estimators=n_estimators)
    x_1= mydata[[input_features]]
    y_1= mydata[['redshift']]


    regr.fit(x_1,y_1)
    prediction = regr.predict(y_1)

    st.text('Depending on the selected redshift on the slider, the errors also change') 
  

    disp_col.subheader('mean absolute error of the model is:')
    disp_col.write(mean_absolute_error(y_1,prediction))

    disp_col.subheader('mean absolute error of the model is:')
    disp_col.write(mean_squared_error(y_1,prediction))

    disp_col.subheader('mean absolute error of the model is:')
    disp_col.write(r2_score(y_1,prediction))




# import streamlit as st
# from streamlit.logger import get_logger

# LOGGER = get_logger(__name__)


# def run():
#     st.set_page_config(
#         page_title="Hello",
#         page_icon="👋",
#     )

#     st.write("# Welcome to Streamlit! 👋")

#     st.sidebar.success("Select a demo above.")

#     st.markdown(
#         """
#         Streamlit is an open-source app framework built specifically for
#         Machine Learning and Data Science projects.
#         **👈 Select a demo from the sidebar** to see some examples
#         of what Streamlit can do!
#         ### Want to learn more?
#         - Check out [streamlit.io](https://streamlit.io)
#         - Jump into our [documentation](https://docs.streamlit.io)
#         - Ask a question in our [community
#           forums](https://discuss.streamlit.io)
#         ### See more complex demos
#         - Use a neural net to [analyze the Udacity Self-driving Car Image
#           Dataset](https://github.com/streamlit/demo-self-driving)
#         - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
#     """
#     )


# if __name__ == "__main__":
#     run()
