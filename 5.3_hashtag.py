import string

user_hashtag = input("Enter a hashtag: ").title().replace(' ','')
new_hashtag = ''.join(i for i in user_hashtag if i not in string.punctuation)
cut_hashtag = new_hashtag[:139]
print('#' + cut_hashtag)
#print(len('#' + cut_hashtag))
