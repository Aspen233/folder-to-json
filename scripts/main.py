import os
import json


def get_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except (UnicodeDecodeError, OSError):
        return None


def generate_folder_structure(folder_path):
    folder_structure = {}
    for root, dirs, files in os.walk(folder_path):
        relative_path = os.path.relpath(root, folder_path)
        current_level = folder_structure
        if relative_path != '.':
            for part in relative_path.split(os.sep):
                current_level = current_level.setdefault(part, {})
        for file in files:
            file_path = os.path.join(root, file)
            content = get_file_content(file_path)
            current_level[file] = content if content else "Non-viewable or binary file"
    return folder_structure


def save_as_json(folder_structure, output_file='folder_structure.json'):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(folder_structure, f, indent=4, ensure_ascii=False)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate folder structure and content in JSON format.")
    parser.add_argument("folder_path", help="Path to the folder to analyze.")
    parser.add_argument("-o", "--output", default="folder_structure.json", help="Output JSON file name.")
    args = parser.parse_args()

    folder_path = args.folder_path
    output_file = args.output

    if os.path.isdir(folder_path):
        structure = generate_folder_structure(folder_path)
        save_as_json(structure, output_file)
        print(f"Folder structure saved to {output_file}")
    else:
        print("Provided path is not a directory.")


if __name__ == "__main__":
    main()
