# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
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
import os
from datetime import date
import threading
import time

@st.cache_data
def get_sales_data(data):
    global df
    df = pd.read_csv(data ,encoding='cp949')
    return df

def format_with_commas(number):
    return f"{number:,}"

def get_sales_max(df,col1,col2,cvr : None):
    revenue = sum(df[col1])
    order = sum(df[col2])
    if cvr == None:
        if revenue > 1000000:
            revenue = int(revenue/1000000)
            unit = 'M'
            return revenue, order, unit
        elif revenue >= 1000 and revenue < 1000000:
            revenue = int(revenue/1000)
            unit = 'K'
            return revenue, order, unit
        elif revenue < 1000:
            unit = ''
            return revenue, order, unit
    elif cvr == True:
        if  revenue > 1000000:
            cvr = revenue/order
            revenue = int(revenue / 1000000)
            unit = 'M'
            return revenue, order, unit ,cvr
        elif revenue >= 1000 and revenue < 1000000:
            cvr = revenue/order
            revenue = int(revenue / 1000)
            unit = 'K'
            return revenue, order, unit, cvr
        elif revenue < 1000:
            cvr = revenue/order
            unit = ''
            return revenue, order, unit, cvr


def display_barchart(data,x,y):
    if x == 'cvr':
        chart_data = data[["구매금액","구매수량","구매일자"]]
        chart_data = chart_data.groupby("구매일자")[["구매금액","구매수량"]].sum()
        chart_data = chart_data["구매금액"]/chart_data["구매수량"]
        st.bar_chart(chart_data, height=200, x_label=None, y_label=None)
    elif x != 'cvr':
        chart_data = data[[x,y]]
        chart_data = chart_data.groupby(y)[x].sum()
        st.bar_chart(chart_data,height=200,x_label=None,y_label=None)

def display_metric(col, title, value, data ,bar_value):
    with col:
        with st.container(border = True, height= 350):
            st.metric(title, value)
            display_barchart(data,bar_value,"구매일자")

def upload_handling(from_date,to_date, data):
    if data != None:
        df = get_sales_data(data)
        # get_dimension_filter(df)
        # df = data
        metircs = [
            ("Overview_v1", "Net Revenue"),
            ("Overview_v2", "Net Revenue")
        ]
        from_date = int(from_date.strftime('%Y%m%d'))
        to_date = int(to_date.strftime('%Y%m%d'))
        df = df[(df["구매일자"] >= from_date)
                &(df["구매일자"] <= to_date)].copy()

        cols = st.columns(3)

        revenue, order, unit, cvr = get_sales_max(df, "구매금액", "구매수량",cvr=True)
        st.dataframe(df.style.highlight_max(axis=0) , width= 1600, hide_index = True)
        display_metric(cols[0],"Revenue", f" {revenue}{unit}", df,"구매금액")
        display_metric(cols[1],"Order Count", f" {order}", df,"구매수량")
        display_metric(cols[2],"CVR", f" {int(cvr)}", df, "cvr")

def get_dimension_filter(data):
    df = get_sales_data(data)
    for i in df.select_dtypes(include='object').columns:
        filter_value = []
        filter_value = list(df[i].drop_duplicates())
        i = st.multiselect(
            f"{i}",
            filter_value,
            filter_value
        )
    return get_dimension_filter(i)

data = st.file_uploader("Upload")
# get_dimension = get_dimension_filter(data)data


with st.sidebar:
    st.header("⚙️ Settings")
    total = st.date_input("Between Date",(date(2014, 12, 21),date(2014, 12, 31)) )
    if int(len(total)) == 2:
        from_date , to_date = total
        sales_filter = True
    else:
        st.error("Choose Date")
        sales_filter = False

condition = threading.Condition()

with condition:
    if sales_filter == False:
        condition.wait()
    elif sales_filter == True:
        upload_handling(from_date, to_date, data)
