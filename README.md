# langchain-falcon-chainlit
Simple Chat UI using Falcon model, LangChain and Chainlit

### Open Source in Action 🚀
- Falcon as Large Language model
- LangChain as Web Framework
- Falcon model from Huggingface Website
- Deploying using Chainlit

## System Requirements

You must have Python 3.10 or later installed. Earlier versions of Python may not compile.

## Steps to Replicate 

1. Fork this repository or create a codespace in GitHub as I showed you in the youtube video.

2. Run the following command in the terminal to install necessary python packages:
   ```
   pip install -r requirements.txt
   ```

3. Rename example.env to .env and input the huggingfacehub api token as follows. Get Huggingfacehub api token from this [URL](https://huggingface.co/settings/tokens). You need to create an account in Huggingface if you haven't already.
   ```
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
   ```

4. Run the following command in your terminal to start the chat UI:
   ```
   chainlit run app.py -w
   ```

## Disclaimer
This is test project and is presented in my youtube video to learn new stuffs using the available open source projects and model. It is not meant to be used in production as it's not production ready. You can modify the code and use for your usecases ✌️
