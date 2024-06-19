import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Nuclear Distance Analysis Guide",
    page_icon="📖",
)

st.title("Guide for Nuclear Distance Analysis Application")
st.subheader("This guide will walk you through the features and usage of the Nuclear Distance Analysis application.")

st.sidebar.title("Navigation")
st.sidebar.markdown("""
- [Overview](#overview)
- [How to Use the Application](#how-to-use-the-application)
- [Detailed Steps](#detailed-steps)
- [Visualizations](#visualizations)
- [Requirements](#requirements)
- [Contact](#contact)
""", unsafe_allow_html=True)

st.markdown("""

### Overview
The Nuclear Distance Analysis application allows users to upload control and experimental images of Drosophila muscles, annotate nuclei positions, and analyze the distances between nuclei. The app provides visualizations of the distances through scatter plots, histograms, and KDE plots.

### How to Use the Application
1. **Upload Images**
   - The app has two columns for image uploads: one for control images and one for experimental images.
   - Upload your control images in the left column and experimental images in the right column.
   - The accepted image formats are JPEG and PNG.

2. **Annotate Images**
   - Once the images are uploaded, you will be able to annotate the nuclei positions on each image.
   - For each uploaded image, you will see a canvas where you can draw circles to mark the nuclei positions.

3. **Analyze Distances**
   - After annotating all uploaded images, click the "Analyze" button to proceed with the analysis.
   - The app will calculate the distances between the annotated nuclei positions.
   - Click the "Process" button to generate and display visualizations of the distances.

### Detailed Steps
#### Step 1: Upload Control and Experimental Images
- **Control Images**: 
  - A3L: [Upload Control Image A3L]
  - A3R: [Upload Control Image A3R]
  - A4L: [Upload Control Image A4L]
  - A4R: [Upload Control Image A4R]

- **Experimental Images**: 
  - A3L: [Upload Experimental Image A3L]
  - A3R: [Upload Experimental Image A3R]
  - A4L: [Upload Experimental Image A4L]
  - A4R: [Upload Experimental Image A4R]
""")
st.image("C:/Users/fcbwa/OneDrive/Desktop/NNA/nuclear_distance/images/upload.png", caption="Upload")

st.markdown("""
                 
#### Step 2: Annotate Nuclei Positions
- For each uploaded image, you will be provided with a canvas.
- Use the drawing tool to mark the nuclei positions by drawing circles.
- The control images will have green circles, and the experimental images will have yellow circles.
""")

#create columns for images
col1, col2 = st.columns(2)

# Display control image in first column
with col1:
    st.image("C:/Users/fcbwa/OneDrive/Desktop/NNA/nuclear_distance/images/control.png", caption="Control annotation")

# Display experimental image in second column
with col2:
    st.image("C:/Users/fcbwa/OneDrive/Desktop/NNA/nuclear_distance/images/exp.png", caption="Experiments annotation")


st.markdown("""
#### Step 3: Analyze Nuclei Distances
- After annotating all images, click the "Process" button.
- The app will process the annotations, calculate the distances between nuclei and generate visualizations, including scatter plots, histograms, and KDE plots.
- Click the "" button to 
""")
st.image("C:/Users/fcbwa/OneDrive/Desktop/NNA/nuclear_distance/images/process.png", caption="Processing")
st.markdown("""
### Visualizations
- **Scatter Plot**: Shows the distances between nuclei pairs for both control and experimental images.
- **Histogram**: Displays the frequency distribution of distances for control and experimental images separately.
- **Combined Histogram**: A combined view of both histograms.
- **KDE Plot**: Shows the density distribution of distances.
- **Merged Nucleus Positions**: Displays the annotated nuclei positions on a single plot.
""")
st.image("C:/Users/fcbwa/OneDrive/Desktop/NNA/nuclear_distance/images/results.png", caption="Upload")

st.markdown("""
### Requirements
Ensure you have the following Python packages installed:
```plaintext
streamlit
opencv-python
openpyxl
matplotlib
numpy
scipy
pandas
seaborn
pillow
streamlit-drawable-canvas
""")

st.markdown("""
### Contact
For any issues or questions, please contact fcb.adnan10@gmail.com.

We hope this guide helps you in using the Nuclear Distance Analysis application effectively!
""")
