import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os

# Directory containing trained Aadhaar card designs
dataset_dir = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\kyc-auth-protocol\synthetic_aadhaar_cards"

# Function to compute Structural Similarity Index (SSIM)
def compute_ssim(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(gray1, gray2, full=True)
    return score

# Function for ORB feature matching
def compute_orb_similarity(img1, img2):
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    if descriptors1 is None or descriptors2 is None:
        return 0

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2)

    return len(matches) / max(len(keypoints1), len(keypoints2))

# Function to validate an Aadhaar image
def validate_aadhaar_card(input_image_path):
    input_image = cv2.imread(input_image_path)
    input_image = cv2.resize(input_image, (600, 300))

    best_match = 0

    # Iterate through dataset images
    for filename in os.listdir(dataset_dir):
        dataset_image_path = os.path.join(dataset_dir, filename)
        dataset_image = cv2.imread(dataset_image_path)
        dataset_image = cv2.resize(dataset_image, (600, 300))

        ssim_score = compute_ssim(input_image, dataset_image)
        orb_score = compute_orb_similarity(input_image, dataset_image)

        similarity_score = (ssim_score + orb_score) / 2  # Average similarity
        best_match = max(best_match, similarity_score)

    print(f"Best Match Score: {best_match * 100:.2f}%")

    return best_match >= 0.30  # Accept if ≥60%

# Example Usage
input_image_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\kyc-auth-protocol\config\api\TestDataset\invalid-2.jpeg"
is_valid = validate_aadhaar_card(input_image_path)

if is_valid:
    print("✅ Valid Aadhaar Card!")
else:
    print("❌ Invalid Aadhaar Card!")
