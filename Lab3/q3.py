from collections import Counter

def get_most_frequent_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        
        words = text.split()
        word_count = Counter(words)
        
        most_common_words = dict(word_count.most_common(10))
        
        print("Top 10 most frequently appearing words:")
        for word, count in most_common_words.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")
    get_most_frequent_words(file_path)
