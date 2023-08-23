def function1(a):
    '''
    Function to take in a DNA sequence and returns a dictionary of the counts of each base
    Args:
    a: A string that is ideally a genomic sequences
    Returns:
    b: A dictionary of counts per unique character in the inputed string
    '''
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    '''
    function to calculate the frequencey of a dictionary and prints them
    Args:
    a: a dictionary with a unique character as a key and the counts as the value
    Returns:
    None
    '''
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
