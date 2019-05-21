text = "X-DSPAM-Confidence:    0.8475"
lpos = text.find(':')
new_str = text[lpos + 1:]
new_str = new_str.lstrip()
print new_str
num = float(new_str)
print num
