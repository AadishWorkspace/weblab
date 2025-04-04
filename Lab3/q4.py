def sort_file_contents(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        sorted_lines = sorted(line.strip() for line in lines if line.strip())
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(sorted_lines))
        
        print(f"Sorted contents written to {output_file}")
    
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path of the input text file: ")
    output_file = input("Enter the path of the output text file: ")
    sort_file_contents(input_file, output_file)
