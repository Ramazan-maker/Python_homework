text = "это пример текста. он содержит несколько предложений. каждое предложение начинается с маленькой буквы."
lines = text.split("\n")
new_text = ""
for line in lines:
    new_text += "    " + line + "\n"
print(new_text)