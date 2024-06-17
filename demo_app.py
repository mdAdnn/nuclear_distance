import cv2
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from scipy.spatial.distance import pdist, squareform

st.title("OpenCV Demo App")
st.subheader("This app allows you to play with Image filters!")
st.text("We use OpenCV and Streamlit for this demo")

# Upload options for control and experimental images
control_uploaded_file = st.file_uploader("Choose a Control Image", type=["jpeg", "png"])
experimental_uploaded_file = st.file_uploader("Choose an Experimental Image", type=["jpeg", "png"])

# Function to convert uploaded file to OpenCV image
def uploaded_file_to_cv2_image(uploaded_file):
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        return image
    return None

# Process the uploaded control image
control_image = uploaded_file_to_cv2_image(control_uploaded_file)

# Process the uploaded experimental image
experimental_image = uploaded_file_to_cv2_image(experimental_uploaded_file)

# Display images and provide annotation canvas
if control_image is not None and experimental_image is not None:
    st.success("Both images uploaded successfully. Proceed with annotation.")

    # Convert images to RGB for display in Streamlit
    control_image_rgb = cv2.cvtColor(control_image, cv2.COLOR_BGR2RGB)
    experimental_image_rgb = cv2.cvtColor(experimental_image, cv2.COLOR_BGR2RGB)

    st.write("Annotate the Control Image:")
    control_canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=2,
        stroke_color="green",
        background_image=Image.fromarray(control_image_rgb),
        update_streamlit=True,
        height=control_image.shape[0],
        width=control_image.shape[1],
        drawing_mode="circle",
        key="control_canvas",
    )

    st.write("Annotate the Experimental Image:")
    experimental_canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=2,
        stroke_color="yellow",
        background_image=Image.fromarray(experimental_image_rgb),
        update_streamlit=True,
        height=experimental_image.shape[0],
        width=experimental_image.shape[1],
        drawing_mode="circle",
        key="experimental_canvas",
    )

    # Extract the annotations from the canvas result
    control_nucleus_positions = []
    if control_canvas_result.json_data is not None:
        control_nucleus_positions = [(shape['left'], shape['top']) for shape in control_canvas_result.json_data['objects']]
        st.write(f"Control Nucleus positions: {control_nucleus_positions}")

    experimental_nucleus_positions = []
    if experimental_canvas_result.json_data is not None:
        experimental_nucleus_positions = [(shape['left'], shape['top']) for shape in experimental_canvas_result.json_data['objects']]
        st.write(f"Experimental Nucleus positions: {experimental_nucleus_positions}")

    # Button to process and display plots
    if st.button("Process"):
        if control_nucleus_positions and experimental_nucleus_positions:
            # Calculate distances
            control_distances = pdist(control_nucleus_positions)
            experimental_distances = pdist(experimental_nucleus_positions)

            # Merge nucleus positions if both groups have the same number of positions
            if len(control_nucleus_positions) == len(experimental_nucleus_positions):
                merged_positions = np.concatenate((control_nucleus_positions, experimental_nucleus_positions), axis=0)

                # Create a figure to display images and plots
                fig, ax = plt.subplots(figsize=(8, 8))

                # Display control group nucleus positions
                control_positions = np.array(control_nucleus_positions)
                ax.scatter(control_positions[:, 0], control_positions[:, 1], color='green', label='Control')

                # Display experimental group nucleus positions
                experimental_positions = np.array(experimental_nucleus_positions)
                ax.scatter(experimental_positions[:, 0], experimental_positions[:, 1], color='blue', label='Experimental')

                ax.set_title('Merged Nucleus Positions')
                ax.set_xlabel('X-coordinate')
                ax.set_ylabel('Y-coordinate')
                ax.invert_yaxis()  # Invert y-axis to match image coordinates
                ax.legend()

                # Show the plot
                plt.tight_layout()

                # Download plot button
                st.pyplot(fig)
                
            else:
                st.warning("Number of nucleus positions in control and experimental groups are different. Cannot merge.")
        else:
            st.warning("Please annotate both control and experimental images.")

