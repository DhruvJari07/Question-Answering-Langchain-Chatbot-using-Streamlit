from langchain_community.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

Huggingface_api = os.getenv("Huggingface_api")

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token='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', temperature=0.3)

input_text = 'what is large language model?'

print(llm.invoke(input_text))

