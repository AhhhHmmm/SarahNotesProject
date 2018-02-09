import pyperclip

def generateSessionFocus():
	sessionFocus = 'Breaking up problems'
	preText = 'Symptoms/Challenges Since Last Session & Overall Focus:'
	midText = 'Session was focused on {}. '.format(sessionFocus)
	header = True
	with open('example.txt', 'r') as f:
		for line in f:
			if header:
				header = False
				continue
			line = line.strip()
			line = line.split('\t')
			rowData = {
				'clientReported' : line[0],
				'extraInfo' : line[1],
				'clientAndTherapistExplored' : line[2]
			}
			midText += 'Client reported ' + rowData['clientReported'].lower() + '. '
			if rowData['extraInfo'] != '':
				midText += 'Extra Info: ' + rowData['extraInfo'] + ' '
			midText += 'Client and therapist explored ' + rowData['clientAndTherapistExplored'] + '. '
	postText = ''
	textList = [preText, midText, postText]
	text = ' '.join(textList)
	pyperclip.copy(text)
	return text

def getTherapeuticIntervent():
	preText = 'Progress Towards Goals: '
	'Client has made progress as evidenced by {}'
	'Interentions Implemented: Therapist reviewed client\'s mood, symptoms, and experiences since last session. Therapist created a safe and supportive space for client to openly express herself. Therapist validated client\'s feelings to continue to establish report and strengthen the therapeutic alliance. Therapist provided unconditional positive regard in support of counseling.' # always the same
	'Client and therapist explored {}' # different options for explored
	'Client and therapist explored {}'
	'Client and therapist explored {}'
	'Client and therapist explored {}'
	'During the session, therapist encouraged client\'s autonomy and self determination.' # always the same


print(generateSessionFocus())

