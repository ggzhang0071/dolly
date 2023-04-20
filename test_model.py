from transformers import pipeline
import torch

instruct_pipeline = pipeline(model="databricks/dolly-v2-12b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")


text="亡羊补牢是什么"
result=instruct_pipeline(text)
print(result)
