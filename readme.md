# YouTube Video Content Assistant

This project provides a Streamlit-based web application designed to assist in generating titles and scripts for YouTube videos. Utilizing the power of OpenAI's language models via the LangChain library, it offers a user-friendly interface to input video topics and receive creative, AI-generated content suggestions.

## Features

- Generate compelling YouTube video titles based on input topics.
- Produce detailed video scripts leveraging Wikipedia research and AI creativity.
- Review previous titles and scripts generated during the session.
- Access and utilize Wikipedia research directly within the app for enhanced content creation.

## Getting Started

To run this application on your local machine, follow these steps:

### Prerequisites

Ensure you have Python 3.8 or later installed, along with pip for package management.

### Installation

1. Clone the repository to your local machine:

git clone git@github.com:ericmartinez1189/youtube_script_assistance.git

2. Navigate to the cloned repository directory:

cd your-repository

3. Install the required dependencies:

pip install -r requirements.txt

4. To launch the Streamlit application, run:

streamlit run app.py

Navigate to the displayed URL in your browser to interact with the application.

### Application Files
**app.py:** The main Python file that launches the Streamlit web application. Use this file to see the application in action and interact with the AI-generated content features.

**UnderstandingLangChain.ipynb:** A Jupyter Notebook file that provides a detailed exploration of the functionality and logic behind using LangChain for building this application. It's recommended for those who want to understand the underlying processes and customize the application further.

### How It Works
The application uses LangChain to integrate OpenAI's language models for generating video content. Users input a video topic, and the application leverages LangChain's capabilities to generate a title and script, utilizing Wikipedia for research when necessary.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
OpenAI for the GPT models.
LangChain community for the tools and libraries facilitating AI model integration.
Streamlit for the amazing framework that makes web applications accessible to data scientists.