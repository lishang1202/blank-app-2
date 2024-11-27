import streamlit as st
# 设置网页标题
st.title("李尚的Streamlit网站")

# 显示一些文本内容
st.write("欢迎来到这个简单的Streamlit示例网站！在这里你可以体验一些基本的交互功能。")

# 创建一个滑块部件
slider_value = st.slider("请选择一个数值", 0, 100, 50)
st.write(f"你选择的数值是: {slider_value}")