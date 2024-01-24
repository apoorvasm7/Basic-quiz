user_input=input("enter a sentence")
if not user_input:
    print("error:input is empty")
else:
    word_count=len(user_input.split())
    print("word_count=",word_count)