import openai
from .config import Config

class LLMAgent:
    """
    Wrapper around OpenAI’s ChatCompletion API for natural-language analysis.
    """

    def __init__(self, model: str = "gpt-4o-mini"):
        openai.api_key = Config.OPENAI_API_KEY
        openai.api_base = Config.OPENAI_API_BASE
        self.model = model

    def ask(self, prompt: str, temperature: float = 0.2, max_tokens: int = 512) -> str:
        """
        Send a prompt to the LLM and return the generated response text.
        :param prompt: The natural-language query or instruction.
        :param temperature: Sampling temperature.
        :param max_tokens: Max tokens in the completion.
        :return: Generated text from the model.
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()

git add src/llm_agent.py
git commit -m "Add LLM agent wrapper for OpenAI ChatCompletion"
