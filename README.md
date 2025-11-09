# Integrating GPT and Hugging Face Models into Web Projects

Gen-AI is an innovative Python project designed to explore, implement, and integrate AI algorithms into practical web-based applications.
This repository demonstrates how to deploy and interact with Generative AI models — including Hugging Face APIs, chatbots, and image-enhanced systems — all within modular Python projects.

## Overview

This repository hosts multiple AI-powered Python projects built around natural language processing, image generation, and interactive applications.
It now integrates Hugging Face inference APIs, allowing seamless deployment of generative models (like Zephyr or Mistral) without requiring local downloads or heavy compute.

The **main** branch serves as a stable base that integrates the project’s core frameworks, while each feature branch experiments with different Gen-AI capabilities.

## Branches

1. [AI-Assistant](https://github.com/Shrvaani/Gen-AI-Using-Python/tree/AI_Assistant) - An AI-powered virtual assistant that answers user queries using LLMs.
2. [AI-Powered-Image-Gallery](https://github.com/Shrvaani/Gen-AI-Using-Python/tree/AI_Powered_Image_Gallery) - An intelligent image gallery with automated tagging and categorization.

##Hugging Face Integration:
The LaughBot branch now uses the Hugging Face Router API instead of OpenAI.
This allows the chatbot to run fully in the cloud — ideal for deploying on Streamlit Cloud or Hugging Face Spaces, without requiring any local downloads or model hosting.

## Installation & Setup
Ensure you have the required Python dependencies installed.

```
pip install -r requirements.txt
```
##Requirements include:

```
streamlit
requests
colorama
python-dotenv
huggingface-hub
```

## Usage

1. Clone the Repository
```
git clone <repo_url>
cd <repo_folder>
```
2. Set Up Environment Variables
Create a **.env** file in your project root and add:

```
HF_TOKEN=your_huggingface_api_token
HF_MODEL_ID=HuggingFaceH4/zephyr-7b-beta
```
##Run the App (Streamlit)

```
streamlit run main.py
```

##Access the App:

```
Local: http://localhost:8501
```