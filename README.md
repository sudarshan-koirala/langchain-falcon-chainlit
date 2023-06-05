# langchain-falcon-chainlit
Simple Chat UI using Falcon model, LangChain and Chainlit

### [Youtube Video Covering this GitHub Repo](https://youtu.be/gnyUUY8X-G4)

### Open Source in Action 🚀
- [Falcon](https://falconllm.tii.ae/) as Large Language model
- [LangChain](https://python.langchain.com/en/latest/modules/models/llms/integrations/huggingface_hub.html) as a Framework for LLM
- [Falcon model](https://huggingface.co/tiiuae/falcon-7b-instruct) from Huggingface Website
- [Chainlit](https://docs.chainlit.io/langchain) for deploying.

## System Requirements

You must have Python 3.10 or later installed. Earlier versions of python may not compile.

## Steps to Replicate 

1. Fork this repository and create a codespace in GitHub as I showed you in the youtube video OR Clone it locally.
```
git clone https://github.com/sudarshan-koirala/langchain-falcon-chainlit.git
cd langchain-falcon-chainlit
```

2. Rename example.env to .env with `cp example.env .env`and input the huggingfacehub api token as follows. Get Huggingfacehub api token from this [URL](https://huggingface.co/settings/tokens). You need to create an account in Huggingface if you haven't already.
   ```
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
   ```

3. Run the following command in the terminal to install necessary python packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the following command in your terminal to start the chat UI:
   ```
   chainlit run langchain_falcon.py -w
   ```

## Disclaimer
This is test project and is presented in my youtube video to learn new stuffs using the available open source projects and model. It is not meant to be used in production as it's not production ready. You can modify the code and use for your usecases ✌️
