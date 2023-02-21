# first-time_python

This is a Python script that defines the behavior of a custom TouchDesigner operator. The operator will generate a grid of lines at random angles, creating a glitch art-like effect. Here is a breakdown of the code:

# press 'Setup Parameters' in the OP to call this function to re-create the parameters
def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	p = page.appendFloat('Valuea', label='Value A')
	p = page.appendFloat('Valueb', label='Value B')
	return
This function defines the behavior when the "Setup Parameters" button is pressed. It adds a custom page to the operator's parameters with two float parameters called "Valuea" and "Valueb".

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

This function is called whenever a custom pulse parameter is pushed. However, it doesn't do anything in this case.

def line(sop,x1,y1,x2,y2):
	poly = sop.appendPoly(2,addPoints=True,closed=False)
	
	poly[0].point.x = x1
	poly[0].point.y = y1
	
	poly[1].point.x = x2
	poly[1].point.y = y2

This function creates a line between two points and appends it to the provided SOP (surface operator). It creates a poly primitive with two points and sets their coordinates to (x1, y1) and (x2, y2).

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

This function is called every time the operator is cooked (i.e., its output is updated). It first clears the operator's output, then creates a grid of lines by looping over the x and y coordinates in the range of -25 to 25. For each point, it randomly decides whether to draw a line from the bottom-left to the top-right, or from the top-left to the bottom-right, using the line() function defined earlier. The lineLength parameter determines the length of each line segment.

Overall, this script generates a grid of lines at random angles that change each time the operator is cooked. The parameters "Valuea" and "Valueb" don't seem to be used in this script and could be removed.

//Japanese

これは、カスタムTouchDesignerオペレーターの動作を定義するPythonスクリプトです。オペレーターは、ランダムな角度でグリッチアートのような効果を生成するグリッド線を生成します。以下にコードの詳細を示します。
# press 'Setup Parameters' in the OP to call this function to re-create the parameters
def onSetupParameters(scriptOp):
    page = scriptOp.appendCustomPage('Custom')
    p = page.appendFloat('Valuea', label='Value A')
    p = page.appendFloat('Valueb', label='Value B')
    return
この関数は、「Setup Parameters」ボタンが押されたときの動作を定義します。カスタムページをオペレーターのパラメータに追加し、「Valuea」と「Valueb」という2つの浮動小数点パラメータを作成します。
# called whenever custom pulse parameter is pushed
def onPulse(par):
    return
この関数は、カスタムパルスパラメータが押されたときに呼び出されます。ただし、この場合は何もしません。
def line(sop,x1,y1,x2,y2):
    poly = sop.appendPoly(2,addPoints=True,closed=False)
    
    poly[0].point.x = x1
    poly[0].point.y = y1
    
    poly[1].point.x = x2
    poly[1].point.y = y2

この関数は、2つの点間に線を作成し、提供されたSOP（surface operator）に追加します。2つのポイントを持つポリプリミティブを作成し、その座標を(x1、y1)と(x2、y2)に設定します。
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

この関数は、オペレーターがクックされるたびに呼び出されます（つまり、その出力が更新されます）。最初にオペレーターの出力をクリアし、次に-25から25のxおよびy座標の範囲でループして線のグリッドを作成します。各ポイントについて、前に定義されたline（）関数を使用して、ランダムに左下から右上に線を引くか、左上から右下に線を引くかを決定します。lineLengthパラメータは、各線分の長さを決定します。

全体的に、このスクリプトはランダムな角度でグリッド状の線を生成し、オペレーターがクックされるたびに変化します。「Valuea」と「Valueb」のパラメータはこのスクリプトでは使用されず、削除できます。
