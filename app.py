import streamlit as st
import pandas as pd
from datetime import date


#Read partitioned dataData 
january = "Data/January Input Platform Data .xlsx"

february = "Data/February Input Platform Data .xlsx"

march = "Data/March Input Platform Data .xlsx"

april = "Data/April Input Platform Data .xlsx"

may = "Data/May Input Platform Data .xlsx"

june = "Data/June Input Platform Data  00.06.30.xlsx"
 
july = "Data/July Input Platform Data .xlsx"


def get_date():
    today = date.today()
    d1 = today.strftime("%B %d, %Y")
    return d1


with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#data = pd.read_excel(april)
whole_data = pd.concat(
   map(pd.read_excel, [january, february, march, april, may, june, july]), ignore_index=True)

st.markdown("<h1 style='text-align: center; padding-top:0px;'>Input Data Platform Report</h1>", unsafe_allow_html=True)


#======================== Total Statistics =======================
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>Total General Statistics</h4>", unsafe_allow_html=True)


total_cost = whole_data['totalCost'].sum()
total_rebates = whole_data['rebates'].sum() - 20251040.0
number_of_DMAs = len(whole_data['dmaId'].unique())
total_transcactions = len(whole_data['branchId'].index)


col1, col2 = st.columns([1,1]) 
with col1:
    st.write(f"Number of Transcations: {total_transcactions:,.2f}")
with col2:
    st.write(f"Total Value of Txns: {total_cost:,.2f} Ksh")

col1, col2 = st.columns([1,1]) 
with col1:
    st.write(f"Total Value of Rebates: {total_rebates:,.2f} Ksh")
with col2:
    st.write(f"Total Number of DMAs: {number_of_DMAs:,.2f}")




#======================== Dailry Report =======================
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>Daily Statistics and Update</h4>", unsafe_allow_html=True)


daily_start_date = '2022-06-20'
daily_end_date = '2022-06-21'

mask_data = (whole_data['creationDate'] > daily_start_date) & (whole_data['creationDate'] <= daily_end_date)

whole_data = whole_data.loc[mask_data]

data_len = len(whole_data['branchId'].index)


daily_cost = whole_data['totalCost'].sum() 

st.write(get_date()) 

col1, col2 = st.columns([1,1]) 

with col1:
    st.write(f"Number of Transcations: {data_len:,.2f}")
with col2:
    st.write(f"Daily Value of Txns: {daily_cost:,.2f} Ksh")

col1, col2 = st.columns([1,1]) 
with col1:
    st.write("Total Cash Received: ")
with col2:
    st.write(f"Total Mpesa Txns: ")

col1, col2 = st.columns([1,1]) 

with col1:
    st.write("Total Rebates: ")
with col2:
    st.write("No of New DMAs: ")

#======================== Dailry Report =======================
st.markdown("---")
st.markdown("<h4 style='text-align: center;'> Monthly Statistics and Update </h4>", unsafe_allow_html=True)

option = st.selectbox(
     'Please Select Month:',
     ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October" , "November", "December"))


st.markdown("---")


payment_method = data['paymentMethod'].unique() 

grouped_data = data.groupby('paymentMethod') 


cash_payment = len(grouped_data.get_group('CASH').index) 


mpesa_1 = len(grouped_data.get_group('mpesa')) 

mpesa_2 = len(grouped_data.get_group('MPESA').index) 


total_mpesa = mpesa_2 + mpesa_1  

total_payment = total_mpesa + cash_payment

st.write(f"Total Farmers: {total_payment:,}") 

st.write(f"Farmers who paid Cash: {cash_payment:,}") 

st.write(f"Farmers who paid using Mpesa: {total_mpesa:,}") 





st.markdown("---")
st.subheader("Payment Status")
st.markdown("---")  

payment_status = data['paymentStatus'].unique() 

grouped_status = data.groupby('paymentStatus') 


paid_status = len(grouped_status.get_group('PAID')) 



failed_status = len(grouped_status.get_group('FAILED')) 



pending_status = len(grouped_status.get_group('PENDING')) 



unknown_status = len(grouped_status.get_group('UNKNOWN')) 



col1, col2 = st.columns([1,1]) 

with col1:
    st.write(f"Paid Status: { paid_status:,}") 
with col2:
    st.write(f"Failed Status: { failed_status:,}") 

col1, col2 = st.columns([1,1]) 
with col1:
    st.write(f"Pending Status: { pending_status:,}")
with col2:
    st.write(f"Unknown Status: { unknown_status:,}")  



# total_status = paid_status + pending_status + unknown_status + failed_status

# st.write(total_status)


st.markdown("---")
st.subheader("Amount Per Payment Method")
st.markdown("---")  

Total_Cash_Payment = grouped_data.get_group('CASH')["totalCost"].sum() 
Total_Mpesa_Cost = grouped_data.get_group('mpesa')["totalCost"].sum() + grouped_data.get_group('MPESA')["totalCost"].sum() 

Total_Cost = Total_Cash_Payment + Total_Mpesa_Cost

st.write(f" Total Cost : {Total_Cost:,.2f}")


col1, col2 = st.columns([1,1])
with col1:
    st.write(f" Total Cost Via CASH Payment: {Total_Cash_Payment:,.2f}")
with col2:
    st.write(f" Total Cost Via Mpesa Payment: {Total_Mpesa_Cost:,.2f}") 





st.markdown("---")
st.subheader("Monthly Rebates")


rebates = data['rebates'].sum()


st.write(f" April Rebates: {rebates:,.2f}")


st.markdown("---")  
st.markdown("<h4 style='text-align: center; padding-top:0px;'> Download 25th to 25th Monthly Data</h4>", unsafe_allow_html=True)

st.write("In the section below you can download Date 26th to 25th data for each month")
month_data = st.selectbox(
     'Please Select Month:',
     ("January", "February", "March", "April", "May", "June", "July"))

btn2 = st.button(
     label="Download Data",
     key= "Mostly for roy to use"
     )



st.sidebar.write("Download Monthly Data")

monthly_data = st.sidebar.selectbox(
     'Please Select Month:',
     ("January", "February", "March", "April", "May", "June"))


st.sidebar.button(
     label="Download Data"
 )


hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)   




