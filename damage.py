import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title('サマナクロ召喚獣攻撃クリダメクリ率計算機')

with st.container(border=True):
        st.write('素のステータスとアカウントスキル')
        coll1, coll2, coll3 = st.columns(3)
        with coll1:
                Attack = st.number_input('Lv.90時の素の攻撃力(ペルナとアルヘンは1911)',0,3000,1911)
                accAz  = st.number_input('アカウントスキルの召喚獣攻撃実数',0,200,200)
                accCd  = st.number_input('アカウントスキルの召喚獣クリダメ',0.0,10.5,10.5)
        with coll2:
                Cridam = st.number_input('素のクリダメ(ペルナとアルヘンは30)',0,400,30)
                accAp  = st.number_input('アカウントスキルの召喚獣攻撃パーセント',0,15,15)
                accCp  = st.number_input('アカウントスキルの召喚獣クリ率',0.0,7.5,7.5)
        with coll3:
                Criper = st.number_input('素のクリ率(ペルナは15 アルヘンは21)',0,100,21)

with st.container(border=True):
    st.write('図鑑効果')
    collllll1, collllll2,collllll3 = st.columns(3)
    with collllll1:
           zuAtta = st.number_input('召喚獣の図鑑効果攻撃',0)
           star1  = st.number_input('その属性の星1召喚獣の図鑑効果攻撃実数',0)
           hondana= st.selectbox('その属性の本棚召喚獣攻撃レベル',[0,1,2,3])
    with collllll2:
           zuCridam = st.number_input('召喚獣の図鑑効果クリダメ',0.0)
           star2    = st.number_input('その属性の星2召喚獣の図鑑効果攻撃実数',0)
           kenkyuu  = st.number_input('図鑑研究による攻撃実数',0)
    with collllll3:
           zuCriper = st.number_input('召喚獣の図鑑効果クリ率',0.0)
           star3    = st.number_input('その属性の星3召喚獣の図鑑効果攻撃実数',0)
           

with st.container(border=True):
    st.write('赤宝石およびルーンの主オプション')
    col1, col2,col3,col4 = st.columns(4)
    with col1:
        fireweapon = st.selectbox('火武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B','無し'])
        waterweapon = st.selectbox('水武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B','無し'])
        windweapon = st.selectbox('風武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B','無し'])
    with col2:
        lightweapon = st.selectbox('光武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B','無し'])
        darkweapon = st.selectbox('闇武器の赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B','無し'])
        supportweapon = st.selectbox('サポート武器赤宝石',['攻撃実数S', '攻撃実数A','攻撃実数B','攻撃%S', '攻撃%A','攻撃%B','クリダメS', 'クリダメA','クリダメB','クリ率S', 'クリ率A','クリ率B','無し'])
    with col3:
        r1Main = st.selectbox('ルーン1主オプ',['攻撃実数'])
        r2Main = st.selectbox('ルーン2主オプ',['その他','攻撃実数','攻撃%','クリダメ','クリ率'])
        r3Main = st.selectbox('ルーン3主オプ',['防御実数'])
    with col4:
        r4Main = st.selectbox('ルーン4主オプ',['その他','攻撃実数','攻撃%','クリダメ','クリ率'])
        r5Main = st.selectbox('ルーン5主オプ',['体力実数'])
        r6Main = st.selectbox('ルーン6主オプ',['その他','攻撃実数','攻撃%','クリダメ','クリ率'])
        moukou = st.checkbox('猛攻セット')
        gekido = st.checkbox('激怒セット')
        yaiba  = st.slider('刃セット何セット',0,3)


with st.container(border=True):
        st.write('ルーンのサブオプション')
        colll1, colll2, colll3,colll4, colll5, colll6 = st.columns(6)
        with colll1:
                r1Az = st.number_input('ルーン1攻撃実数', 0)
                r1Ap = st.number_input('ルーン1攻撃%', 0.0)
                r1Cd = st.number_input('ルーン1クリダメ', 0.0)
                r1Cp = st.number_input('ルーン1クリ率', 0.0)
        with colll2:
                r2Az = st.number_input('ルーン2攻撃実数', 0)
                r2Ap = st.number_input('ルーン2攻撃%', 0.0)
                r2Cd = st.number_input('ルーン2クリダメ', 0.0)
                r2Cp = st.number_input('ルーン2クリ率', 0.0)
        with colll3:
                r3Az = st.number_input('ルーン3攻撃実数', 0)
                r3Ap = st.number_input('ルーン3攻撃%', 0.0)
                r3Cd = st.number_input('ルーン3クリダメ', 0.0)
                r3Cp = st.number_input('ルーン3クリ率', 0.0)
        with colll4:
                r4Az = st.number_input('ルーン4攻撃実数', 0)
                r4Ap = st.number_input('ルーン4攻撃%', 0.0)
                r4Cd = st.number_input('ルーン4クリダメ', 0.0)
                r4Cp = st.number_input('ルーン4クリ率', 0.0)
        with colll5:
                r5Az = st.number_input('ルーン5攻撃実数', 0)
                r5Ap = st.number_input('ルーン5攻撃%', 0.0)
                r5Cd = st.number_input('ルーン5クリダメ', 0.0)
                r5Cp = st.number_input('ルーン5クリ率', 0.0)
        with colll6:
                r6Az = st.number_input('ルーン6攻撃実数', 0)
                r6Ap = st.number_input('ルーン6攻撃%', 0.0)
                r6Cd = st.number_input('ルーン6クリダメ', 0.0)
                r6Cp = st.number_input('ルーン6クリ率', 0.0)

with st.container(border=True):
        st.write('ルーンの銀河石と魔法書')
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

with st.container(border=True):
        st.write('その他の情報')
        colllll1, colllll2, colllll3,colllll4,colllll5 = st.columns(5)
        with colllll1:
               equipWeapon = st.selectbox('今装備してる武器',['火','水','風','光','闇'])
               cloth = st.number_input('衣装攻撃実数',0)
        with colllll2:
               AttBuff = st.number_input('攻撃バフレベル',0,10)
               artifact= st.number_input('AFの攻撃実数',0)
        with colllll3:
               CdBuff = st.number_input('クリダメバフレベル',0,10)
               monsyo = st.number_input('紋章の攻撃実数(主オプとサブオプの和)',0)
        with colllll4:
               CpBuff = st.number_input('クリ率バフレベル',0,10)
        with colllll5:
               food = st.selectbox('料理',['無し','攻撃+493','クリダメ+20.8%','クリ率+11.4%'])



weaponDic = {'無し':0,
              '攻撃実数S':61, '攻撃実数A':53,'攻撃実数B':48,
              '攻撃%S':11.7, '攻撃%A':10,'攻撃%B':8,
              'クリダメS':13.1, 'クリダメA':11.5,'クリダメB':10,
              'クリ率S':8.1, 'クリ率A':7,'クリ率B':6}
weaponAzDic = {'無し':0,
              '攻撃実数S':61, '攻撃実数A':53,'攻撃実数B':48,
              '攻撃%S':0, '攻撃%A':0,'攻撃%B':0,
              'クリダメS':0, 'クリダメA':0,'クリダメB':0,
              'クリ率S':0, 'クリ率A':0,'クリ率B':0}
weaponApDic = {'無し':0,
              '攻撃実数S':0, '攻撃実数A':0,'攻撃実数B':0,
              '攻撃%S':11.7, '攻撃%A':10,'攻撃%B':8,
              'クリダメS':0, 'クリダメA':0,'クリダメB':0,
              'クリ率S':0, 'クリ率A':0,'クリ率B':0}
weaponCdDic = {'無し':0,
              '攻撃実数S':0, '攻撃実数A':0,'攻撃実数B':0,
              '攻撃%S':0, '攻撃%A':0,'攻撃%B':0,
              'クリダメS':13.1, 'クリダメA':11.5,'クリダメB':10,
              'クリ率S':0, 'クリ率A':0,'クリ率B':0}
weaponCpDic = {'無し':0,
              '攻撃実数S':0, '攻撃実数A':0,'攻撃実数B':0,
              '攻撃%S':0, '攻撃%A':0,'攻撃%B':0,
              'クリダメS':0, 'クリダメA':0,'クリダメB':0,
              'クリ率S':8.1, 'クリ率A':7,'クリ率B':6}


mainOpDic = {'その他':0,'攻撃実数':576,'攻撃%':51.2,'クリダメ':54,'クリ率':37}
gingaDic  = {'その他':0,
             '攻撃実数S':56, '攻撃実数A':51,'攻撃実数B':46,
             '攻撃%S':8, '攻撃%A':7.5,'攻撃%B':7,
             'クリダメS':9, 'クリダメA':8.4,'クリダメB':7.8,
             'クリ率S':5.3, 'クリ率A':4.9,'クリ率B':4.5}
bookDic   = {'その他':0,
             '攻撃実数S':50, '攻撃実数A':47,'攻撃実数B':44,
             '攻撃%S':8, '攻撃%A':7.5,'攻撃%B':7,
             'クリダメS':9, 'クリダメA':8.3,'クリダメB':7.6,
             'クリ率S':5.4, 'クリ率A':5,'クリ率B':4.6}

AbuffDic={0:1,1:1.5,2:1.54,3:1.57,4:1.60,5:1.62,6:1.64,7:1.66,8:1.68,9:1.69,10:1.70}
DbuffDic={0:0,1:60,2:80,3:100,4:110,5:120,6:130,7:135,8:140,9:145,10:150}
PbuffDic={0:0,1:30,2:40,3:50,4:57,5:64,6:68,7:72,8:75,9:77,10:80}

hondanaDic={0:0, 1:1.5, 2:3.0, 3:4.6}



groupA = Attack + 158
groupB = 100 + accAp + hondanaDic[hondana]
if equipWeapon=='火' : groupB = groupB + (weaponApDic[fireweapon]) + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
if equipWeapon=='水' : groupB = groupB + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon]) + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
if equipWeapon=='風' : groupB = groupB + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon]) + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
if equipWeapon=='光' : groupB = groupB + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon]) + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
if equipWeapon=='闇' : groupB = groupB + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon]) + (weaponApDic[supportweapon])
if r2Main=='攻撃%' : groupB = groupB + mainOpDic['攻撃%']
if r4Main=='攻撃%' : groupB = groupB + mainOpDic['攻撃%']
if r6Main=='攻撃%' : groupB = groupB + mainOpDic['攻撃%']
if moukou==True: groupB = groupB + 35
groupB = groupB + r1Ap + r2Ap + r3Ap + r4Ap + r5Ap + r6Ap
if r1ginga in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + gingaDic[r1ginga]
if r2ginga in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + gingaDic[r2ginga]
if r3ginga in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + gingaDic[r3ginga]
if r4ginga in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + gingaDic[r4ginga]
if r5ginga in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + gingaDic[r5ginga]
if r6ginga in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + gingaDic[r6ginga]
if r1book  in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + bookDic[r1book]
if r2book  in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + bookDic[r2book]
if r3book  in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + bookDic[r3book]
if r4book  in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + bookDic[r4book]
if r5book  in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + bookDic[r5book]
if r6book  in ('攻撃%S','攻撃%A','攻撃%B'): groupB = groupB + bookDic[r6book]
groupC = accAz + zuAtta + star1 + star2 + star3 + kenkyuu
if equipWeapon=='火' : groupC = groupC + (weaponAzDic[fireweapon]) + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
if equipWeapon=='水' : groupC = groupC + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon]) + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
if equipWeapon=='風' : groupC = groupC + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon]) + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
if equipWeapon=='光' : groupC = groupC + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon]) + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
if equipWeapon=='闇' : groupC = groupC + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon]) + (weaponAzDic[supportweapon])
if r1Main=='攻撃実数' : groupC = groupC + mainOpDic['攻撃実数']
if r2Main=='攻撃実数' : groupC = groupC + mainOpDic['攻撃実数']
if r4Main=='攻撃実数' : groupC = groupC + mainOpDic['攻撃実数']
if r6Main=='攻撃実数' : groupC = groupC + mainOpDic['攻撃実数']
groupC = groupC + r1Az + r2Az + r3Az + r4Az + r5Az + r6Az
if r1ginga in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + gingaDic[r1ginga]
if r2ginga in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + gingaDic[r2ginga]
if r3ginga in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + gingaDic[r3ginga]
if r4ginga in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + gingaDic[r4ginga]
if r5ginga in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + gingaDic[r5ginga]
if r6ginga in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + gingaDic[r6ginga]
if r1book  in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + bookDic[r1book]
if r2book  in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + bookDic[r2book]
if r3book  in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + bookDic[r3book]
if r4book  in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + bookDic[r4book]
if r5book  in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + bookDic[r5book]
if r6book  in ('攻撃実数S','攻撃実数A','攻撃実数B'): groupC = groupC + bookDic[r6book]
if food=='攻撃+493': groupC = groupC + 493
groupC = groupC + cloth + artifact + monsyo
afterAttack = (groupA * groupB /100) + groupC
afterAttack = afterAttack * AbuffDic[AttBuff]

afterCd = Cridam + zuCridam + accCd
if equipWeapon=='火' : afterCd = afterCd + (weaponCdDic[fireweapon]) + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
if equipWeapon=='水' : afterCd = afterCd + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon]) + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
if equipWeapon=='風' : afterCd = afterCd + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon]) + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
if equipWeapon=='光' : afterCd = afterCd + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon]) + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
if equipWeapon=='闇' : afterCd = afterCd + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon]) + (weaponCdDic[supportweapon])
if r2Main=='クリダメ' : afterCd = afterCd + mainOpDic['クリダメ']
if r4Main=='クリダメ' : afterCd = afterCd + mainOpDic['クリダメ']
if r6Main=='クリダメ' : afterCd = afterCd + mainOpDic['クリダメ']
if gekido==True: afterCd = afterCd + 40
afterCd = afterCd + r1Cd + r2Cd + r3Cd + r4Cd + r5Cd + r6Cd
if r1ginga in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + gingaDic[r1ginga]
if r2ginga in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + gingaDic[r2ginga]
if r3ginga in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + gingaDic[r3ginga]
if r4ginga in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + gingaDic[r4ginga]
if r5ginga in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + gingaDic[r5ginga]
if r6ginga in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + gingaDic[r6ginga]
if r1book  in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + bookDic[r1book]
if r2book  in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + bookDic[r2book]
if r3book  in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + bookDic[r3book]
if r4book  in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + bookDic[r4book]
if r5book  in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + bookDic[r5book]
if r6book  in ('クリダメS','クリダメA','クリダメB'): afterCd = afterCd + bookDic[r6book]
afterCd = afterCd + DbuffDic[CdBuff]
if food=='クリダメ+20.8%': afterCd = afterCd+20.8
if afterCd>400 : afterCd=400

afterCp = Criper + zuCriper + accCp
if equipWeapon=='火' : afterCp = afterCp + (weaponCpDic[fireweapon]) + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
if equipWeapon=='水' : afterCp = afterCp + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon]) + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
if equipWeapon=='風' : afterCp = afterCp + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon]) + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
if equipWeapon=='光' : afterCp = afterCp + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon]) + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
if equipWeapon=='闇' : afterCp = afterCp + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon]) + (weaponCpDic[supportweapon])
if r2Main=='クリ率' : afterCp = afterCp + mainOpDic['クリ率']
if r4Main=='クリ率' : afterCp = afterCp + mainOpDic['クリ率']
if r6Main=='クリ率' : afterCp = afterCp + mainOpDic['クリ率']
afterCp = afterCp + yaiba*12
afterCp = afterCp + r1Cp + r2Cp + r3Cp + r4Cp + r5Cp + r6Cp
if r1ginga in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + gingaDic[r1ginga]
if r2ginga in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + gingaDic[r2ginga]
if r3ginga in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + gingaDic[r3ginga]
if r4ginga in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + gingaDic[r4ginga]
if r5ginga in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + gingaDic[r5ginga]
if r6ginga in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + gingaDic[r6ginga]
if r1book  in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + bookDic[r1book]
if r2book  in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + bookDic[r2book]
if r3book  in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + bookDic[r3book]
if r4book  in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + bookDic[r4book]
if r5book  in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + bookDic[r5book]
if r6book  in ('クリ率S','クリ率A','クリ率B'): afterCp = afterCp + bookDic[r6book]
afterCp = afterCp + PbuffDic[CpBuff]
if food=='クリ率+11.4%': afterCp = afterCp+11.4
if afterCp>100 : afterCp=100

karyoku = afterAttack*(1-afterCp/100)+afterAttack*(1+afterCd/100)*(afterCp/100)

with st.sidebar:
        st.write('補正後の攻撃力')
        afterAttack
        st.write('補正後のクリダメ')
        afterCd
        st.write('補正後のクリ率')
        afterCp
        st.title('火力指標')
        st.write('攻撃力*(1-クリ率/100)+攻撃力*(1+クリダメ/100)*(クリ率/100)のこと')
        st.write('これが最も大きくなるように工夫しよう！')
        karyoku

st.title('ここまでを入力すると左のサイドバーに計算結果が自動で表示される')
st.write('以下は解説')

tab1, tab2, tab3 = st.tabs(["攻撃力の計算式", "この計算機の使い方", "銀河石魔法書サジェスト機能"])
with tab1:
        st.write('''
        攻撃力は
        
        「召喚獣」のページで表示される攻撃力 = (Aグループ×Bグループ)+Cグループ

        で計算される。

        ABCグループの内訳は以下''')
        with st.expander("Aグループ"):
                st.write('Lv.90時の素の攻撃力(ペルナは1911 アルヘンは1911)')
                st.write('タワー効果攻撃実数+158')
        with st.expander("Bグループ(%系全般)"):
                st.write('アカウントスキル召喚獣の攻撃%')
                st.write('赤宝石攻撃%')
                st.write('ルーン主オプ攻撃%')
                st.write('ルーンサブオプ攻撃%')
                st.write('猛攻セット')
                st.write('銀河石攻撃%')
                st.write('魔法書攻撃%')
                st.write('本棚の魔法')
        with st.expander("Cグループ(タワー効果以外の実数系全般)"):
                st.write('アカウントスキル召喚獣の攻撃実数')
                st.write('図鑑Lv(星1+星2+星3+本体)効果')
                st.write('赤宝石攻撃実数')
                st.write('ルーン主オプ攻撃実数')
                st.write('ルーンサブオプ攻撃実数')
                st.write('衣装効果')
                st.write('図鑑研究')
                st.write('料理')
                st.write('銀河石攻撃実数')
                st.write('魔法書攻撃実数')
                st.write('アーティファクト')
                st.write('紋章攻撃実数')

        st.write('例外')
        st.write('攻撃バフ(剣バフ)：召喚獣のページには反映されない (多分Cグループの後に乗算)')
        
with tab2:
       st.write('あなたのアカウントで発動している図鑑効果などなどをゲーム内で調べて入力してください')
       st.write('そうすると攻撃とクリダメとクリ率から算出される「火力指標」が表示されます')
       st.write('赤宝石などのSABの値は概算値なので、補正後の攻撃力クリダメクリ率はゲーム内の値とわずかにズレます')
       st.write('全て特級前提です。(こんな計算機を必要とする人間が特級を妥協するはずが無いため)')
       st.write('■■■')
       st.write('シンプルな計算機なので好きな目的に使って頂ければと思いますが')
       st.write('想定する使い方としては')
       st.write('「銀河石と魔法書の最適解を算出したい」とか')
       st.write('「銀河石と魔法書も付けたけど、赤宝石を変更して、もっと火力伸ばせんやろか」とか')
       st.write('「実際何が火力指標に大きく関わって来るんやろか」とか')
       st.write('そういう疑問を解決するために用いることを想定しました')
       st.write('■■■')
       st.write('火力指標というのは造語です')
       st.write('火力指標にスキル倍率と防御減衰と与ダメバフ被ダメデバフ等を掛けたら')
       st.write('最終ダメージの期待値になる感じです')
       st.write('■■■')
       st.write('要望等は 超過3赤赤赤 (ネフティス鯖) まで')

with tab3:
        st.write('銀河石と魔法書をどう組み合わせると火力指標が最大になるかサジェストする機能')
        st.write('上の入力欄の、ルーンの銀河石と魔法書以外を入力すると自動で計算される')
        st.write('あくまでも目安として特級Aの値で計算する')
        st.write('攻撃実数の銀河石と魔法書は無視する')
        dfginga = pd.DataFrame({
            '銀河石攻撃%'
                :[6,5,5,4,4,4,3,3,3,3,2,2,2,2,2,1,1,1,1,1,1,0,0,0,0,0,0,0],
            '銀河石クリダメ'
                :[0,1,0,2,1,0,3,2,1,0,4,3,2,1,0,5,4,3,2,1,0,6,5,4,3,2,1,0],
            '銀河石クリ率'
                :[0,0,1,0,1,2,0,1,2,3,0,1,2,3,4,0,1,2,3,4,5,0,1,2,3,4,5,6]
            })
        dfmahou = pd.DataFrame({
            '魔法書攻撃%'
                :[6,5,5,4,4,4,3,3,3,3,2,2,2,2,2,1,1,1,1,1,1,0,0,0,0,0,0,0],
            '魔法書クリダメ'
                :[0,1,0,2,1,0,3,2,1,0,4,3,2,1,0,5,4,3,2,1,0,6,5,4,3,2,1,0],
            '魔法書クリ率'
                :[0,0,1,0,1,2,0,1,2,3,0,1,2,3,4,0,1,2,3,4,5,0,1,2,3,4,5,6]
            })
        df=dfginga.join(dfmahou,how='cross')

        sihyoCollumn=[]
        for i in range(0, 784, 1):
               groupA2=Attack + 158
               groupB2=100 + accAp + hondanaDic[hondana]
               if equipWeapon=='火' : groupB2 = groupB2 + (weaponApDic[fireweapon]) + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
               if equipWeapon=='水' : groupB2 = groupB2 + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon]) + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
               if equipWeapon=='風' : groupB2 = groupB2 + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon]) + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
               if equipWeapon=='光' : groupB2 = groupB2 + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon]) + (weaponApDic[darkweapon])/4 + (weaponApDic[supportweapon])
               if equipWeapon=='闇' : groupB2 = groupB2 + (weaponApDic[fireweapon])/4 + (weaponApDic[waterweapon])/4 + (weaponApDic[windweapon])/4 + (weaponApDic[lightweapon])/4 + (weaponApDic[darkweapon]) + (weaponApDic[supportweapon])
               if r2Main=='攻撃%' : groupB2 = groupB2 + mainOpDic['攻撃%']
               if r4Main=='攻撃%' : groupB2 = groupB2 + mainOpDic['攻撃%']
               if r6Main=='攻撃%' : groupB2 = groupB2 + mainOpDic['攻撃%']
               if moukou==True: groupB2 = groupB2 + 35
               groupB2 = groupB2 + r1Ap + r2Ap + r3Ap + r4Ap + r5Ap + r6Ap
               gropuB2 = groupB2 + df.at[i,'銀河石攻撃%']*gingaDic['攻撃%A'] + df.at[i,'魔法書攻撃%']*bookDic['攻撃%A']
               groupC2 = accAz + zuAtta + star1 + star2 + star3 + kenkyuu
               if equipWeapon=='火' : groupC2 = groupC2 + (weaponAzDic[fireweapon]) + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
               if equipWeapon=='水' : groupC2 = groupC2 + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon]) + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
               if equipWeapon=='風' : groupC2 = groupC2 + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon]) + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
               if equipWeapon=='光' : groupC2 = groupC2 + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon]) + (weaponAzDic[darkweapon])/4 + (weaponAzDic[supportweapon])
               if equipWeapon=='闇' : groupC2 = groupC2 + (weaponAzDic[fireweapon])/4 + (weaponAzDic[waterweapon])/4 + (weaponAzDic[windweapon])/4 + (weaponAzDic[lightweapon])/4 + (weaponAzDic[darkweapon]) + (weaponAzDic[supportweapon])
               if r1Main=='攻撃実数' : groupC2 = groupC2 + mainOpDic['攻撃実数']
               if r2Main=='攻撃実数' : groupC2 = groupC2 + mainOpDic['攻撃実数']
               if r4Main=='攻撃実数' : groupC2 = groupC2 + mainOpDic['攻撃実数']
               if r6Main=='攻撃実数' : groupC2 = groupC2 + mainOpDic['攻撃実数']
               groupC2 = groupC2 + r1Az + r2Az + r3Az + r4Az + r5Az + r6Az
               if food=='攻撃+493': groupC2 = groupC2 + 493
               groupC2 = groupC2 + cloth + artifact + monsyo
               afterAttack2 = (groupA2 * groupB2 /100) + groupC2
               afterAttack2 = afterAttack2 * AbuffDic[AttBuff]





               afterCd2 = Cridam + zuCridam + accCd
               if equipWeapon=='火' : afterCd2 = afterCd2 + (weaponCdDic[fireweapon]) + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
               if equipWeapon=='水' : afterCd2 = afterCd2 + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon]) + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
               if equipWeapon=='風' : afterCd2 = afterCd2 + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon]) + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
               if equipWeapon=='光' : afterCd2 = afterCd2 + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon]) + (weaponCdDic[darkweapon])/4 + (weaponCdDic[supportweapon])
               if equipWeapon=='闇' : afterCd2 = afterCd2 + (weaponCdDic[fireweapon])/4 + (weaponCdDic[waterweapon])/4 + (weaponCdDic[windweapon])/4 + (weaponCdDic[lightweapon])/4 + (weaponCdDic[darkweapon]) + (weaponCdDic[supportweapon])
               if r2Main=='クリダメ' : afterCd2 = afterCd2 + mainOpDic['クリダメ']
               if r4Main=='クリダメ' : afterCd2 = afterCd2 + mainOpDic['クリダメ']
               if r6Main=='クリダメ' : afterCd2 = afterCd2 + mainOpDic['クリダメ']
               if gekido==True: afterCd2 = afterCd2 + 40
               afterCd2 = afterCd2 + df.at[i,'銀河石クリダメ']*gingaDic['クリダメA'] + df.at[i,'魔法書クリダメ']*bookDic['クリダメA']
               afterCd2 = afterCd2 + DbuffDic[CdBuff]
               if food=='クリダメ+20.8%': afterCd2 = afterCd2 + 20.8
               if afterCd2>400 : afterCd2=400




               afterCp2 = Criper + zuCriper + accCp
               if equipWeapon=='火' : afterCp2 = afterCp2 + (weaponCpDic[fireweapon]) + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
               if equipWeapon=='水' : afterCp2 = afterCp2 + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon]) + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
               if equipWeapon=='風' : afterCp2 = afterCp2 + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon]) + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
               if equipWeapon=='光' : afterCp2 = afterCp2 + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon]) + (weaponCpDic[darkweapon])/4 + (weaponCpDic[supportweapon])
               if equipWeapon=='闇' : afterCp2 = afterCp2 + (weaponCpDic[fireweapon])/4 + (weaponCpDic[waterweapon])/4 + (weaponCpDic[windweapon])/4 + (weaponCpDic[lightweapon])/4 + (weaponCpDic[darkweapon]) + (weaponCpDic[supportweapon])
               if r2Main=='クリ率' : afterCp2 = afterCp2 + mainOpDic['クリ率']
               if r4Main=='クリ率' : afterCp2 = afterCp2 + mainOpDic['クリ率']
               if r6Main=='クリ率' : afterCp2 = afterCp2 + mainOpDic['クリ率']
               afterCp2 = afterCp2 + yaiba*12
               afterCp2 = afterCp2 + r1Cp + r2Cp + r3Cp + r4Cp + r5Cp + r6Cp
               afterCp2 = afterCp2 + df.at[i,'銀河石クリ率']*gingaDic['クリ率A'] + df.at[i,'魔法書クリ率']*bookDic['クリ率A']
               afterCp2 = afterCp2 + PbuffDic[CpBuff]
               if food=='クリ率+11.4%': afterCp2 = afterCp2+11.4
               if afterCp2>100 : afterCp2=100

               karyoku2 = afterAttack2*(1-afterCp2/100)+afterAttack2*(1+afterCd2/100)*(afterCp2/100)
               sihyoCollumn.append(karyoku2)
        
        dfsihyo = pd.DataFrame(sihyoCollumn)
        dfsihyo.columns=['火力指標']
        df=df.join(dfsihyo)

        df=df.sort_values('火力指標',ascending=False)
        df
        
        st.write('このデータテーブルから分かるように')
        text='攻撃%特級Aの銀河石を' + str(int(df.iloc[0]['銀河石攻撃%'])) + '個'
        st.write(text)
        text='クリダメ特級Aの銀河石を' + str(int(df.iloc[0]['銀河石クリダメ'])) + '個'
        st.write(text)
        text='クリ率特級Aの銀河石を' + str(int(df.iloc[0]['銀河石クリ率'])) + '個'
        st.write(text)
        text='攻撃%特級Aの魔法書を' + str(int(df.iloc[0]['魔法書攻撃%'])) + '冊'
        st.write(text)
        text='クリダメ特級Aの魔法書を' + str(int(df.iloc[0]['魔法書クリダメ'])) + '冊'
        st.write(text)
        text='クリ率特級Aの魔法書を' + str(int(df.iloc[0]['魔法書クリ率'])) + '冊'
        st.write(text)
        st.write('装着すると、火力指標が最大になる')