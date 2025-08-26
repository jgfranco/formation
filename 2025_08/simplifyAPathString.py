'''
Today, you will be given the problem to simply a file path string.

On Unix style computers, you can always describe an absolute path by starting with a slash, and having / separated folders after it. Here's an example:
"/home/oliver"

There three additional rules to be aware of:  
1) Additional consecutive slashes don't matter. "/home/oliver" == "/home//oliver"  
2) A ./ means current directory, and also does not matter. "home/oliver" == "/home/./oliver"
3) A ../ moves up to a parent directory. "/home/oliver/.." == "/home"  

In this problem, we're asking that you create the simplest possible path given an input string.

Follow-up:
Support relative paths. A relative path might not start with a leading slash and instead start with just a directory name, or a leading "./" or "../".
 

EXAMPLE(S)
"/a/./b/../../c/." => "/c"  
c

Here, you're drilling two folder levels in: "a" then "b", but then moving up to directories because of ".." so therefore you should end up at /. Then, you move back into c, so the final output is just "/c".
 

FUNCTION SIGNATURE
function simplifyPath(path)
def simplify_path(path):


string are always valid 


/c/.././d//e/
split("/")


'c' add to stack
'..' pop from stack
'.' ignore
'd' add to stack
'' ignore
'e' add to stack

/c/../../../
         /c//d
traverse the string from left to right
/klfs/..
[]
use a stack to keep track of folders

1 split by slash
2 traverse produced array
    if dot or no char, ignore
    if to dots, pop from stack
    anything else (name of folder), push to stack
3 return join of the stack bracketed by slashes, append a slash at the beginning,
'''

def simplify_pathAbs(path):

    elements = path.split("/")
    stack = []

    for element in elements:
        if element == '.' or element == '':
            continue
        elif element == '..' and stack:
            stack.pop()
           
        else:
            stack.append(element)
    
    return "/" + '/'.join(stack)
        
#Space: O(n) where n is the number folders in the string
# Time: O(e) where e is the number of elements we traverse

def simplify_pathRel(path):

    elements = path.split("/")
    stack = []

    absolute = False

    if len(path) > 0 and path[0] == "/": absolute = True

    for element in elements:
        if element == '.' or element == '':
            continue
        elif element == '..' and stack:
            stack.pop()
        else:
            stack.append(element)

    if absolute: return "/" + '/'.join(stack)
    
    return '/'.join(stack)


# Tests for absolute paths
print(simplify_pathAbs('/foo/bar') =="/foo/bar")
print(simplify_pathAbs('/foo//bar/') == "/foo/bar")
print(simplify_pathAbs('foo/bar/') == "/foo/bar")
print(simplify_pathAbs('/foo/bar/..') == "/foo")
print(simplify_pathAbs('/foo/../bar/') == "/bar")
print(simplify_pathAbs('/foo/bar/../baz/./../baz/../biff') == "/foo/biff")
print(simplify_pathAbs('./a/b/../../c/d/.././e/../') == "/c")  
print(simplify_pathAbs('/') == "/")
print(simplify_pathAbs('/../..') == "/")
print(simplify_pathAbs('/././foo/bar/././') == "/foo/bar")
print(simplify_pathAbs('/home/user/dir/') == "/home/user/dir")
print(simplify_pathAbs('/home//user///dir/.././') == "/home/user")
print(simplify_pathAbs('') == "/")  # Expected: /

# Tests for relative paths
print(simplify_pathRel('./foo/bar/') == "foo/bar")
print(simplify_pathRel('../foo/bar/') == "../foo/bar")
print(simplify_pathRel('./foo/bar/./baz') == "foo/bar/baz")
print(simplify_pathRel('../../foo/bar') == "foo/bar")
print(simplify_pathRel('/../..') == "/")
print(simplify_pathRel('/a/./b/../../c/') == "/c")