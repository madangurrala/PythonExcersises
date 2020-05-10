text = "X-DSPAM-Confidence:    0.8475"
position = text.find(':')
print(float(text[position+1 :].lstrip()))
