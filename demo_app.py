import cv2
import streamlit as st
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist, squareform
import pandas as pd
import seaborn as sns  # Import Seaborn for KDE plots
from PIL import Image


st.title("OpenCV Demo App")
st.subheader("This app allows you to play with Image filters!")
st.text("We use OpenCV and Streamlit for this demo")

# Function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Function to calculate Euclidean distance between two points in millimeters
def calculate_distance_mm(point1, point2, scale_mm_per_pixel):
    distance_pixels = calculate_distance(point1, point2)
    distance_mm = distance_pixels * scale_mm_per_pixel
    return distance_mm

# Global variables to store the nucleus positions for control and experimental groups
control_nucleus_positions = []
experimental_nucleus_positions = []

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global control_nucleus_positions, experimental_nucleus_positions
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the mouse click is for the control image or the experimental image
        if param == 'control':
            control_nucleus_positions.append((x, y))
            print("Control Nucleus positions:", control_nucleus_positions)
        elif param == 'experimental':
            experimental_nucleus_positions.append((x, y))
            print("Experimental Nucleus positions:", experimental_nucleus_positions)

# Paths to the image files for control and experimental groups
control_file_path = r"C:\Users\fcbwa\OneDrive\Desktop\NNA\Nucleia-Distance\CHD1_NLS\JPG\Females\Control\A3 L.jpg"
experimental_file_path = r"C:\Users\fcbwa\OneDrive\Desktop\NNA\Nucleia-Distance\CHD1_NLS\JPG\Males\Experiments\A3 L.jpg"

# Load the control image
control_image = cv2.imread(control_file_path)
if control_image is None:
    print("Error: Unable to load the control image.")
    exit()
print("Control Image loaded successfully.")

# Load the experimental image
experimental_image = cv2.imread(experimental_file_path)
if experimental_image is None:
    print("Error: Unable to load the experimental image.")
    exit()
print("Experimental Image loaded successfully.")

# Display the control image for annotation
cv2.imshow('Control Image for Annotation', control_image)
cv2.setMouseCallback('Control Image for Annotation', mouse_callback, param='control')
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the experimental image for annotation
cv2.imshow('Experimental Image for Annotation', experimental_image)
cv2.setMouseCallback('Experimental Image for Annotation', mouse_callback, param='experimental')
cv2.waitKey(0)
cv2.destroyAllWindows()

