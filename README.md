# RemoveBG - Background Removal Web Application

This project is a simple web application built with **Flask** that allows users to upload an image, remove its background, and download the processed image.
The application leverages background removal functionality and displays the result on the web page for easy access.

## Features
- 📤 **File Upload**: Users can upload an image to the application.
- 🧹 **Background Removal**: The application removes the background of the uploaded image.
- 👁️‍🗨️ **Preview**: Displays the output image as a preview on the page.
- ⬇️ **Download**: Provides a download button to download the output image.

## Technologies Used
- 🐍 **Python 3.x**
- ⚙️ **Flask**: A lightweight WSGI web application framework.
- 🌐 **HTML, CSS, JavaScript**: For frontend UI and interactivity.
- **Pillow**: A image processing library.

  
## Project Structure
```text
RemoveBG/
├── app.py # Flask backend (main application file)
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Main HTML page
└── static/
├── style.css # Custom styles
└── output/ # Output folder where processed images are saved
└── uploads/ # Folder where uploaded images are stored
```

```bash
mkdir RemoveBG
cd RemoveBG

:: Create files
echo. > app.py
echo. > requirements.txt

:: Create templates folder and index.html
mkdir templates
cd templates
echo. > index.html
cd ..

:: Create static folder with subfolders and files
mkdir static
cd static
echo. > style.css
mkdir output
mkdir uploads
cd ..
```

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/misterraju/RemoveBackground.git
cd RemoveBG
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Create Folders
Ensure that the following folders exist:

uploads/ - to store uploaded images.

static/output/ - to store output images with removed backgrounds.

If the folders are missing, create them manually, or the application will automatically generate them if the code is correctly set up.

```bash
mkdir uploads
mkdir static/output
```
### 4. Run the Application
```bash
python app.py
```
This will start the Flask development server at http://127.0.0.1:5000.

### 5. Open the Application
Open your web browser and go to http://127.0.0.1:5000. You can upload an image, remove its background, and preview the result directly from the web page.

## How it Works

1.  **Uploading an Image**: The user selects an image file using the file input field in the form.
2.  **Processing the Image**: Once the image is uploaded, the background is removed using the `remove_background` function in the backend.
3.  **Previewing the Image**: The output image is displayed on the page for the user to preview.
4.  **Downloading the Output**: The user can download the processed image by clicking the "Download Output" button.

## Requirements

To run this project, you need to have the following installed:

*   **Python 3.x**: Download from [python.org](https://www.python.org/).
*   **Flask**: A lightweight Python web framework.
*   **Pillow**: A image processing library.

## Author

*   **Raju Ghimire** - [MisterRaju](https://www.github.com/MisterRaju)
---

If you find any bugs or want to contribute, feel free to fork the repository and submit a pull request.
