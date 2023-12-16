import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # some frontend
    st.header('Draw a Histogram of Different Parameters From Dataset!')
    sd = st.selectbox(
        "Select a Data Parameter",
        [
            "GENDER",
            "CHILD_TOTAL",
            "SOCSTATUS_WORK_FL",
            "SOCSTATUS_PENS_FL",
            "DEPENDANTS",
            "PERSONAL_INCOME",
            "TARGET",
            "LOAN_NUM_TOTAL",
            "LOAN_NUM_CLOSED"
        ]
    )

    # download data
    data = pd.read_csv('for_streamlit.csv')
    data.drop(['Unnamed: 0'], inplace=True, axis=1)

    # draw a histogram
    fig = plt.figure(figsize=(10, 8))
    if sd == "PERSONAL_INCOME":
        plt.hist(data[sd], bins=80)
        plt.xlim(0, 60000)
    else:
        tmp = dict(data[sd].value_counts())
        sns.barplot(x=list(tmp.keys()), y=list(tmp.values()))
    plt.ylabel('Amount')
    plt.xlabel(sd)
    st.pyplot(fig)

if __name__ == '__main__':
    main()