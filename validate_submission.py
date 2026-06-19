import os
import pandas as pd
import nbformat
from pptx import Presentation
import cv2

# Define expected files
required_files = {
    "CostBenefit.xlsx": "Excel workbook for cost-benefit analysis",
    "FraudDetection.ipynb": "Jupyter notebook for fraud detection",
    "Storytelling.pptx": "PowerPoint presentation for data storytelling",
    "ResultsImpact.mp4": "Video explaining results and business impact"
}

def validate_submission(folder_path):
    print("🔍 Validating submission package...\n")
    
    for file_name, description in required_files.items():
        file_path = os.path.join(folder_path, file_name)
        
        if not os.path.exists(file_path):
            print(f"❌ Missing: {file_name} ({description})")
            continue
        
        try:
            if file_name.endswith(".xlsx"):
                pd.ExcelFile(file_path)  # Try loading Excel
            elif file_name.endswith(".ipynb"):
                nbformat.read(file_path, as_version=4)  # Validate notebook
            elif file_name.endswith(".pptx"):
                Presentation(file_path)  # Validate PPT
            elif file_name.endswith(".mp4"):
                cap = cv2.VideoCapture(file_path)
                if not cap.isOpened():
                    raise ValueError("Video cannot be opened")
                cap.release()
            print(f"✅ Valid: {file_name} ({description})")
        except Exception as e:
            print(f"⚠️ Corrupt or unreadable: {file_name} → {e}")

# Example usage
validate_submission("Submission_Package")
