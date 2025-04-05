from faker import Faker
import random
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
import qrcode

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Function to generate a fake Aadhaar number
def generate_aadhaar_number():
    first_digit = random.randint(2, 9)
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    num = f"{first_digit}{remaining_digits}"
    return f"{num[:4]} {num[4:8]} {num[8:]}"

# Directory setup
output_dir = "synthetic_aadhaar_cards"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters
num_records = 200  # Generate 200 Aadhaar cards

# Load resources
logo_path = r'C:\Users\Priyesh Pandey\OneDrive\Desktop\kyc-auth-protocol\config\api\_Synthetic\Resources\ashok-stambh.png'
bharat_sarkar_path = r'C:\Users\Priyesh Pandey\OneDrive\Desktop\kyc-auth-protocol\config\api\_Synthetic\Resources\bharat-sarkar.png'
face_path = r'C:\Users\Priyesh Pandey\OneDrive\Desktop\kyc-auth-protocol\config\api\_Synthetic\Resources\human-2.jpg'
footer_path = r'C:\Users\Priyesh Pandey\OneDrive\Desktop\kyc-auth-protocol\config\api\_Synthetic\Resources\footer.png'
qr_code_path = r'C:\Users\Priyesh Pandey\OneDrive\Desktop\kyc-auth-protocol\config\api\_Synthetic\Resources\QR_Code.png'

# Check if files exist
for path in [logo_path, bharat_sarkar_path, face_path, footer_path, qr_code_path]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found at {path}. Ensure it exists.")

# Load and resize images
logo = Image.open(logo_path).convert("RGBA").resize((50, 50), Image.Resampling.LANCZOS)
bharat_sarkar = Image.open(bharat_sarkar_path).convert("RGBA").resize((300, 30), Image.Resampling.LANCZOS)
face = Image.open(face_path).convert("RGBA").resize((100, 120), Image.Resampling.LANCZOS)
footer = Image.open(footer_path).convert("RGBA").resize((600, 30), Image.Resampling.LANCZOS)
qr_code = Image.open(qr_code_path).convert("RGBA").resize((120, 120), Image.Resampling.LANCZOS)  # Enlarged QR code

# Font setup
try:
    font = ImageFont.truetype("arial.ttf", 20)  
    hindi_font = ImageFont.truetype("Nirmala.ttf", 20)  
except:
    font = ImageFont.load_default()
    hindi_font = font  

# Generate synthetic Aadhaar cards
data = {
    "Aadhaar Number": [],
    "Name": [],
    "Date of Birth": [],
    "Gender": [],
    "Image File": []
}

for i in range(num_records):
    aadhaar_num = generate_aadhaar_number()
    name = fake.name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y")
    gender = random.choice(["पुरुष (Male)", "महिला (Female)", "अन्य (Other)"])  

    # Add to dataset
    data["Aadhaar Number"].append(aadhaar_num)
    data["Name"].append(name)
    data["Date of Birth"].append(dob)
    data["Gender"].append(gender)

    # Create template
    template = Image.new('RGB', (600, 300), color='white')
    draw = ImageDraw.Draw(template)

    # Add header elements
    template.paste(logo, (10, 10), logo)
    template.paste(bharat_sarkar, (150, 5), bharat_sarkar)

    # Add profile image
    template.paste(face, (20, 80), face)

    # Personal details (Hindi inclusion)
    draw.text((200, 40), f"{name}", fill="black", font=font)  
    draw.text((200, 70), f"जन्म तिथि: {dob}", fill="black", font=hindi_font)
    draw.text((200, 100), f"लिंग: {gender}", fill="black", font=hindi_font)

    # Aadhaar number (aligned correctly)
    draw.text((200, 190), aadhaar_num, fill="black", font=ImageFont.truetype("arial.ttf", 30))  

    # QR Code placement
    template.paste(qr_code, (450, 110), qr_code)  

    # Footer placement
    template.paste(footer, (0, template.height - footer.height), footer)

    # Save the image
    image_filename = f"{output_dir}/aadhaar_card_{i+1}.png"
    template.save(image_filename)
    data["Image File"].append(image_filename)

    if i % 100 == 0:
        print(f"Generated {i} Aadhaar images...")

# Save data as CSV
df = pd.DataFrame(data)
df.to_csv("synthetic_aadhaar_data.csv", index=False)

# Print confirmation
print(f"Generated {num_records} synthetic Aadhaar records and images.")
print("Text data saved to 'synthetic_aadhaar_data.csv'")
print(f"Images saved in '{output_dir}' folder")
print("\nSample of the dataset:")
print(df.head())
