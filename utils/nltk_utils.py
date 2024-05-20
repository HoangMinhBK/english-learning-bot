# utils/nltk_utils.py
import re
import nltk
from nltk.corpus import wordnet

# Download NLTK resources (required for WordNet)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


class NLTKUtils:
    @staticmethod
    def get_word_meanings(word):
        meanings = []
        for synset in wordnet.synsets(word):
            meanings.append(synset.definition())
        return meanings

    @staticmethod
    def get_word_details(word):
        details = []
        synsets = wordnet.synsets(word)

        for synset in synsets:
            # Get the first definition (if available)
            definition = (
                synset.definition() if synset.definition() else "No definition found."
            )

            # Get synonyms
            synonyms = (
                ", ".join(synset.lemma_names()[:3])
                if synset.lemma_names()
                else "No synonyms found."
            )

            # Get usage example (if available)
            example = (
                synset.examples()[0] if synset.examples() else "No example available."
            )

            # Get pronunciation (if available)
            pronunciation = (
                synset.pronunciations()[0]
                if hasattr(synset, "pronunciations") and synset.pronunciations()
                else "No pronunciation available."
            )

            details.append(
                {
                    "definition": definition,
                    "synonyms": synonyms,
                    "example": example,
                    "pronunciation": pronunciation,
                }
            )

            # Limit to the first 3 senses
            if len(details) >= 3:
                break

        return details

    @staticmethod
    def highlight_and_define_words(text):
        words = nltk.word_tokenize(text)
        highlighted_text = text
        word_details = {}
        highlighted_count = 0  # Counter for the number of highlighted words

        for word in words:
            # Check if the word is not a punctuation mark or a stopword
            if word.isalnum() and word not in nltk.corpus.stopwords.words("english"):
                # Check if the word hasn't been analyzed before and the limit is not reached
                if word.lower() not in word_details and highlighted_count < 3:
                    # Highlight the word in the text
                    highlighted_text = highlighted_text.replace(word, f"*{word}*")
                    # Get meanings for the word
                    meanings = NLTKUtils.get_word_details(word)
                    word_details[word.lower()] = meanings
                    highlighted_count += 1  # Increment the counter

        return highlighted_text, word_details

    @staticmethod
    def escape_markdown(text):
        # Escape special characters used in Markdown
        escaped_text = re.sub(r"([*_`\[\]])", r"\\\1", text)
        return escaped_text
