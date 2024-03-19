import random
questions = [
    {
        "prompt": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Au", "C. Pt", "D. Hg"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote the novel 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Ernest Hemingway", "C. F. Scott Fitzgerald", "D. William Faulkner"],
        "answer": "A"
    },
    {
        "prompt": "What is the capital of Brazil?",
        "options": ["A. Rio de Janeiro", "B. São Paulo", "C. Brasília", "D. Salvador"],
        "answer": "C"
    },
    {
        "prompt": "Which planet is known as the 'Red Planet'?",
        "options": ["A. Jupiter", "B. Venus", "C. Mars", "D. Saturn"],
        "answer": "C "
    },
    {
        "prompt": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    {
        "prompt": "What is the chemical formula for water?",
        "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
        "answer": "A"
    },
    {
        "prompt": "Who painted the 'Mona Lisa'?",
        "options": ["A. Leonardo da Vinci", "B. Michelangelo", "C. Raphael", "D. Donatello"],
        "answer": "A"
    },
    {
        "prompt": "Which country is the largest by land area?",
        "options": ["A. Russia", "B. Canada", "C. China", "D. United States"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical symbol for silver?",
        "options": ["A. Si", "B. Ag", "C. Au", "D. Hg"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Tennessee Williams", "C. Arthur Miller", "D. George Bernard Shaw"],
        "answer": "A"
    },
    {
        "prompt": "What is the tallest mountain in the world?",
        "options": ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Lhotse"],
        "answer": "A"
    },
    {
        "prompt": "Who invented the telephone?",
        "options": ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Guglielmo Marconi"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical symbol for iron?",
        "options": ["A. Fr", "B. Ir", "C. In", "D. Fe"],
        "answer": "D"
    },
    {
        "prompt": "Who wrote 'The Great Gatsby'?",
        "options": ["A. Ernest Hemingway", "B. F. Scott Fitzgerald", "C. William Faulkner", "D. Harper Lee"],
        "answer": "B"
    },
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["A. Japan", "B. China", "C. South Korea", "D. Thailand"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical formula for carbon dioxide?",
        "options": ["A. O2", "B. H2O", "C. NaCl", "D. CO2"],
        "answer": "D"
    },
    {
        "prompt": "Who is known as the 'Father of Geometry'?",
        "options": ["A. Pythagoras", "B. Euclid", "C. Archimedes", "D. Aristotle"],
        "answer": "B"
    },
    {
        "prompt": "Which ocean is the largest?",
        "options": ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Southern Ocean"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical symbol for sodium?",
        "options": ["A. S", "B. So", "C. Na", "D. Sa"],
        "answer": "C"
    },
    {
        "prompt": "Who painted 'The Starry Night'?",
        "options": ["A. Pablo Picasso", "B. Vincent van Gogh", "C. Claude Monet", "D. Leonardo da Vinci"],
        "answer": "B"
    },
    {
        "prompt": "Which city is known as the City of Love?",
        "options": ["A. Prague", "B. Venice", "C. Rome", "D. Paris"],
        "answer": "D"
    },
    {
        "prompt": "What is the chemical formula for hydrogen peroxide?",
        "options": ["A. NaCl", "B. CO2", "C. H2O2", "D. O2"],
        "answer": "C"
    },
    {
        "prompt": "Who wrote '1984'?",
        "options": ["A. Aldous Huxley", "B. George Orwell", "C. Ray Bradbury", "D. J.R.R. Tolkien"],
        "answer": "B"
    },
    {
        "prompt": "Which country is known as the Land of the Midnight Sun?",
        "options": ["A. Finland", "B. Sweden", "C. Norway", "D. Iceland"],
        "answer": "C"
    },
    {
        "prompt": "What is the chemical symbol for oxygen?",
        "options": ["A. Ox", "B. O", "C. Oc", "D. On"],
        "answer": "B"
    },
    {
        "prompt": "Who composed 'Symphony No. 9'?",
        "options": ["A. Ludwig van Beethoven", "B. Wolfgang Amadeus Mozart", "C. Johann Sebastian Bach", "D. Pyotr Ilyich Tchaikovsky"],
        "answer": "A"
    },
    {
        "prompt": "Which planet is known as the 'Blue Planet'?",
        "options": ["A. Earth", "B. Neptune", "C. Uranus", "D. Venus"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical formula for ammonia?",
        "options": ["A. O2", "B. CO2", "C. NaCl", "D. NH3"],
        "answer": "D"
    },
    {
        "prompt": "Who painted 'The Last Supper'?",
        "options": ["A. Leonardo da Vinci", "B. Michelangelo", "C. Raphael", "D. Donatello"],
        "answer": "A"
    },
    {
        "prompt": "Which country is known as the Land of Fire and Ice?",
        "options": ["A. Greenland", "B. Iceland", "C. Finland", "D. Norway"],
        "answer": "B"
    },
    {
        "prompt": "What is the chemical symbol for helium?",
        "options": ["A. H", "B. He", "C. Hy", "D. Hee"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'Pride and Prejudice'?",
        "options": ["A. Jane Austen", "B. Emily Brontë", "C. Charlotte Brontë", "D. Virginia Woolf"],
        "answer": "A"
    },
    {
        "prompt": "Which city is known as the Eternal City?",
        "options": ["A. Jerusalem", "B. Athens", "C. Rome", "D. Istanbul"],
        "answer": "C"
    },
    {
        "prompt": "What is the chemical formula for methane?",
        "options": ["A. O2", "B. CO2", "C. NaCl", "D. CH4"],
        "answer": "D"
    },
    {
        "prompt": "Who composed 'The Four Seasons'?",
        "options": ["A. Wolfgang Amadeus Mozart", "B. Johann Sebastian Bach", "C. Antonio Vivaldi", "D. Ludwig van Beethoven"],
        "answer": "C"
    }
]


def run_quiz(questions, num_questions=10):  # Define a function named run_quiz with parameters questions and num_questions (default is 10)
    selected_questions = random.sample(questions, num_questions)  # Use random.sample to select num_questions random questions from the list of questions
    score = 0  # Initialize the score variable to keep track of the user's score
    for i, question in enumerate(selected_questions, 1):  # Iterate over each selected question using enumerate, starting from 1
        print(f"Question {i}: {question['prompt']}")  # Print the question prompt along with its index
        for option in question["options"]:  # Iterate over each option in the question's options
            print(option)  # Print the option
        
        while True:  # Start an infinite loop to ensure valid input from the user
            user_answer = input("Your answer: ").upper()  # Prompt the user for their answer and convert it to uppercase
            if user_answer in ['A', 'B', 'C', 'D']:  # Check if the user's answer is one of the valid options (A, B, C, or D)
                break  # Break out of the loop if the answer is valid
            else:
                print("Please input the right options (A, B, C, or D).")  # Print a message asking the user to input the correct options
        
        if user_answer == question["answer"]:  # Check if the user's answer matches the correct answer for the question
            print("Correct!")  # Print a message indicating the answer is correct
            score += 1  # Increment the score by 1
        else:
            print(f"Sorry, the correct answer is {question['answer']}.")  # Print a message indicating the correct answer
        
    print(f"You scored {score} out of {num_questions}.")  # Print the user's final score
    
    # Check the user's score and provide appropriate feedback
    if score > 5:
        print(f"Congratulations, you got {score}.")  # Print end of game message
    else:
        print("You suck! Do better!")  # Print a message encouraging message to the user

# Call the run_quiz function with the questions list
run_quiz(questions)