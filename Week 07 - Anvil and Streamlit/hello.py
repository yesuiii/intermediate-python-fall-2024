import streamlit as st
import pandas as pd
import numpy as np

st.title('My first app', )

st.write("Here's our first attempt at using data to create a table:")

st.markdown("""## Heading 2

**This is bold text**

This is *italicized text.*""")

df = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
})

df

option = st.selectbox(
 'Which number do you like best?',
  df['first column'])

'You selected: ', option

chart_data = pd.DataFrame(
     np.random.randn(option, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
