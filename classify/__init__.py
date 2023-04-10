import os

import openai

key_value_prompts = {
    "ita_v1": {
        "prompt": "Classifica questo testo con etichette di una unica parola separate per virgola, "
              "relative al tono, stato emotivo, argumento, livello di esperienze:\n{{text}}\n",
        "ghost_tags": ["", " ", "  ", "tono", "stato emotivo", "argumento", "livello di esperienze"]
    }
}


def openai_classify(text: str, prompt_version: str) -> list[str]:
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=key_value_prompts[prompt_version]["prompt"].replace("{{text}}", text),
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        text = response.choices[0].text
        tags = [tag.strip() for tag in text.split(",")]
        return [tag for tag in tags if tag not in key_value_prompts[prompt_version]["ghost_tags"]]
    except Exception as e:
        print(e)

    return []


def classify(text_file_path, classify_driver, prompt_version) -> list[str]:
    with open(text_file_path, "r") as f:
        text = f.read()

    print(f"Classifying using {classify_driver.__name__} with {prompt_version}...")
    tags = classify_driver(text, prompt_version)
    print("Tags:", tags)
    return tags
