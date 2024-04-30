import streamlit as st
st.title('サマナクロ宝石ルーン銀河石魔法書シミュ')
st.write('召喚士の武器を外して、召喚獣のルーンを外した状態の、召喚獣の攻撃力とクリダメとクリ率をここに手入力する')
coll1, coll2, coll3 = st.columns(3)
with coll1:
    Attack = st.number_input('攻撃力', 0)
with coll2:
    CliDam = st.number_input('クリダメ', 0.0)
with coll3:
    Cliper = st.number_input('クリ率', 0.0)
 

container = st.container(border=True)
with st.container():
    col1, col2,col3,col4 = st.columns(4)
    with col1:
        selected_item = st.selectbox('火武器の赤宝石',
                        ['攻撃実数S', '攻撃実数A','攻撃実数B',
                        '攻撃%S', '攻撃%A','攻撃%B',
                        'クリダメS', 'クリダメA','クリダメB',
                        'クリ率S', 'クリ率A','クリ率B'
                        ])
        selected_item = st.selectbox('水武器の赤宝石',
                        ['攻撃実数S', '攻撃実数A','攻撃実数B',
                        '攻撃%S', '攻撃%A','攻撃%B',
                        'クリダメS', 'クリダメA','クリダメB',
                        'クリ率S', 'クリ率A','クリ率B'
                        ])
        selected_item = st.selectbox('風武器の赤宝石',
                        ['攻撃実数S', '攻撃実数A','攻撃実数B',
                        '攻撃%S', '攻撃%A','攻撃%B',
                        'クリダメS', 'クリダメA','クリダメB',
                        'クリ率S', 'クリ率A','クリ率B'
                        ])
    with col2:
        selected_item = st.selectbox('光武器の赤宝石',
                        ['攻撃実数S', '攻撃実数A','攻撃実数B',
                        '攻撃%S', '攻撃%A','攻撃%B',
                        'クリダメS', 'クリダメA','クリダメB',
                        'クリ率S', 'クリ率A','クリ率B'
                        ])
        selected_item = st.selectbox('闇武器の赤宝石',
                        ['攻撃実数S', '攻撃実数A','攻撃実数B',
                        '攻撃%S', '攻撃%A','攻撃%B',
                        'クリダメS', 'クリダメA','クリダメB',
                        'クリ率S', 'クリ率A','クリ率B'
                        ])
        selected_item = st.selectbox('サポート武器赤宝石',
                        ['攻撃実数S', '攻撃実数A','攻撃実数B',
                        '攻撃%S', '攻撃%A','攻撃%B',
                        'クリダメS', 'クリダメA','クリダメB',
                        'クリ率S', 'クリ率A','クリ率B'])
    with col3:
                selected_item = st.selectbox('ルーン1主オプ',
                        ['攻撃実数'])
                selected_item = st.selectbox('ルーン2主オプ',
                        ['攻撃実数','攻撃%','クリダメ','栗率'])
                selected_item = st.selectbox('ルーン3主オプ',
                        ['防御実数'])
    with col4:
                selected_item = st.selectbox('ルーン4主オプ',
                        ['攻撃実数','攻撃%','クリダメ','栗率'])
                selected_item = st.selectbox('ルーン5主オプ',
                        ['体力実数'])
                selected_item = st.selectbox('ルーン6主オプ',
                        ['攻撃実数','攻撃%','クリダメ','栗率'])

colll1, colll2, colll3,colll4, colll5, colll6, = st.columns(6)