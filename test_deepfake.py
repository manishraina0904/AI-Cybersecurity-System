from src.deepfake import detect_deepfake

img_path = input("Enter image path: ")
result = detect_deepfake(img_path)

print("Result:", result)