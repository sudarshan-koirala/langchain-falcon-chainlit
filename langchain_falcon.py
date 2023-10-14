#!/usr/bin/env python
# coding: utf-8

# <a target="_blank" href="https://colab.research.google.com/github/sudarshan-koirala/langchain-falcon-chainlit/blob/main/langchain_falcon.ipynb">
#   <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
# </a>

# In[1]:


get_ipython().run_cell_magic('capture', '', '%pip install langchain huggingface_hub watermark\n')


# In[3]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-a "Mridul Jain" -vmp langchain,huggingface_hub')


# In[4]:


# get your Huggingface access token from https://huggingface.co/settings/tokens 🔑
from getpass import getpass
import os

HUGGINGFACE_API_TOKEN = getpass()
os.environ["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"] = HUGGINGFACE_API_TOKEN   


# #### Let's use falcon-7b-instruct model from [Huggingface website](https://huggingface.co/tiiuae/falcon-7b-instruct)

# In[5]:


from langchain import HuggingFaceHub

repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACE_API_TOKEN, 
                     repo_id=repo_id, 
                     model_kwargs={"temperature":0.7, "max_new_tokens":700})


# In[6]:


from langchain import PromptTemplate, LLMChain

template = """
You are a helpful AI assistant and provide the answer for the question asked politely.

{question}
Answer: Let's think step by step.
"""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "How to cook Pizza ?"

print(llm_chain.run(question))


# In[ ]:




