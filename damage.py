import streamlit as st
st.title('サマナクロ宝石ルーン銀河石魔法書シミュ')
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
        st.write('ルーンのサブオプ')
        colll1, colll2, colll3,colll4, colll5, colll6, = st.columns(6)
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