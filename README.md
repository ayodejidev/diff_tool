# Folder and File Comparator

This Python script allows you to compare the contents of either two files or two folders and output the differences in a readable format.

## Prerequisites

- Python 3.x installed on your system

## How to Use

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script by executing the following command:
   ```bash
   python folder_file_comparator.py
   ```
5. Follow the prompts to enter the paths of the files or folders you want to compare.
6. The script will generate a diff output file named `diff_output.txt` containing the differences between the files or folders.

## Input Requirements

- You can input either two file paths or two folder paths.
- Both inputs must be of the same type (i.e., two files or two folders).

## Output

- If there are no differences between the files or folders, the script will indicate so.
- If there are differences, the script will output them in a unified diff format and save them to a file named `diff_output.txt`.

## Example Usage

- Comparing two files:

  ```bash
  Enter the path of the first file or folder: file1.txt
  Enter the path of the second file or folder: file2.txt
  ```

- Comparing two folders:
  ```bash
  Enter the path of the first file or folder: folder1
  Enter the path of the second file or folder: folder2
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
