


NumLaughs = 0

# Check if the class is paying attention
if isClassPayingAttention == True:
    NextTopic = 'StudentCode'
else:
    NextTopic = 'ShowGoodMeme'

if NextTopic == 'StudentCode':
    ShowNextSlide()
else:
    ShowNextMeme()
    NumLaughs += 1

