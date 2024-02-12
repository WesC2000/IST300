
import streamlit as st
import time
st.write('Hello World')

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


st.image("otto.jpg")
#st.audio("Audio.mp3")
#st.video("video.mp4")


st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)



st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()
st.subheader("Progress bar")
st.progress(10)

st.subheader("Wait the execution")
with st.spinner('Wait for it...'):
    time.sleep(1)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))



st.sidebar.title("This is writeen inside the sidebar")
st.sidebar.button("Click_sidebar")
# Careful of having the same internal key 
# E.g. st.button('Click') and st.sidebar.button("Click") causes error

st.sidebar.radio("pick your gender",["male","female"])


container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)


import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.bar_chart(df)


import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.area_chart(df)


import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
df = pd.DataFrame(np.random.randn(500, 3),columns=['x','y','z'])
c = alt.Chart(df).mark_circle().encode(x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)



import streamlit as st
import graphviz as graphviz
st.graphviz_chart('''    
    digraph {        
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp    
    }
''')



import pandas as pd
import numpy as np
import streamlit as st
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)



