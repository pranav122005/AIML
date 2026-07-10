import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

import random
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

commodity_prices = {
    "onion": 3200,
    "potato": 1800,
    "tur": 7200,
    "moong": 8500,
    "rice": 4200,
    "wheat": 2800,
    "soybean": 5100,
    "cotton": 6700
}

commodities = list(commodity_prices.keys())

intents = {

    "greeting": {
        "patterns": [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening",
            "good afternoon",
            "namaste"
        ],
        "responses": [
            "Hello!",
            "Hi there!",
            "Hey!",
            "Welcome!",
            "Nice to meet you!",
            "How can I assist you today?"
        ]
    },

    "thanks": {
        "patterns": [
            "thanks",
            "thank",
            "thankyou"
        ],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "My pleasure!",
            "Anytime!"
        ]
    },

    "goodbye": {
        "patterns": [
            "bye",
            "exit",
            "quit"
        ],
        "responses": [
            "Goodbye!",
            "See you later!",
            "Have a nice day!",
            "Take care!"
        ]
    }

}

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()


def preprocess(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words]

    # Small NLP experiment
    tokens = [lemmatizer.lemmatize(word, pos="v") for word in tokens]

    return tokens


def extract_commodity(user_input):

    tokens = preprocess(user_input)

    for token in tokens:

        if token in commodities:
            return token

    return None


def get_intent(user_input):

    tokens = preprocess(user_input)

    if any(word in tokens for word in [
        "price",
        "cost",
        "rate",
        "value",
        "market",
        "buy",
        "sell"
    ]):
        return "price_query"

    if any(word in tokens for word in [
        "hi",
        "hello",
        "hey",
        "morning",
        "evening",
        "afternoon",
        "namaste"
    ]):
        return "greeting"

    if any(word in tokens for word in [
        "thanks",
        "thank"
    ]):
        return "thanks"

    if any(word in tokens for word in [
        "bye",
        "exit",
        "quit"
    ]):
        return "goodbye"

    if any(word in tokens for word in [
        "list",
        "available",
        "commodity",
        "commodities"
    ]):
        return "list"

    if "help" in tokens:
        return "help"

    return "unknown"


def chatbot():

    print("=" * 60)
    print("        Smart Commodity Price Assistant")
    print("=" * 60)
    print("Powered by NLP")
    print("\nAvailable Commodities:")
    print(", ".join(commodities).title())
    print("\nType 'help' for commands.")
    print("Type 'bye' to exit.\n")

    last_intent = None

    while True:

        user_input = input("You : ")

        intent = get_intent(user_input)

        commodity = extract_commodity(user_input)

        if intent == "unknown" and commodity:
            intent = "price_query"

        if intent == "unknown" and last_intent == "price_query":
            intent = "price_query"

        if intent == "price_query":

            if commodity:

                price = commodity_prices[commodity]

                print("=" * 40)
                print(f"Commodity     : {commodity.title()}")
                print(f"Current Price : ₹{price} per quintal")
                print("Market Status : Stable")
                print("=" * 40)
                print()

                last_intent = None

            else:

                print("Bot : Please specify the commodity.")
                print(", ".join(commodities).title())
                print()

                last_intent = "price_query"

        elif intent == "greeting":

            response = random.choice(
                intents["greeting"]["responses"]
            )

            print("Bot :", response, "\n")

            last_intent = None

        elif intent == "thanks":

            response = random.choice(
                intents["thanks"]["responses"]
            )

            print("Bot :", response, "\n")

            last_intent = None

        elif intent == "goodbye":

            response = random.choice(
                intents["goodbye"]["responses"]
            )

            print("Bot :", response)

            break

        elif intent == "list":

            print("\nAvailable Commodities:\n")

            for item in commodities:
                print("-", item.title())

            print()

            last_intent = None

        elif intent == "help":

            print("\nYou can ask questions like:\n")
            print("• Price of onion")
            print("• Cost of wheat")
            print("• Market value of rice")
            print("• List commodities")
            print("• Hi")
            print("• Thanks")
            print("• Bye\n")

            last_intent = None

        else:

            print("Bot : Sorry, I couldn't understand your request.")
            print("Try asking:")
            print("• Price of onion")
            print("• Cost of rice")
            print("• List commodities\n")

            last_intent = None


chatbot()

print(stop_words)
