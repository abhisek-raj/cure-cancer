# Cancer Cure Q&A System

A Flask-based web application that provides information about natural cancer treatments based on Dr. Hulda Clark's research from "The Cure for All Cancers". The system uses a combination of machine learning and keyword analysis to answer questions about various treatment approaches.

## Features

- Interactive Q&A interface
- Machine learning-based question classification
- Keyword analysis for precise responses
- Statistics and analytics dashboard
- Responsive design for all devices
- Example questions for easy start

## Installation

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Place your trained ML model file (`cure_cancer_text_classifier_*.pkl`) in the project root directory if you have one.

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
my_model_bot/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── static/              # Static files (CSS, JS, images)
└── templates/           # HTML templates
    ├── index.html       # Main Q&A interface
    ├── stats.html       # Statistics page
    └── about.html       # About page
```

## Usage

1. Enter your question in the input field on the home page
2. Click "Get Treatment Answer" to submit
3. View the generated response and analysis
4. Explore example questions to get started
5. Check the statistics page for usage analytics

## Note on Machine Learning Model

The application is designed to work with a pre-trained machine learning model for question classification. If no model is found, the system will fall back to keyword-based matching. To use the ML features, place your trained model file in the project root directory.

## License

This project is for educational purposes only. The information provided is not intended as medical advice. Always consult with qualified healthcare professionals for medical advice and treatment.

## Disclaimer

This application is based on the research of Dr. Hulda Clark but is not affiliated with or endorsed by her or her estate. The information provided should not be considered as medical advice. Always consult with a qualified healthcare professional before starting any treatment.
