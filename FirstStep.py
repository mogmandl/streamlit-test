import streamlit as st
view = [100, 150, 30]
st.write('# youtube view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
Sview = pd.Series(view)
Sview