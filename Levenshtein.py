def distance(a, b):
    """Calculates the Levenshtein distance between a and b"""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
            
    return current_row[n]


def transform(file):
    """We take the path to the file as input, return the converted string"""
    
    text = [] # Here we will save lines of the code
    with open(file, 'r',  encoding='utf8') as f:
        # We need to drop lines which is commented
        for line in f:
            if line[0] == '#':
                continue
            if line.find('#') != -1 and (line.find('"""') == -1 and line.find("'''") == -1):
                # here we cut off the part of the string after the sign #
                text += [line[:line.find('#')]]
                continue
            text += [line]
    
    # Turn list into string. Delete all the spacec and \n
    String_text = ''
    for i in text:
        String_text += i.replace('\n', '').replace(' ', '')
    
    # Remove everything inside the quotes
    words = ['"""', "'''"]
    for word in words:
        while String_text.find(word) != -1:
            sr = String_text.find(word)
            if String_text.find(word, sr + 1) == -1:
                break
            String_text = String_text[:sr] + String_text[String_text.find(word, sr + 1) + len(word):]
    
    # Reduce the string to lowercase
    String_text = String_text.lower()
    
    # Replace the standard names with one letter
    replacement = ['import', 'from', 'def', 'class', 'return']
    shortname = ['i', 'f', 'd', 'c', 'r']
    for i in range(len(replacement)): 
        String_text = String_text.replace(replacement[i], shortname[i])    
    
    return String_text


def comparison(file_name):
    """We take file with the paths to the compared python files and get score of similarity from 0 to 1
    1 - identical code
    0 - Completely different code"""
    results = [] 
    with open(file_name, 'r') as f:
        for line in f:
            original = line.split()[0]
            fake = line.split()[1]

            file_cod = transform(original)
            plagiat_cod = transform(fake)
            
            similarity = 1 - distance(plagiat_cod, file_cod)/max(len(file_cod), len(plagiat_cod))
            
            results += [original + '  и  ' + fake + ' Сходство ' + str(round(similarity, 2))]

    return results