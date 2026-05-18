history = open("history.txt", "r", encoding="utf-8", errors="ignore")
project_time = open("I was online.txt", "w", encoding="utf-8")
project_words = open("I said.txt", "w", encoding="utf-8")

words: dict[str, int] = {}

for entry in history.readlines():

    if "May" in entry and "2026" in entry:
        project_time.write(entry)
        continue

    if "AM" in entry or "PM" in entry:
        project_time.write(entry)
        continue

    for word in entry.split():
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

for word in sorted(words, key=lambda w: words[w], reverse=True):
    project_words.write(f"{word}: {words[word]}\n")

history.close()
project_time.close()
project_words.close()