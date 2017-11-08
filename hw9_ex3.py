#################
# import argparse
#################
import argparse

###############################
## short form
###############################
parser = argparse.ArgumentParser()

################################
## get 2 arguments as integer
################################
parser.add_argument("num1",help="Integer number 1",type=int)
parser.add_argument("num2",help="Integer number 2",type=int)

##########################################################################
## triggers argument parser and errors out if args not provided.
##########################################################################
args = parser.parse_args()

########################
# reassign to variables
########################
num1 = args.num1
num2 = args.num2

########################
# print result
########################
print("%d + %d = %d" % (num1, num2, num1 + num2))
