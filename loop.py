import gensim

def summarize(text):
  """Summarizes the given text.

  Args:
    text: The text to be summarized.

  Returns:
    A summary of the text.
  """

  # Create a Gensim summarization object.
  summarizer = gensim.summarization.summarizer.Summarizer()

  # Summarize the text.
  summary = summarizer(text)

  # Return the summary.
  return summary

# Example usage:

text = """
Natural language processing (NLP) is a field of computer science and artificial intelligence that deals with the interaction between computers and human (natural) languages. It's used to give computers the ability to understand and process human language, including speech and text.

NLP is used in a wide variety of AI applications, including:

* Machine translation: NLP is used to translate text from one language to another.
* Text classification: NLP is used to classify text into different categories, such as spam or not spam, or positive or negative sentiment.
* Question answering: NLP is used to answer questions posed in natural language.
* Chatbots: NLP is used to create chatbots that can converse with humans in a natural way.
* Speech recognition: NLP is used to convert speech to text.
* Text summarization: NLP is used to summarize long pieces of text into shorter ones.
* Named entity recognition: NLP is used to identify named entities in text, such as people, places, and organizations.
"""

summary = summarize(text)

# Print the summary.
print(summary)
