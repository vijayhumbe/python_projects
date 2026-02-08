import streamlit as st
st.title("STUDENT RANKING 🎓 ")
st.header("ENTER YOUR MARKS HERE 👇")
eng = st.number_input("Enter your english marks here",value=None, placeholder="Type a number...")
hi = st.number_input("Enter your hindi marks here",value=None, placeholder="Type a number...")
math = st.number_input("Enter your math marks here",value=None, placeholder="Type a number...")
sci = st.number_input("Enter your science marks here",value=None, placeholder="Type a number...")
tel = st.number_input("Enter your telgu marks here",value=None, placeholder="Type a number...")
submit = st.button("submit")
if submit:
    if eng == 0 and hi == 0 and math == 0 and sci == 0 and tel == 0 :
     st.warning("first enter your marks for ranking")
    elif eng == 0:
     st.warning("please enter your english marks")
    elif hi == 0 :
     st.warning("please enter your hindi marks")
    elif math == 0 :
     st.warning("please enter your math marks")
    elif sci == 0 :
     st.warning("please enter your science marks")
    elif tel == 0 :
     st.warning("please enter your telgu marks")
    else :
       total = eng+hi+math+sci+tel
       per = (total)/500*100
       st.success("🎉 Total marks "+str(total))
       st.success("📊 percentage : "+str(per)+"%")
       if per<50:
    
        st.warning("Your Failed")
       elif per>=50 and per<=59.99 :
        st.success("🏅 Congrats!! You got D grade")
       elif per>60 and per<69.99 :
        st.success("🏅 Congrats!! You got C grade")
       elif per>70 and per<79.99 :
        st.success("🏅 Congrats!! You got B grade")
       elif per>80 and per<=89.99 :
        st.success("🏅 Congrats!! You got A grade")
       elif per>90 and per<=100 :
        st.success("🏅 Congrats!!  You got A+  grade")



    