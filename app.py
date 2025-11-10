from dotenv import load_dotenv
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

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

# langchain_openai「schema」とモジュール使用
# 1つの入力フォームでユーザーの予算、希望を聞き「HumanMessege]とする
# ラジオボタンで選ばれたアプリに応じて専門家を選択しユーザー入力に回答
# 関数の呼び戻しinvoke とメッセージのリスト使用
# 日本観光地案内が選ばれた場合、予算や日数、その他希望を入力するフォームを表示し「HumanMessage」のクラスとする
# 要望フォームが空の場合は、要望は特になしとして、一般的な人気のおすすめ観光地、グルメを紹介する
# 回答は「SystemMessage」とし、日本の観光案内 / グルメの専門家として適切に解答
#「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義

# 共通の入力フォーム
user_input = st.text_area(
    "ご希望の内容を入力してください（例: 予算・日数・エリア・食べたいもの 等）"
)

def get_llm_response(user_input: str, selected_app: str) -> str:
    if selected_app == "日本観光地案内":
        system_text = (
            "あなたは日本全国の観光地に詳しい旅行プランナーです。"
            "利用者の希望に合わせて、具体的な旅行プランを日本語で提案してください。"
        )
    else:  # 日本グルメ案内
        system_text = (
            "あなたは日本各地の飲食店とローカルグルメに詳しい食の専門家です。"
            "利用者の希望に合わせて、具体的なグルメプランを日本語で提案してください。"
        )

    messages = [
        SystemMessage(content=system_text),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages)
    return response.content

# ボタン押下で実行
if st.button("プランを生成"):
    if not user_input.strip():
        st.warning("ご希望の内容を入力してください。")
    else:
        answer = get_llm_response(user_input, selected_item)
        st.subheader("専門家からの提案")
        st.write(answer)