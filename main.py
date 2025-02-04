import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="민원 분류 자동화 ",
    page_icon="🗂️",
    layout="wide",
)

st.title("국민신문고 민원 담당 기관 분류 예측\n")
st.markdown("""\n**민원**은 국민이 행정기관에 어떤 행위나 답변을 요청하는 다양한 의사표시를 통칭하는 개념으로, 
        행정의 민주화와 신뢰도를 높이고 국민들이 가장 간편하게 이용할 수 있는 행정 구제 수단으로 활용되고 있습니다.
        \n우리는 **국민신문고**를 통해서 온라인으로 편리하게 민원을 신청할 수 있습니다.\n\n\n""")

def load_image(img_file):
    img = Image.open(img_file)
    return img

img_news = load_image("./images/news.png")
st.image(img_news, width=500)

st.markdown("""민원을 신청할 때 선택한 기관이 적정 처리 기관이 아닐 경우, 해당 기관으로 이송 후 처리됩니다.
        \n이때 알맞은 담당 기관으로 이송되는 과정에서 시간이 추가적으로 소요됩니다. """)

img_minwon = load_image("./images/minwon_req.png")
st.image(img_minwon, width=500)

st.markdown("""하지만 사진과 같이 민원을 신청할 때 선택할 수 있는 민원의 수는 
        \n**공공기관 342곳, 중앙행정기관 55곳, 지방자치단체 17곳, 헌법기관 4곳, 교육기관 3곳으로**
        \n민원인의 입장에서 적절한 처리기관을 찾기는 쉽지 않습니다. 그래서 저희는 이러한 불편함과 번거로움을 줄이고자""")

st.markdown(""" ### 민원 분류 자동화 서비스를 구현해보기로 하였습니다.""")
