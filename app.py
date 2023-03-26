import streamlit as st
import openai




st.write("""
# Arkouda Query Bot
""")


user_input = st.text_input("Enter your API token")


question = st.text_input("Enter your question")



openai.api_key = user_input


if question != "":

    with st.spinner('Writing your answer'):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": """
                    You're a chatbot that answers question based on documentation of Arkouda 
                    which allows a user to interactively issue massively parallel computations on distributed data using functions and syntax that mimic NumPy
            
                    Rules:
                    1. If something isn't possible, just say the following thing isn't possible.
            
                    """
                    },
                    {"role": "user", "content": question},
                    {"role": "user", "content": "Who is the creator of Arachne ?"},
                    {"role": "assistant", "content": "Arachne was built by a PhD student named Oliver Rogriges at NJIT"}
                ]
        )
        st.success("Done!")
        st.markdown(response['choices'][0]['message']['content'])
