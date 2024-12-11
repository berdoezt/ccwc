import sys
import os

def is_file_exist(file_name):
    return os.path.isfile(file_name)

def count_words(content_byte):
    content_words = len(content_byte.split())
    return content_words

def count_lines(content_byte):
    content_lines = len(content_byte.decode().split('\n')) - 1
    return content_lines

def count_bytes(content_byte):
    return len(content_byte)

def count_chars(content_byte: bytes):
    return len(content_byte.decode())

options = {
    '-c': count_bytes,
    '-l': count_lines,
    '-w': count_words,
    '-m': count_chars
}

def is_stdin():
    return not sys.stdin.isatty()

def process_with_stdin():
    content_byte = sys.stdin.read().encode('utf-8')
    if len(sys.argv) == 2:
        option = sys.argv[1]
        if option not in options:
            print(f"invalid option {option}")
            return
        
        result = options[option](content_byte)
        print(f"{result}")
    elif len(sys.argv) == 1:
        
        result_c = options["-c"](content_byte)
        result_l = options["-l"](content_byte)
        result_w = options["-w"](content_byte)

        print(f"  {result_l} {result_w} {result_c}")
    pass

def main():
    if len(sys.argv) == 3:
        option = sys.argv[1]
        if option not in options:
            print(f"invalid option {option}")
            return
        
        file_name = sys.argv[2]
        if not is_file_exist(file_name):
            print(f"{file_name} is not exist")
            return
        
        content_byte = open(file_name, mode='rb').read()
        result = options[option](content_byte)
        print(f"{result} {file_name}")
    elif len(sys.argv) <= 2:
        if is_stdin():
            process_with_stdin()
            return
        
        file_name = sys.argv[1]
        if not is_file_exist(file_name):
            print(f"{file_name} is not exist")
            return
        
        content_byte = open(file_name, mode='rb').read()
        
        result_c = options["-c"](content_byte)
        result_l = options["-l"](content_byte)
        result_w = options["-w"](content_byte)

        print(f"  {result_l} {result_w} {result_c} {file_name}")

if __name__ == "__main__":
    main()