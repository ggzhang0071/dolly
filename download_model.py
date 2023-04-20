from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-12b")

model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-12b")
