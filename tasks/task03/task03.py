import re

texts = [
    "Hello, World!",
    "The world is mine",
    "Hello, how are you?"
]

words = dict()
for lineIndex, textLine in enumerate(texts):
    wordArray = re.split("\\W", textLine)
    for word in wordArray:
        word = word.lower()
        if not words.get(word):
            words[word] = {"count": 0, "first_line": lineIndex}
        words[word]["count"] += 1

del words['']
print(f"{'word':15}{'count':7}{'first line':12}")

for word in words:
    print(f"{word:15}{words[word]['count']:<7}{words[word]['first_line']:<12}")
