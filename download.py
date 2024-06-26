from huggingface_hub import snapshot_download

model_id = "psymon/KoLlama2-7b"
snapshot_download(repo_id=model_id, local_dir="KoLlama2-hf", local_dir_use_symlinks=False, revision="main")
