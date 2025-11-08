# Project : Integrating the GPT models into Web Projects

## **Install Python** ![Python](img/python_65.png)

- A [Quick Guide for Installing](https://github.com/PackeTsar/Install-Python/blob/master/README.md#install-python-) Python on Common Operating Systems
- Download the latest version of [Python 3.12](https://www.python.org/downloads/)

## Create a virtual environment :

(Windows)
```
python -m venv env
```

(MacOS)
```
python3 -m venv env
```

## Activate the virtual environment :

```
source env/bin/activate
```

## Installation:
(Windows)
```
pip install -r requirements.txt
```

(MacOS)

```
pip3 install -r requirements.txt
```

## [Get a Hugging Face API Key](https://huggingface.co/settings/tokens)

1. Visit https://huggingface.co/settings/tokens

2. Click “New Token”

3. Choose Read Access

4. Copy your token (it starts with hf_...)

## .env File Setup:

Create a **.env** file in your project root:

```
HF_TOKEN=hf_your_huggingface_token_here
```

## Run the script:

(Windows)
```
streamlit run main.py
```

(MacOS)
```
streamlit run main.py
```

##Tech Stack:

**Language:** Python 3.12

**Framework:** Streamlit

**Model Provider:** Hugging Face Inference API

**Model Used:** openai/gpt-oss-20b (or any other open-source model of your choice)

**Environment Management:** Python venv

**Environment Variables:** Managed using python-dotenv