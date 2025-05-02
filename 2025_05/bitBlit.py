
'''
Bit Blit is a classic low level graphics interview question that may date back to the 1980s. Yes, last century. You are unlikely to encounter this in an interview for most jobs today, but it still makes a great practice problem for dealing with multi-dimensional arrays and being strategic about iteration directions.

Traditionally this problem is about [raster images](https://www.adobe.com/creativecloud/file-types/image/raster.html) but we'll make this about ASCII art. Given a large picture (represented by characters in a 2D matrix), we want to copy a subregion from a source location to a destination location within that large picture. 

The function is given a rectangular 2D matrix of single characters, source and destination points, and a size, copy the characters from the source region to the destination. The trick is to do this in-place, modifying the original array without allocating any new memory.

Each of the source and destination points are (x, y) coordinates into the matrix. The size is also two dimensional, consisting of a height and width.

For example:

********************************
*                              *
*   S--7---                    *
*   3     |                    *
*   _______                    *
*                              *
*                              *
*               D              *
*                              *
*                              *
*                              *
********************************

The top left corners of the source and destination regions are indicated by S and D respectively. The size is 7 wide by 3 high.
 

EXAMPLE(S)
function getBuffer() {
  return [
    ["*", "*", "|", "|"],
    ["*", "*", "|", "|"],
    ["-", "-", "/", "/"],
    ["-", "-", "/", "/"]
  ];
}
console.log("Original Matrix")
console.log(getBuffer());

console.log("Basic example");
let buffer = getBuffer();
bitblit(buffer, 0, 0, 2, 2, 2, 2);
console.log(buffer);

  [
    ["* (S)", "*", "|", "|"],
    ["*", "*", "|", "|"],
    ["-", "-", "*(D)", "*"],
    ["-", "-", "*", "*"]
  ];

srcx = 0
srcy = 0
destx = 2
desty = 2 
size = 2

The buffer after the bit blit is:
[
  [ '*', '*', '|', '|' ],
  [ '*', '*', '|', '|' ],
  [ '-', '-', '*', '*' ],
  [ '-', '-', '*', '*' ]
]

Notice the block of stars that was originally in the upper left has been copied to the lower right.

As another example, let's do the same thing but start the source block at (1, 1). Now the output is:
[
  [ '*', '*', '|', '|' ],
  [ '*', '*', '|', '|' ],
  [ '-', '-', '*', '|' ],
  [ '-', '-', '-', '/' ]
]

Notice that in overwriting the upper left corner of the destination, we still correctly copied the original character, the '/' to the new location.
 

FUNCTION SIGNATURE
function bitblit(buffer, srcx, srcy, destx, desty, width, height)


console.log("TEST 1 - Overlap but no issues in natural direction");
let buffer = getBuffer();
bitblit(buffer, 1, 1, 0, 0, 3, 3);
console.log(buffer);

console.log("TEST 2 - bad overlap only in X direction");
buffer = getBuffer();
bitblit(buffer, 0, 0, 0, 1, 3, 3);
console.log(buffer);

console.log("TEST 3 - bad overlap only in Y direction");
buffer = getBuffer();
bitblit(buffer, 0, 0, 1, 0, 3, 3);
console.log(buffer);

console.log("TEST 4 - bad overlap both directions");
buffer = getBuffer();
bitblit(buffer, 0, 0, 1, 1, 3, 3);
console.log(buffer);

assumptions:
src and destination can overlap
src or destination can run out of space ie width and height is larger than available room


f(buffer, srcx, srcy, dstx, dsty, width, height)
- begin at the srcx, srcy position
- loop while we havent yet run out of bounds horizontally (i)
  - loop while we havent yet run out of bounds vertically (j)
    - overwrite the cell at buffer [dstx + i][dsty + j] with the current cell


'''

def getBuffer():
  return [
    ["01", "02", "03", "04"],
    ["05", "06", "07", "08"],
    ["09", "10", "11", "12"],
    ["13", "14", "15", "16"]
  ];

def printBuffer(buffer):

    output = ""
    for row in buffer:
        output += " ".join(row) + "\n"
    print(output)

def bitblit(buffer, srcx, srcy, dstx, dsty, width, height):
    dx = -1 if dstx >= srcx and srcx + width > dstx else 1
    xstart = width - 1 if dx == -1 else 0
    xend = -1 if dx == -1 else width

    dy = -1 if dsty >= srcy and srcy + height > dsty else 1
    ystart = height - 1 if dy == -1 else 0
    yend = -1 if dy == -1 else height

    for i in range(xstart, xend, dx):
        for j in range(ystart, yend, dy):
            if dstx + i < len(buffer[0]) and dsty + j < len(buffer) and srcx + i  < len(buffer[0]) and srcy + j < len(buffer):
                buffer[dstx + i][dsty + j] = buffer[srcx + i][srcy + j]


print("TEST 1 - Overlap but no issues in natural direction");
buffer = getBuffer();
printBuffer(buffer)
bitblit(buffer, 1, 1, 0, 0, 3, 3);
printBuffer(buffer);


print("TEST 2 - bad overlap only in X direction");
buffer = getBuffer();
printBuffer(buffer)
bitblit(buffer, 0, 0, 0, 1, 3, 3);
printBuffer(buffer)

print("TEST 3 - bad overlap only in Y direction");
buffer = getBuffer();
printBuffer(buffer)
bitblit(buffer, 0, 0, 1, 0, 3, 3);
printBuffer(buffer)

print("TEST 4 - bad overlap both directions");
buffer = getBuffer();
printBuffer(buffer)
bitblit(buffer, 0, 0, 1, 1, 3, 3);
printBuffer(buffer)