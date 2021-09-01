import random

uniqueLetters = ["A", "E", "I", "L", "M", "N", "O", "P", "T", "V"]  
uniqueDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def parse(lettersStr, lettersWithRelevantIndex):
      letters = lettersStr.split()
      #extract index of relevant letters
      numbers = list(map(lambda letterInIndexList: str(lettersWithRelevantIndex.index(letterInIndexList)), letters))
      returnvalue = int(''.join(numbers))
      return returnvalue

def isEquationTrue(assignedLetters):
     OPTI = parse("O P T I", assignedLetters)
     ML = parse("M L", assignedLetters)
     AI = parse("A I", assignedLetters)
     NP = parse("N P", assignedLetters)
     LOVE = parse("L O V E", assignedLetters)
     return OPTI + ML + AI + NP == LOVE and not hasLeadingZeros(assignedLetters)
    
def printEquation(assignedNumbers):
  OPTI = parse("O P T I", assignedNumbers)
  ML = parse("M L", assignedNumbers)
  AI = parse("A I", assignedNumbers)
  NP = parse("N P", assignedNumbers)
  LOVE = parse("L O V E", assignedNumbers)
  print("OPTI + ML + AI + NP = LOVE: {"
            + str(OPTI) + " + " + str(ML) + " + " + str(AI) + " + " + str(NP) + " = " + str(LOVE)
            + "}")
    
def hasLeadingZeros(assignedNumbers):
      return assignedNumbers.index("O") == 0 \
        or assignedNumbers.index("M") == 0 \
        or assignedNumbers.index("A") == 0 \
        or assignedNumbers.index("N") == 0 \
        or assignedNumbers.index("L") == 0
    
def is_new_solution(solution, findings):
  return len(list(filter(lambda list: list == solution, findings))) == 0


findings = []
orderedLetters = [elem for elem in uniqueLetters]
itr = 0
while itr <= 1000000:
  itr = itr + 1
  random.shuffle(orderedLetters)
  solution = [elem for elem in orderedLetters]
  if(isEquationTrue(solution) and is_new_solution(solution, findings)):
    printEquation(solution)
    findings.append(solution)
    for l in orderedLetters:
      print(str(orderedLetters.index(l)) + ": " + l)

print("Number of iterations in search: " + str(itr))
print("Number of findings in search: ", len(findings))