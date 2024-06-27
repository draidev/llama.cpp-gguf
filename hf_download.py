import sys
from huggingface_hub import snapshot_download

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 download.py <model_name>")
        sys.exit(1)

    model_id= sys.argv[1]
    snapshot_download(repo_id=model_id, local_dir="llam3-Korean-Bllossom-8B", local_dir_use_symlinks=False, revision="main")
