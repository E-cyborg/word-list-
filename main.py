import random 
import os
def banner():
    print("\n-------------welcome to list program-------------\n")


def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def append_words(file_path, word_list):
    a=input('Do you want to see the list(y/n): ')
    if a=='y':
        for word in word_list:
            print(word)
    else:
        with open(file_path, 'a') as file:
            for word in word_list:
                file.write(word + '\n')


def generate_random_words(word_length, num_words, word_list):
    return [''.join(random.choices(word_list, k=word_length)) for _ in range(num_words)]

def fully_random(num_words, word_list):
    return [''.join(random.choices(word_list, k=random.randint(0, 100))) for _ in range(num_words)]

#def fully_random(num_words, word_list):
#    return [''.join(random.choices(word_list, k=random.randint(0, 100))) for _ in range(num_words)]


def manual_entry():
    """Manually enter words."""
    word_list = []
    while True:
        word = input("Enter a word (press Enter to finish): ")
        if not word:
            break
        word_list.append(word)
    return word_list



def create_new_file():
    """Create a new file."""
    clear_console()
    file_name = input("Enter the new file name: ")
    if os.path.exists(file_name):
        print("File already exists")
    else:
        word_list = manual_entry()
        if word_list:
            with open(file_name, 'w') as file:
                append_words(file, word_list)
            print("File created and words appended successfully.")



def append_to_existing_file():
    """Append to an existing file."""
    clear_console()
    file_name = input("Enter the existing file name: ")
    if not os.path.exists(file_name):
        print("File does not exist.")
        return

    print("Choose how to add words:")
    print("1. Manually enter words")
    print("2. Generate random words")
    print('3. length randomly')
    choice = input("Enter your choice (1 or 3): ").strip()

    if choice == '1':
        word_list = manual_entry()
    elif choice == '2':
        word_length = int(input("Enter the length of each word: "))
        num_words = int(input("Enter the number of words to generate: "))
        word_list = generate_random_words(word_length, num_words, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    elif choice == '3':
        a=0
        num_words = int(input("Enter the number of words to generate: "))
        word_list = fully_random(num_words, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    else:
        print("Invalid choice.")
        return

    if word_list:
        append_words(file_name, word_list)
        print("Words appended to the file successfully.")

def show_current_directory():
    """Display the current working directory."""
    print("Current working directory:", os.getcwd())



def change_directory():
    """Change the current working directory."""
    new_directory = input("Enter the new directory path: ")
    if os.path.exists(new_directory):
        os.chdir(new_directory)
        print("Current working directory changed to:", os.getcwd())
    else:
        print("Error: The specified path does not exist.")



def main():

    clear_console()
    while True:
        print("""
            Options:
            1. Append to an existing file
            2. Create a new file
            3. Show current directory
            4. Change directory
            5. Exit
        """)
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            append_to_existing_file()
        elif choice == '2':
            create_new_file()
        elif choice == '3':
            show_current_directory()
        elif choice == '4':
            change_directory()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    banner()
    main()
