import kagglehub

# Download latest version
path = kagglehub.dataset_download("shrutimehta/zomato-restaurants-data")

print("Path to dataset files:", path)