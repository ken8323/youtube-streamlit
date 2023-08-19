import streamlit as st
import time

st.title('streamlit入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration =st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Intration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!'

left_column,right_column = st.columns(2)
button=left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラム')


expander=st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text=st.text_input('あなたの趣味は？')

# 'あなたの趣味は：',text,'です'

# condition=st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition

# if st.checkbox('Show Image'):
#   img=Image.open('DSC_1767.JPG')
#   st.image(img,caption='CHIHARU',use_column_width=True)


# df = pd.DataFrame(
#     np.random.rand(100,2)/(50,50)+[35.69,139.70],
#     columns=['lat','lon']
# )

#st.table(df.style.highlight_max(axis=0))
#メモ：動的な表はDataFrame、静的な表はtable

# st.map(df)


"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""



