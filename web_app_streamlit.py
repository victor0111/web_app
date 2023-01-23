#-*- codeing = utf-8 -*-
#coding=gbk
#@Time : 2023/1/23 4:24
#@Autor : gegexin
#@File : web_app_streamlit.py
#@Software: PyCharm

import streamlit as st
# import numpy as np
# import pandas as pd
import webbrowser as web
from io import StringIO
# import time
# import os
# import yaml
# import init_streamlit
# import libs.streamlit_authenticator as stauth

link_list = [
        ("����", "https://go.yh0523.cn/y.cy?url="),
        ("8090","https://www.8090.la/8090/?url="),
        ("����", "https://im1907.top/?jx="),
        ("ë����", "https://www.mtosz.com/m3u8.php?url="),
        ("M3U8", "https://jx.m3u8.tv/jiexi/?url="),
        ("����", "https://www.administratorw.com/video.php?url="),
        ("�߸�", "https://jx.nnxv.cn/tv.php?url="),
        ("˾��", "https://jx.4kdv.com/?url="),
        ("Ϻ��", "https://jx.xmflv.com/?url="),
        ("ŷ��", "https://okjx.cc/?url="),
        ("��ħ", "https://www.ckmov.vip/api.php?url="),
        ("����", "https://jx.aidouer.net/?url="),
        ("�̹�", "https://www.pangujiexi.cc/jiexi.php?url="),
        ("�߰�", "https://www.h8jx.com/jiexi.php?url="),
        ("����", "https://api.qianqi.net/vip/?url="),
        ("����", "https://jx.playerjy.com/?url="),
        ("�ۺ�", "https://jx.jsonplayer.com/player/?url="),
        ("ҹĻ", "https://www.yemu.xyz/?url="),
    ]



def my_logics():
    st.set_page_config(page_title='���Ƹ���Ƶվ��',
                       page_icon='D:\PycharmProjects\JD_Auto\Web_app\ico\play.webp')
    st.subheader('���Ƹ���Ƶվ��')
    input_link=st.text_input('������Ƶ����:')

    option = st.sidebar.selectbox(
         'ѡ����Ƶ������·(���������ɹ����л���·����)��',
        ('%s'%link_list[i][0] for i in range(0, len(link_list)) ))
    st.sidebar.write('Ŀǰѡ��Ľ�����·Ϊ:', option)
    for i in range(0, len(link_list)):
         if link_list[i][0]==option:
              base_url=link_list[i][1]
              # st.write(base_url)

    colum1, colum2,colum3, colum4,colum5, colum6= st.columns(6)
    with colum1:
         print(1)
    with colum2:
         print(1)
    with colum3:
         print(1)
    with colum4:
         print(1)
    with colum5:
         print(1)
    with colum6:
         if st.button("����"):
              if input_link!='':
                   web.open(base_url+input_link)
              else:
                   st.warning("��������Ƶ����")

    # if st.button("��ȡ�б�"):
    #      if input_link!='':
    # st.video("https://www.youtube.com/watch?v=bTEpmtIa3z4", format="video/mp4", start_time=0)
    # ���ļ�����
    uploaded_file = st.file_uploader("ѡ��txt��ʽ�ļ�")
    if uploaded_file is not None:
         # To convert to a string based IO:
         stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
         # To read file as string:
         string_data = stringio.read()
         #st.write(string_data)
         line_parts=string_data.split('\n')
         col1, col2, col3 = st.columns(3)
         num=0
         for line in line_parts:
              line_two=line.split(';')
              try:
                   line_title=line_two[0]
                   #st.write(line_title)
                   line_link=line_two[1]
                   coplete_link=base_url+line_link
                   #st.write(coplete_link)
                   if num%3==0:
                        with col1:
                             if st.button(line_title):
                                  web.open(coplete_link)
                   if num%3==1:
                        with col2:
                             if st.button(line_title):
                                  web.open(coplete_link)
                   if num%3==2:
                        with col3:
                             if st.button(line_title):
                                  web.open(coplete_link)
                   num+=1
              except:
                   pass

my_logics()
