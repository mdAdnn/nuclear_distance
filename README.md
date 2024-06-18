# Nuclear Distance Analysis

This Python script performs analysis on the distances between nucleus positions in microscopy images for control and experimental groups. It calculates pairwise distances, visualizes the data with histograms, scatter plots, and KDE plots, and conducts statistical tests to compare the groups.

## Features

- Annotation of nucleus positions on microscopy images.
- Calculation of pairwise distances between nucleus positions.
- Visualization of nucleus positions and distances.

## Dependencies

- streamlit
- opencv-python
- openpyxl
- matplotlib
- numpy
- scipy
- pandas
- seaborn
- pillow
- streamlit-drawable-canvas

# Setting up terminal
1. create python environment:
    ```bash
    python -m venv venv
    ```
2. activate the env:
   ```bash
    venv\scripts\activate
    ```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mdAdnn/nuclear_distance.git
    ```

2. Install Python and required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the script:
   ```bash
   streamlit run Welcome.py
   ```

## Navigating through the web-app.
 - To display more pages and options, click on the arrow in the top left corner.

## Follow the instructions to annotate nucleus positions on control and experimental images.

1. Run the Python Script: Execute the Python script provided in the project directory by running the following command in your terminal or command prompt:
    ```bash
    streamlit run Welcome.py
    ```
2. Upload the images of controls and experiments:
   - Once the script is running, it will open the web page.
   - Web-page contains total of 8 upload files option (4 for controls and 4 for experiments).
   - Upload the images of segment A3 right and left, A4 right and left segment of the sample respectively for controls and experiments.
3. Annotate the images:
   - Once all the images are uploaded you can select the desired nucleus from each image.
   - After the selection click process to obtain plot for the overall comparision.
  
By following these steps, you can effectively view the generated plots and statistical analysis results after annotating nucleus positions using the streamlit app.

## Contributors
You've installed all the necessary tools and dependencies and can now run the provided code successfully. Let me know if you need further assistance!
Mohd Adnan
Email:fcb.adnan10@gmail.com
