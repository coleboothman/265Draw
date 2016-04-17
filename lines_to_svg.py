import sys
import re

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False	

# SVG header with placeholders for canvas width and height
SVG_HEADER = "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\""" width=\"%d\" height=\"%d\">\n"

# SVG bounding box with placeholders for width and height
SVG_BOUNDING_BOX = "<rect x=\"0\" y=\"0\" width=\"%d\" height=\"%d\""" style=\"stroke:#000;fill:none\" />\n"
# SVG line with placeholders for x0, y0, x1, y1
SVG_LINE ="<line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\""" style=\"stroke:#000\" />\n" 

# SVG footer
SVG_FOOTER = "</svg>"






CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500
BUFFER_LENGTH = 80;
buffer =[BUFFER_LENGTH]
keyword =[BUFFER_LENGTH]
line_number = 1;

# process command line arguments
if (len(sys.argv) != 2):
	print >> sys.stderr,"Usage: %s lines_file\n" % (sys.argv[0])
	sys.exit(1)

try:	
	lines_file = open(sys.argv[1], "r")
except:
	print >> sys.stderr,"Cannot open: %s\n" % (sys.argv[1])
	sys.exit(2)
	


# generate header, bounding box
print SVG_HEADER % (CANVAS_WIDTH, CANVAS_HEIGHT)
print SVG_BOUNDING_BOX % (CANVAS_WIDTH, CANVAS_HEIGHT)
checkkeyword = True
# process lines file until end of file, or an error
for line in lines_file:
	passline = True
	L = line.split()
	if checkkeyword:
		keyword = L[0]
	checkkeyword = False	
	
	buffer = ' '.join(L)
	if not(L[0] == keyword):
		print >> sys.stderr, ("Error in line %d:\n   %s\n   ^") % (line_number , buffer)
			

	elif not(is_number(L[1]) is True):
		distance = len(L[0])+1
		for i in L[1]:
			if (i.isdigit() is False):
				print >> sys.stderr, ("Error in line %d:\n   %s\n   " + (" "*distance) + "^") % (line_number , buffer)
			distance = distance + 1	
			
	elif (is_number(L[2]) is False):
		distance = len(L[0] + L[1])+2
		for i in L[2]:
			if (i.isdigit() is False):
				print >> sys.stderr, ("Error in line %d:\n   %s\n   " + (" "*distance) + "^") % (line_number , buffer)
			distance = distance + 1	
		

	elif not(is_number(L[3]) is True):
		distance = len(L[0] + L[1] + L[2])+3
		for i in L[3]:
			if (i.isdigit() is False):
				print >> sys.stderr, ("Error in line %d:\n   %s\n   " + (" "*distance) + "^") % (line_number , buffer)
			distance = distance + 1	
		

	elif not(is_number(L[4]) is True):
		distance = len(L[0] + L[1] + L[2] + L[3])+4
		for i in L[4]:
			if (i.isdigit() is False):
				print >> sys.stderr, ("Error in line %d:\n   %s\n   " + (" "*distance) + "^") % (line_number , buffer)
			distance = distance + 1	
	elif len(L) > 5:
		distance = len(L[0] + L[1] + L[2] + L[3] + L[4])+5
		print >> sys.stderr, ("Error in line %d:\n   %s\n   " + (" "*distance) + "^") % (line_number , buffer)
	else:
		x0 = int(L[1])
		y0 = int(L[2])
		x1 = int(L[3])
		y1 = int(L[4])
	
	
	# convert from standard to SVG coordinates
	# TODO: check that w/h are even?
		x0 = x0 + CANVAS_WIDTH/2;
		y0 = -y0 + CANVAS_HEIGHT/2;
		x1 = x1+ CANVAS_WIDTH/2;
		y1 = -y1 + CANVAS_HEIGHT/2;

		if (
			x0 < 0 or x0 > CANVAS_WIDTH or
			y0 < 0 or y0 > CANVAS_HEIGHT
			or
			x1 < 0 or x1 > CANVAS_WIDTH or
			y1 < 0 or y1 > CANVAS_HEIGHT
		) :
			distance = len(L[0])+1
			print >> sys.stderr, ("Error in line %d:\n   %s\n   " + (" "*distance) + "^") % (line_number , buffer)
			passline = False
			
	
		if passline is True:
			print SVG_LINE % (x0, y0, x1, y1)
		passline = True	
	line_number = line_number+1
print "%s\n" % (SVG_FOOTER)
sys.exit(0)



  



