import pandas as pd

newst2 = ''
with open('thesis.txt', 'r') as f:
    for x in f:
        newst = ''
        if not(x.startswith("  ") or x.startswith("\\") or x.startswith("%")):
            x = x.split(' ')
            for word in x:
                if '\n' in word and len(x) == 1:
                    newst += '\n\n'
                elif '~' in word:
                    if ',' in word:
                        newst += word.split('~')[0].replace('\n', '').replace('Fig.', 'the figure') + ', '
                    elif '.' in word:
                        newst += word.split('~')[0].replace('\n', '').replace('Fig.', 'the figure')  + '. '
                    else:
                        newst += word.split('~')[0].replace('\n', '').replace('Fig.', 'the figure')  + ' '
                else:
                    newst += word.replace('\n', '') + ' '
            newst2 += newst

df = pd.DataFrame([newst2])
df.to_clipboard(index=False, header=False)