NUMBER_OF_CUTS = int(input("NUMBER OF CUTS : "))
ANGLES_IN_LIST = list(map(int,input("ANGLES WITH SEPERATOR COMMA : ").split(",")))
K = []
for i in ANGLES_IN_LIST :
    if i not in K :
        K.append(i)
L = K    # STORING THE ANGLES WITHOUT REPETITON IN L VARIABLE
M = 0    # M IS TAKEN TO FIND OUT THE SUM OF ALL ANGLES IN LIST
for i in ANGLES_IN_LIST:
    M = M + i
X = M    # STORING THE SUM OF ALL ANGLES GIVEN IN THE LIST IS STORED IN X VARIABLE

# CASE 1 : CAKE SHOULD BE CUT INTO " N " EQUAL PARTS

# CASE 2 : CAKE SHOULD BE CUT INTO " N " PARTS

# CASE 3 : CAKE SHOULD BE CUT AND NO TWO CAKE SLICES ARE EQUAL

if NUMBER_OF_CUTS == len(ANGLES_IN_LIST)  and M ==360 :
    if len(L) == 1 and L[0] * NUMBER_OF_CUTS == 360 and len(ANGLES_IN_LIST) == NUMBER_OF_CUTS:  # FIRST CASE VERIFICATION
        print("FIRST CASE SATISFIED")
    else:
        print("FIRST CASE NOT SATISFIED")
    if X == 360 and len(ANGLES_IN_LIST) == NUMBER_OF_CUTS:                                     # SECOND CASE VERIFICATION
        print("SEOND CASE SATISFIED")
    else:
        print("SECOND CASE NOT SATISFIED")
    if K == ANGLES_IN_LIST:                                                                    # THIRD CASE VERIFICATION
        print("THIRD CASE SATISFIED")
    else:
        print("THIRD CASE NOT SATISFIED")
else:
    print("GIVE THE INPUT PROPERLY OR CHECK WHEATHER THE SUM OF ANGLES IS 360 ")