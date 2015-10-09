from urllib2 import Request, urlopen, URLError, time

# with open('ABBA-Test.txt') as f:
# 	content = f.readlines()
# 	print content

lines = [line.rstrip('\n') for line in open('ABBA-Test.txt')]
file = open("Lyrics.txt","w")
for songname in lines:
	base_url = 'http://api.chartlyrics.com/apiv1.asmx/GetLyric?lyricId='
	last_url = '&lyricCheckSum='
	name = 'abba'
	url = base_url + name + last_url + songname
	request = Request(url)
	response = urlopen(request)
	text = response.read()
	print(text)
	file.write(text)
	time.sleep(10)
file.close




