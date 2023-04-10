echo-me
=======

A PoC to fine-tune an OpenAI model to adopt a specific style of writing using WhatsApp audio messages.

### Work in progress - not ready for use
**What**: With this project we want to fine-tune an OpenAI model to adopt a specific style of writing using WhatsApp audio messages.<br/>
**Goal**: The model will then be able to generate text in the same style as the author.<br/>

### Challenges
 - [x] Extract text from audio;
 - [ ] Create a dataset of conversations;
 - [ ] Classify conversations by argument, tone, context; 
 - [ ] Fine-tune the model to adopt the style of the author;
 - [ ] Generate text in the same style as the author.
 - [ ] Create a web app to interact with the model.

### Requirements

 - [Python](https://www.python.org/downloads/release/python-360/)
 - [pipenv](https://docs.pipenv.org/)
 - [OpenAI API Key](https://openai.com/)

### Setup
 1. Clone the repository
 2. Install dependencies with `pipenv install`
 3. Clone the `.env.example` file to `.env` and add your OpenAI API key

