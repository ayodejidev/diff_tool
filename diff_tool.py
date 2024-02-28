import os
import difflib

def compare(file1_path, file2_path):
    """
    Compare two files.
    """
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        diff = difflib.unified_diff(file1.readlines(), file2.readlines(), fromfile=file1_path, tofile=file2_path)
        return list(diff)

def compare_folders(folder1_path, folder2_path):
    """
    Compare two folders recursively.
    """
    diff = difflib.Differ()
    folder1_contents = set(os.listdir(folder1_path))
    folder2_contents = set(os.listdir(folder2_path))

    folder1_only = folder1_contents - folder2_contents
    folder2_only = folder2_contents - folder1_contents

    diff_result = list(diff.compare(folder1_contents, folder2_contents))

    return folder1_only, folder2_only, diff_result

def main():
    input_path1 = input("Enter the path of the first file or folder: ")
    input_path2 = input("Enter the path of the second file or folder: ")

    if os.path.isfile(input_path1) and os.path.isfile(input_path2):
        # Comparing files
        diff_result = compare(input_path1, input_path2)
        if not diff_result:
            print("No differences found between the files.")
        else:
            output_file_name = "diff_output.txt"
            with open(output_file_name, 'w') as output_file:
                output_file.write('\n'.join(diff_result))
            print("Differences between the files are saved in", output_file_name)
    elif os.path.isdir(input_path1) and os.path.isdir(input_path2):
        # Comparing folders
        folder1_only, folder2_only, diff_result = compare_folders(input_path1, input_path2)
        if not diff_result:
            print("No differences found between the folders.")
        else:
            output_file_name = "diff_output.txt"
            with open(output_file_name, 'w') as output_file:
                output_file.write('\n'.join(diff_result))
            print("Differences between the folders are saved in", output_file_name)
    else:
        print("Invalid input. Please provide paths to either two files or two folders.")

if __name__ == "__main__":
    main()
