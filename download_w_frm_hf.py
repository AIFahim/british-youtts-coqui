from huggingface_hub import snapshot_download
snapshot_download(repo_id="voices/VCTK_British_English_Males",local_dir="./weight_hf", local_dir_use_symlinks=False)

