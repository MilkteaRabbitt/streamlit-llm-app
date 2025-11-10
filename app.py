from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("LLMアプリ: 日本満喫アプリ")

st.write("##### 日本観光地案内: 日本全国の観光地の魅力をご案内します")
st.write("入力フォームにご予算と日数、その他希望をご自由にご入力ください。")
st.write("##### 日本グルメ案内: 和食だけでなく地元で人気のグルメもご紹介します")
st.write("ご希望の場所とご予算、料理ジャンルなどご入力ください。")

selected_item = st.radio(

    "アプリを選択してください。",

    ["日本観光地案内", "日本グルメ案内"]

)
st.divider()

# ラジオボタンで選ばれたアプリに応じて入力フォームを表示
# 日本観光地案内が選ばれた場合、予算や日数、その他希望を入力するフォームを表示
# 要望フォームが空の場合は、要望は特になしとして、一般的な人気のおすすめ観光地、グルメを紹介する
# langchain_openaiパッケージの「ChatOpenAI」クラスを呼び出し、要望に応じたプランを返す
# gpt　modelはgpt-4o-miniを使用
#「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義

if selected_item == "日本観光地案内":
    budget = st.text_input("ご予算を入力してください（例: 5万円）")
    days = st.text_input("日数を入力してください（例: 3日間）")
    other_requests = st.text_area("その他ご希望があればご入力ください（例: 温泉地、歴史的名所など）")
    
    if st.button("プランを生成"):
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        
        if not other_requests:
            other_requests = "特になし"
        
        prompt = f"予算: {budget}、日数: {days}、その他の希望: {other_requests} に基づいて、日本のおすすめ観光地プランを提案してください。"
        response = llm.invoke(prompt) 
        
        st.subheader("おすすめ観光地プラン:")
        st.write(response.content)  

# 日本グルメ案内が選ばれた場合、場所や予算、料理ジャンルを入力するフォームを表示
# 要望フォームが空の場合は、要望は特になしとして、一般的な人気のおすすめグルメを紹介する
elif selected_item == "日本グルメ案内":
    location = st.text_input("ご希望の場所を入力してください（例: 東京）")
    budget = st.text_input("ご予算を入力してください（例: 3000円）")
    cuisine_type = st.text_area("料理ジャンルをご入力ください（例: 寿司、ラーメンなど）")
    
    if st.button("グルメプランを生成"):
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        
        if not cuisine_type:
            cuisine_type = "特になし"
        
        prompt = f"場所: {location}、予算: {budget}、料理ジャンル: {cuisine_type} に基づいて、日本のおすすめグルメプランを提案してください。"
        response = llm.invoke(prompt)
        
        st.subheader("おすすめグルメプラン:")
        st.write(response.content) 
  