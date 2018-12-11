from string import ascii_lowercase
f = open('input','r')
data = f.read().strip()
f.close()

def react(data):
    pre = ''
    post = data
    while(len(post) != len(pre)):
        pre = post
        for l in ascii_lowercase:
            post = post.replace(l+l.upper(), '').replace(l.upper()+l, '')
    return(len(post))

print('Part A: ', react(data))
scores = {}
for l in ascii_lowercase:
    scores[l] = react(data.replace(l,'').replace(l.upper(), ''))
print('Part B: ', min(scores.values()))
