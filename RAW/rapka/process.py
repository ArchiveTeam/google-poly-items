import json
import os


def main():
    data = set()
    for filename in os.listdir('.'):
        if not filename.endswith('.json'):
            continue
        print(filename)
        with open(filename, 'r') as f:
            filedata = json.load(f)
        for d in filedata:
            data.add('poly:' + d['name'].split('/', 1)[-1])
    with open('items', 'w') as f:
        f.write('\n'.join(sorted(data)))

if __name__ == '__main__':
    main()

