from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot(
    'MyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
    ],
    database_uri='sqlite:///database.db'
)


trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

def chat_with_bot():
    print("Talk to the bot! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"MyBot: {response}")

chat_with_bot()
