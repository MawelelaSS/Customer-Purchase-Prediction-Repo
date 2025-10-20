import json

with open('Customer Purchase Prediction.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

for i, cell in enumerate(notebook['cells']):
    print(f"Cell {i}: {cell['cell_type']}")
    if cell['cell_type'] == 'code':
        print("Source:")
        for line in cell['source']:
            print(line, end='')
        print("\nOutputs:")
        for output in cell.get('outputs', []):
            if 'text' in output:
                for line in output['text']:
                    print(line, end='')
            elif 'data' in output and 'text/plain' in output['data']:
                for line in output['data']['text/plain']:
                    print(line, end='')
        print()
    elif cell['cell_type'] == 'markdown':
        print("Source:")
        for line in cell['source']:
            print(line, end='')
        print()
    print("---")
