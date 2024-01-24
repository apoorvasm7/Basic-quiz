def count_wrds(sentence):
    wrds = sentence.split()
    return len(wrds)

def avg_wrd_length(sentence):
    wrds = sentence.split()
    total_length = sum(len(word) for word in wrds)
    return total_length / len(wrds) if len(wrds) > 0 else 0

def main():

    try:
        user_input = input("Enter a sentence or paragraph: ")
        
        if not user_input:
            print("Error: Empty input. Please enter a sentence or paragraph.")
            return

        print("\nSelect an operation:")
        print("1. Word Count")
        print("2. Average Word Length")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            word_count = count_wrds(user_input)
            print(f"Word count: {word_count}")
        elif choice == "2":
            avg_length = avg_wrd_length(user_input)
            print(f"Average word length: {avg_length:.2f}")
        else:
            print("Invalid choice. Please enter 1 or 2.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
