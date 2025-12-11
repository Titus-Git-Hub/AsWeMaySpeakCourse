import spacy
nlp = spacy.load("en_core_web_md")

input_sentence = nlp(input("Enter a sentence of your choice to classify: "))

categories = {
    "formal": [
        "Dear Sir or Madam, I kindly request your attention to this matter.",
        "Please find the requested information in the attached document.",
        "This report illustrates the current findings in detail.",
        "I would appreciate your prompt response.",
        "For further clarification, feel free to contact me."
    ],
    "casual": [
        "I was at work today.",
        "I’m going to make dinner soon.",
        "Let me know if you need something.",
        "I’ll call you later.",
        "I went to the store earlier."
    ],
    "youth": [
        "Bro, that was totally wild.",
        "Dude, that was completely cringe.",
        "Omg, I swear that was super funny.",
        "This is so nice, no joke.",
        "Lmao, I can't stop laughing."
    ],
    "aggressive": [
        "Shut up and leave me alone.",
        "What the hell are you even talking about?",
        "Get lost, man.",
        "I don't care about your bullshit.",
        "Get out of my face."
    ],
    "emotional": [
        "I'm so happy, you have no idea!",
        "This means so much to me.",
        "I could hug the whole world right now!",
        "This really surprised me in a good way.",
        "I feel really bad today.",
        "It hurts so much to say this.",
        "I'm overwhelmed and don't know what to do.",
        "I feel completely empty.",
        "That really hit me emotionally.",
        "I'm just overwhelmed by everything."
    ]
}

sent_formal = nlp(" ".join(categories["formal"]))
sent_casual = nlp(" ".join(categories["casual"]))
sent_youth = nlp(" ".join(categories["youth"]))
sent_aggressive = nlp(" ".join(categories["aggressive"]))
sent_emotional = nlp(" ".join(categories["emotional"]))

similarity1 = input_sentence.similarity(sent_formal)
similarity2 = input_sentence.similarity(sent_casual)
similarity3 = input_sentence.similarity(sent_youth)
similarity4 = input_sentence.similarity(sent_aggressive)
similarity5 = input_sentence.similarity(sent_emotional)

print(similarity1)
print(similarity2)
print(similarity3)
print(similarity4)
print(similarity5)

similarities = {
    "formal": similarity1,
    "casual": similarity2,
    "youth": similarity3,
    "aggressive": similarity4,
    "emotional": similarity5
}

prediction = max(similarities, key=similarities.get)

print("\nPredicted category:", prediction)

# Points For Improvement: Bigger Data set; better / more efficient code structure.
