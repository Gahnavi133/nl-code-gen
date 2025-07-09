import streamlit as st
from openai_helper import generate_code
from code_runner import safe_exec

st.title("Prompt → Python Code Generator")

user_input = st.text_area("Describe your task:")
if st.button("Generate Code"):
    response = generate_code(user_input)

    if "```python" in response:
        code = response.split("```python")[1].split("```")[0]
    else:
        code = response

    st.code(code, language="python")
    
    run_output, error = safe_exec(code)
    if run_output:
        st.success(run_output)
    if error:
        st.error(error)

    st.markdown("### Explanation")
    st.write(response.split("```")[-1].strip())
