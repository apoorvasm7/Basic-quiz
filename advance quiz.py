import pygame 
import time

class QuizGame:
    def __init__(self, questions):
        # Initialize pygame and load sound files
        pygame.init()
        self.correct_sound = pygame.mixer.Sound("correct.mp3")
        self.incorrect_sound = pygame.mixer.Sound("incorrect.mp3")

        self.questions = questions
        self.score = 0

    def play_sound(self, is_correct):
        # Play the correct or incorrect sound
        if is_correct:
            self.correct_sound.play()
        else:
            self.incorrect_sound.play()

    def ask_question(self, question, options, correct_option):
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the number): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            if options[int(user_answer) - 1] == correct_option:
                print("Correct!")
                self.play_sound(True)
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_option}")
                self.play_sound(False)
        else:
            print("Invalid input. Please enter a valid number.")

    def start_quiz(self):
        for i, (question, options, correct_option) in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}:")
            self.ask_question(question, options, correct_option)
            time.sleep(1)  # Add a pause between questions

        print(f"\nQuiz completed! Your final score is: {self.score}/{len(self.questions)}")
        pygame.mixer.quit()  # Quit pygame mixer after the quiz


# Example usage:
questions_list = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    ("Which programming language is this quiz written in?", ["Python", "Java", "C++", "JavaScript"], "Python"),
    ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], "Blue Whale"),
]

quiz = QuizGame(questions_list)
quiz.start_quiz()