import cv2
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from scipy.spatial.distance import pdist

st.title("OpenCV Demo App")
st.subheader("This app allows you to play with Image filters!")
st.text("We use OpenCV and Streamlit for this demo")

# Upload options for control and experimental images
control_uploaded_files = {
    'A3L': st.file_uploader("Choose a Control Image A3L", type=["jpeg", "png"]),
    'A3R': st.file_uploader("Choose a Control Image A3R", type=["jpeg", "png"]),
    'A4L': st.file_uploader("Choose a Control Image A4L", type=["jpeg", "png"]),
    'A4R': st.file_uploader("Choose a Control Image A4R", type=["jpeg", "png"]),
}

experimental_uploaded_files = {
    'A3L': st.file_uploader("Choose an Experimental Image A3L", type=["jpeg", "png"]),
    'A3R': st.file_uploader("Choose an Experimental Image A3R", type=["jpeg", "png"]),
    'A4L': st.file_uploader("Choose an Experimental Image A4L", type=["jpeg", "png"]),
    'A4R': st.file_uploader("Choose an Experimental Image A4R", type=["jpeg", "png"]),
}

# Function to convert uploaded file to OpenCV image
def uploaded_file_to_cv2_image(uploaded_file):
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        return image
    return None

# Process the uploaded control and experimental images
control_images = {key: uploaded_file_to_cv2_image(file) for key, file in control_uploaded_files.items()}
experimental_images = {key: uploaded_file_to_cv2_image(file) for key, file in experimental_uploaded_files.items()}

# Check if all images are uploaded
all_control_images_uploaded = all(img is not None for img in control_images.values())
all_experimental_images_uploaded = all(img is not None for img in experimental_images.values())
all_images_uploaded = all_control_images_uploaded and all_experimental_images_uploaded

# Display images and provide annotation canvas
if all_images_uploaded:
    st.success("All images uploaded successfully. Proceed with annotation.")

    control_nucleus_positions = []
    experimental_nucleus_positions = []

    for key in control_images:
        control_image = control_images[key]
        experimental_image = experimental_images[key]

        # Convert images to RGB for display in Streamlit
        control_image_rgb = cv2.cvtColor(control_image, cv2.COLOR_BGR2RGB)
        experimental_image_rgb = cv2.cvtColor(experimental_image, cv2.COLOR_BGR2RGB)

        st.write(f"Annotate the Control Image {key}:")
        control_canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=2,
            stroke_color="green",
            background_image=Image.fromarray(control_image_rgb),
            update_streamlit=True,
            height=control_image.shape[0],
            width=control_image.shape[1],
            drawing_mode="circle",
            key=f"control_canvas_{key}",
        )

        st.write(f"Annotate the Experimental Image {key}:")
        experimental_canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=2,
            stroke_color="yellow",
            background_image=Image.fromarray(experimental_image_rgb),
            update_streamlit=True,
            height=experimental_image.shape[0],
            width=experimental_image.shape[1],
            drawing_mode="circle",
            key=f"experimental_canvas_{key}",
        )

        # Extract the annotations from the canvas result
        if control_canvas_result.json_data is not None:
            control_nucleus_positions.extend([(shape['left'], shape['top']) for shape in control_canvas_result.json_data['objects']])
        if experimental_canvas_result.json_data is not None:
            experimental_nucleus_positions.extend([(shape['left'], shape['top']) for shape in experimental_canvas_result.json_data['objects']])

    st.write(f"Control Nucleus positions: {control_nucleus_positions}")
    st.write(f"Number of Control Nucleus positions: {len(control_nucleus_positions)}")
    st.write(f"Experimental Nucleus positions: {experimental_nucleus_positions}")
    st.write(f"Number of Experimental Nucleus positions: {len(experimental_nucleus_positions)}")

    # Button to process and display plots
    if st.button("Process"):
        if control_nucleus_positions and experimental_nucleus_positions:
            # Calculate distances
            control_distances = pdist(control_nucleus_positions)
            experimental_distances = pdist(experimental_nucleus_positions)

            # Create figures for scatter plot, histograms, and KDE plot
            fig, axs = plt.subplots(2, 3, figsize=(18, 12))

            # Scatter plot of distances for both groups
            axs[0, 0].scatter(range(len(control_distances)), control_distances, color='green', label='Control', alpha=0.5)
            axs[0, 0].scatter(range(len(experimental_distances)), experimental_distances, color='blue', label='Experimental', alpha=0.5)
            axs[0, 0].set_xlabel('Pair Index')
            axs[0, 0].set_ylabel('Distance (mm)')
            axs[0, 0].set_title('Scatter Plot of Nucleus Distances')
            axs[0, 0].legend()

            # Histogram of distances for control group
            axs[0, 1].hist(control_distances, bins=20, color='green', alpha=0.5, label='Control')
            axs[0, 1].set_xlabel('Distance (mm)')
            axs[0, 1].set_ylabel('Frequency')
            axs[0, 1].set_title('Histogram of Nucleus Distances (Control)')
            axs[0, 1].legend()

            # Histogram of distances for experimental group
            axs[0, 2].hist(experimental_distances, bins=20, color='blue', alpha=0.5, label='Experimental')
            axs[0, 2].set_xlabel('Distance (mm)')
            axs[0, 2].set_ylabel('Frequency')
            axs[0, 2].set_title('Histogram of Nucleus Distances (Experimental)')
            axs[0, 2].legend()

            # Combined histogram for both groups
            axs[1, 0].hist(control_distances, bins=20, color='green', alpha=0.5, label='Control')
            axs[1, 0].hist(experimental_distances, bins=20, color='blue', alpha=0.5, label='Experimental')
            axs[1, 0].set_xlabel('Distance (mm)')
            axs[1, 0].set_ylabel('Frequency')
            axs[1, 0].set_title('Combined Histogram of Nucleus Distances')
            axs[1, 0].legend()

            # KDE plots for both groups
            sns.kdeplot(control_distances, color='green', label='Control', fill=True, alpha=0.5, ax=axs[1, 1])
            sns.kdeplot(experimental_distances, color='blue', label='Experimental', fill=True, alpha=0.5, ax=axs[1, 1])
            axs[1, 1].set_xlabel('Distance (mm)')
            axs[1, 1].set_ylabel('Density')
            axs[1, 1].set_title('Frequency Curve of Nucleus Distances')
            axs[1, 1].legend()

            # Display scatter plot of nucleus positions
            ax = axs[1, 2]
            ax.scatter([pos[0] for pos in control_nucleus_positions], [pos[1] for pos in control_nucleus_positions], color='green', label='Control')
            ax.scatter([pos[0] for pos in experimental_nucleus_positions], [pos[1] for pos in experimental_nucleus_positions], color='blue', label='Experimental')
            ax.set_title('Merged Nucleus Positions')
            ax.set_xlabel('X-coordinate')
            ax.set_ylabel('Y-coordinate')
            ax.invert_yaxis()  # Invert y-axis to match image coordinates
            ax.legend()

            # Adjust layout and show plot
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("Please annotate all control and experimental images.")
else:
    st.warning("Please upload all required images.")
    
