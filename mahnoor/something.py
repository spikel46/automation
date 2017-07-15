#myfirstproject 7/14
#https://www.buzzfeed.com/claudiarosenbaum/kardashians-blac-chyna-nda-drama?utm_term=.fp48VA32e#.dheVlbnwv
import requests
print ("hi", 1, 2, 3)
res = requests.get('https://www.xxxbuzzfeed.com/claudiarosenbaum/kardashians-blac-chyna-nda-drama?utm_term=.fp48VA32e#.dheVlbnwv')
res.raise_for_status()
print (type(res))
print (len(res.text))
print(res.text[:250])
