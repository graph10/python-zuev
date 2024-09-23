def print_histogram(text):
    from collections import Counter

    counter = Counter(text)
    
    sorted_chars = sorted(counter.keys())
    
    max_count = max(counter.values())
    
    for i in range(max_count, 0, -1):
        line = ''
        for char in sorted_chars:
            if counter[char] >= i:
                line += '#'
            else:
                line += ' '
        print(line)
    
    print(''.join(sorted_chars))

text = input().strip()

print_histogram(text)
