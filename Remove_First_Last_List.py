"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some content', '</h1>']

remove_first_last(html)
=> ['Some content']

html_2 = ['<h1>', 'Some content', 'more', '</h1>']

remove_first_last(html)
=> ['Some content', 'more']
"""

def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    if len(list_to_clean) < 3:
        return 'This list must have at least three elements included within.'
    return content

html = ['<h1>', 'Some content', '</h1>']

html_2 = ['<h1>', 'Some content', 'more', '</h1>']       

html_3 = ['<h1>', 'Some content']       



print(remove_first_and_last(html))
print(remove_first_and_last(html_2))
print(remove_first_and_last(html_3))

['Some content']
['Some content', 'more']
This list must have at least three elements included within.

# The condition within this code was an additional (you could do this)
# suggestion from Jordan, our instructor.  I took it upon myself to
# take this challenge.