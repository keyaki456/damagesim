import streamlit as st

st.set_page_config(layout="wide")

st.title('サマナクロ攻撃クリダメクリ率計算機')
st.write('召喚士の武器を外して、召喚獣のルーンを外した状態の、召喚獣の攻撃力とクリダメとクリ率をここに手入力する')

coll1, coll2, coll3 = st.columns(3)
with coll1:
    Attack = st.number_input('攻撃力', 0)
with coll2:
    CriDam = st.number_input('クリダメ', 0.0)
with coll3:
    Criper = st.number_input('クリ率', 0.0)
 

container = st.container(border=True)
with st.container():
    st.write('赤宝石およびルーンの主オプション')
    col1, col2,col3,col4 = st.columns(4)
    with col1:
        fireweapon = st.selectbox('火武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        waterweapon = st.selectbox('水武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        windweapon = st.selectbox('風武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
    with col2:
        lightweapon = st.selectbox('光武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        darkweapon = st.selectbox('闇武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        supportweapon = st.selectbox('サポート武器赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
    with col3:
        r1Main = st.selectbox('ルーン1主オプ',['攻撃実数'])
        r2Main = st.selectbox('ルーン2主オプ',['その他','攻撃実数','攻撃%','クリダメ','クリ率'])
        r3Main = st.selectbox('ルーン3主オプ',['防御実数'])
    with col4:
        r4Main = st.selectbox('ルーン4主オプ',['その他','攻撃実数','攻撃%','クリダメ','クリ率'])
        r5Main = st.selectbox('ルーン5主オプ',['体力実数'])
        r6Main = st.selectbox('ルーン6主オプ',['その他','攻撃実数','攻撃%','クリダメ','クリ率'])

container = st.container(border=True)
with st.container():
        st.write('ルーンのサブオプション')
        colll1, colll2, colll3,colll4, colll5, colll6 = st.columns(6)
        with colll1:
                r1Az = st.number_input('ルーン1攻撃実数', 0)
                r1Ap = st.number_input('ルーン1攻撃%', 0)
                r1Cd = st.number_input('ルーン1クリダメ', 0)
                r1Cp = st.number_input('ルーン1クリ率', 0)
        with colll2:
                r2Az = st.number_input('ルーン2攻撃実数', 0)
                r2Ap = st.number_input('ルーン2攻撃%', 0)
                r2Cd = st.number_input('ルーン2クリダメ', 0)
                r2Cp = st.number_input('ルーン2クリ率', 0)
        with colll3:
                r3Az = st.number_input('ルーン3攻撃実数', 0)
                r3Ap = st.number_input('ルーン3攻撃%', 0)
                r3Cd = st.number_input('ルーン3クリダメ', 0)
                r3Cp = st.number_input('ルーン3クリ率', 0)
        with colll4:
                r4Az = st.number_input('ルーン4攻撃実数', 0)
                r4Ap = st.number_input('ルーン4攻撃%', 0)
                r4Cd = st.number_input('ルーン4クリダメ', 0)
                r4Cp = st.number_input('ルーン4クリ率', 0)
        with colll5:
                r5Az = st.number_input('ルーン5攻撃実数', 0)
                r5Ap = st.number_input('ルーン5攻撃%', 0)
                r5Cd = st.number_input('ルーン5クリダメ', 0)
                r5Cp = st.number_input('ルーン5クリ率', 0)
        with colll6:
                r6Az = st.number_input('ルーン6攻撃実数', 0)
                r6Ap = st.number_input('ルーン6攻撃%', 0)
                r6Cd = st.number_input('ルーン6クリダメ', 0)
                r6Cp = st.number_input('ルーン6クリ率', 0)

container = st.container(border=True)
with st.container():
        st.write('ルーンの銀河石と本')
        collll1, collll2, collll3,collll4, collll5, collll6 = st.columns(6)
        with collll1:
                r1ginga = st.selectbox('ルーン1の銀河石',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
                r1book = st.selectbox('ルーン1の魔法書',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        with collll2:
                r2ginga = st.selectbox('ルーン2の銀河石',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
                r2book = st.selectbox('ルーン2の魔法書',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        with collll3:
                r3ginga = st.selectbox('ルーン3の銀河石',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
                r3book = st.selectbox('ルーン3の魔法書',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        with collll4:
                r4ginga = st.selectbox('ルーン4の銀河石',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
                r4book = st.selectbox('ルーン4の魔法書',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        with collll5:
                r5ginga = st.selectbox('ルーン5の銀河石',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
                r5book = st.selectbox('ルーン5の魔法書',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
        with collll6:
                r6ginga = st.selectbox('ルーン6の銀河石',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])
                r6book = st.selectbox('ルーン6の魔法書',['その他','攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B'])

container = st.container(border=True)
with st.container():
        st.write('その他の情報')
        colllll1, colllll2, colllll3,colllll4,colllll5 = st.columns(5)
        with colllll1:
               equipWeapon = st.selectbox('今装備してる武器',['火','水','風','光','闇'])
        with colllll2:
               AttBuff = st.number_input('攻撃バフレベル',0,10)
        with colllll3:
               CdBuff = st.number_input('クリダメバフレベル',0,10)
        with colllll4:
               CpBuff = st.number_input('クリ率バフレベル',0,10)
        with colllll5:
               food = st.selectbox('料理',['無し','攻撃+493','クリダメ+20.8%','クリ率+11.4%'])



weaponDic = {'その他':0,
              '攻撃実数S':50, '攻撃実数A':40,'攻撃実数B':30,
              '攻撃%S':10.9, '攻撃%A':9,'攻撃%B':8,
              'クリダメS':12.9, 'クリダメA':11,'クリダメB':10,
              'クリ率S':6.6, 'クリ率A':6,'クリ率B':5.5}
mainOpDic = {'その他':0,'攻撃実数':576,'攻撃%':51.2,'クリダメ':54,'クリ率':37}
gingaDic  = {'その他':0,'攻撃実数S':0, '攻撃実数A':0,'攻撃実数B':0,'攻撃%S':7.4, '攻撃%A':7,'攻撃%B':6.5,'クリダメS':8, 'クリダメA':7.8,'クリダメB':7.5,'クリ率S':0, 'クリ率A':0,'クリ率B':0}
bookDic   = {'その他':0,'攻撃実数S':0, '攻撃実数A':0,'攻撃実数B':0,'攻撃%S':0, '攻撃%A':0,'攻撃%B':0,'クリダメS':0, 'クリダメA':0,'クリダメB':0,'クリ率S':0, 'クリ率A':0,'クリ率B':0}