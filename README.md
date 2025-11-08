## An AI-powered Image Gallery

An AI-enhanced image gallery built with Streamlit and Hugging Face Inference API.
Users can generate AI images from text prompts, view them instantly, and browse a saved gallery — all cloud-based.

## Requirements:

1. **requests**: [HuggingFace](https://huggingface.co/): HTTP library used to communicate with Hugging Face API.
2. **Streamlit**: [Streamlit](https://streamlit.io/): It is an open-source Python toolkit that facilitates the development of stunning, personalized online applications for data science and machine learning.
3. **python-dotenv**: [Python Dotenv](https://pypi.org/project/python-dotenv/): Adds the key-value pair to the environment variable by reading it from the.env file. Using the 12-factor principle, it is excellent for controlling app settings both in development and production.
4. **pillow**: [Pillow](https://pypi.org/project/Pillow/): Pillow is Alex Clark and Contributors' amiable PIL fork. The Python Imaging Library (PIL) was created by Fredrik Lundh and his collaborators.

## Create a virtual environment :

**MacOS/Linux**:

```
python3 -m venv env
```

**Windows**:

```
python -m venv env
```

## Activate the virtual environment :

```
source env/bin/activate
```

## Installation:

**MacOS/Linux**:

```
pip3 install -r requirements.txt
pip3 install streamlit streamlit-chat
```

**Windows**:

```
pip install -r requirements.txt
pip install streamlit streamlit-chat
```

## [Set up Hugging Face API access](https://huggingface.co/settings/tokens)

1. Go to your Hugging Face account → Settings → Access Tokens

2. Create a new token with read access.

3. Add it to your **.env** file:

```
HF_TOKEN=your_huggingface_token
HF_MODEL_ID=black-forest-labs/FLUX.1-dev
```

## Start the app:

`streamlit run main.py`

Then open the provided local URL (usually http://localhost:8501).

**Deployment options**:

## Deploy on Streamlit Cloud:

1. Push your repo to GitHub.

2. Go to streamlit.io/cloud → New app → select your repo.

3. Under App secrets, add:

```
HF_TOKEN = your_huggingface_token
HF_MODEL_ID = black-forest-labs/FLUX.1-dev
```
4. Deploy — the app auto-installs dependencies and launches.

## Deploy on Hugging Face Spaces
1. Go to huggingface.co/spaces → Create new Space.

2. Choose Streamlit as SDK.

3. Upload your project or link GitHub.

4. Add your Hugging Face token under Settings → Secrets.

5. Click Restart Space — your app will run live.

