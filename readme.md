# Digital Twin Generation with Voice Cloning and Realistic Video

This project was developed as part of the Techolution Hackathon. This repository contains the code and instructions for creating a near real-time digital twin using advanced voice cloning and realistic video generation techniques. Our solution aims to tackle the challenge of generating a digital clone of a person, combining their voice, expressions, and speech in a lifelike manner.

## Problem Statement

The challenge presented in the hackathon involves creating AI models capable of the following:

1. **Advanced Neural Architectures**: Utilizing state-of-the-art deep learning techniques, including recurrent neural networks (RNNs), convolutional neural networks (CNNs), and generative adversarial networks (GANs) for voice cloning and spoof video generation.

2. **Expressiveness**: Developing models that can faithfully capture a wide range of emotions, accents, and speaking styles, allowing for expressive voice cloning and fluid video generation from a 2D image.

3. **Naturalness**: Ensuring that the generated voice clones sound natural and human-like, while focusing on generating accurate lip sync and realistic video corresponding to cloned audio.

4. **Robustness**: Enhancing the robustness of the AI models to perform well with limited training data and in challenging acoustic environments. For video, the goal is to minimize traces of fake elements.

5. **Real-Time Nature**: Creating an ensemble of voice cloning and spoof video generation models that operate in near real-time, making it suitable for conversational AI applications.

## Solution Architecture

We approached this problem by leveraging two separate components:

1. **Voice Cloning and Text-to-Speech (TTS)**: We utilize the [Tortoise-TTS](https://github.com/neonbjb/tortoise-tts) repository for both voice cloning and generating speech from a text prompt. This component allows users to upload a sample audio file for voice cloning and specify a text prompt for generating the cloned voice.

2. **Realistic Video Generation**: For generating realistic videos with lip-sync, we used the [SadTalker](https://github.com/OpenTalker/SadTalker) repository. It takes an input image, an audio file from the voice cloning step, and generates a video with lip-sync.

To accommodate the processing requirements and avoid crashes, we used separate Google Colab instances for each component. We also configured ngrok with Flask to create accessible URLs for integration with a Streamlit application.

## Running the Code

To run the complete system, follow these steps:

1. Upload `TorTTS_API.ipynb` to one Colab instance and `Vid_API.ipynb` to another Colab instance.

2. Configure ngrok APIs in both instances.

3. Enter the ngrok URLs generated in step 2 into the `app.py` file.

4. Run the Streamlit application using the command: `streamlit run app.py`.

5. In the Streamlit application, users can perform the following steps:
   - Upload a sample audio file for voice cloning.
   - Specify a text prompt for generating speech.
   - Upload an image of the person whose voice is to be cloned.
   - The system will generate a video with lip-sync using the audio and image provided.


https://github.com/pnkvalavala/digitaltwin/assets/108526358/f6ea634a-65ee-4d2e-92fd-f52c96613959


## Additional Notes

- If you have access to powerful GPUs, you can combine both `TorTTS_API.ipynb` and `Vid_API.ipynb` to run in a single Colab instance for faster processing or in your local machine.

- Note that the Streamlit application is designed for local use, so users will need to clone this repository and run the application on their own machines.
