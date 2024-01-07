import os 
from huggingface_hub import hf_hub_download 

hf_hub_download(repo_id="internlm/internlm-20b", filename="config.json",cache_dir="./down")