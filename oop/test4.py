one = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twleve","Thiteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen","Twenty"]
two = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninty"]
no = 24909
words = ""
if no>9999:
  d = no // 10000
  words += two[d] + " Thousand "
  no = no % 10000
else:
    if no<9999:
          d = no // 1000
          words += one[d] + " Thousand "
          no = no % 1000

if no>99:
  d = no // 100
  words += one[d] + " Hundred "
  no = no % 100

if no>20:
  d = no // 10
  r = no % 10
  words += two[d] + " " + one[r]
else:
  words += one[no]
  

print(words)  
