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
            identifier = d['name'].split('/', 1)[-1]
            if identifier == '2Rb9zxgkDEM':
                print(d)
            data.add('poly:' + identifier)
    with open('items', 'w') as f:
        f.write('\n'.join(sorted(data)))

if __name__ == '__main__':
    main()

