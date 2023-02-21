# me - this DAT
# scriptOp - the OP which is cooking

# press 'Setup Parameters' in the OP to call this function to re-create the parameters
def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	p = page.appendFloat('Valuea', label='Value A')
	p = page.appendFloat('Valueb', label='Value B')
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return
	
def line(sop,x1,y1,x2,y2):
	poly = sop.appendPoly(2,addPoints=True,closed=False)
	
	poly[0].point.x = x1
	poly[0].point.y = y1
	
	poly[1].point.x = x2
	poly[1].point.y = y2
	
import random

def onCook(scriptOp):
	scriptOp.clear()
	
	gridSize = 25
	lineLength = 0.5 
	
	for x in range(-gridSize,gridSize):
		for y in range(-gridSize,gridSize):
			if random.random() > 0.5:
				line(scriptOp, x - lineLength, y - lineLength, x + lineLength, y + lineLength) 
			else: 
				line(scriptOp, x - lineLength, y + lineLength, x + lineLength, y - lineLength) 
