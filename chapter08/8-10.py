def show_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ['Hello', "Good morning", "How is it going?"]
sent_messages = []

show_messages(messages, sent_messages)

print(messages)
print(sent_messages)

