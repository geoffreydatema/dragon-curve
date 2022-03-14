import maya.cmds as cmds

# Create UI
if 'UI' in globals():
    if cmds.window(UI, exists=True):
        cmds.deleteUI(UI, window=True)

UI = cmds.window(title='House Generator', width=400, height=200)

cmds.columnLayout(rowSpacing=10)

cmds.button(label='Next Generation', command='sentence = nextGeneration(sentence)')

cmds.button(label='Interpret Sentence', command='interpretSentence(sentence)')

cmds.showWindow(UI)

# L-system
#forward vectors
forwardVectors = [[0, 0, 1.0], [-1.0, 0, 0], [0, 0, -1.0], [1.0, 0, 0], [0, 0, 1.0], [-1.0, 0, 0], [0, 0, -1.0], [1.0, 0, 0], [0, 0, 1.0], [-1.0, 0, 0], [0, 0, -1.0], [1.0, 0, 0]]
iteration = 0
#variables = F, G
#constants = +, -
axiom = 'F'
rule1 = ['F', 'F+G']
rule2 = ['G', 'F-G']

sentence = axiom
print('Starting sentence: {}'.format(sentence))

def nextGeneration(sentence):
    # New sentence we are constructing
    workingSentence = ''
    # Iterate through all incoming characters
    for c in sentence:
        # Implement rules
        if(c == rule1[0]):
            workingSentence += rule1[1]
        elif(c == rule2[0]):
            workingSentence += rule2[1]
        else:
            workingSentence += c
    global iteration
    iteration += 1
    
    # Print current generation sentence
    print('Iteration {}: {}'.format(iteration, workingSentence))
    
    return workingSentence

def drawLine(startPosition, directionVector):
    newLine = cmds.curve(p=[(startPosition[0], startPosition[1], startPosition[2]), (startPosition[0] + directionVector[0], startPosition[1] + directionVector[1], startPosition[2] + directionVector[2])], degree=1)
    
    startPoint = cmds.pointOnCurve(newLine, parameter=0, position=True)
    endPoint = cmds.pointOnCurve(newLine, parameter=1.0, position=True)
    
    return [newLine, startPoint, endPoint]

def interpretSentence(sentence):

    lineData = ['', [0, 0, 0], [0, 0, 0]]
    
    forwardVectorIndex = 0
    currentDirection = forwardVectors[forwardVectorIndex]
    print(currentDirection)

    for c in sentence:
        
        if(c == 'F' or c == 'G'):
            # Draw forward
            newLine = drawLine(lineData[2], currentDirection)
            lineData = newLine
        elif(c == '+'):
            forwardVectorIndex += 1
            currentDirection = forwardVectors[forwardVectorIndex]
        elif(c == '-'):
            forwardVectorIndex -= 1
            currentDirection = forwardVectors[forwardVectorIndex]
            

