
'''
Today, you will be given the problem to simply a file path string.

On Unix style computers, you can always describe an absolute path by starting with a slash, and having / separated folders after it. Here's an example:
"/home/oliver"

There three additional rules to be aware of:  
1) Additional consecutive slashes don't matter. "/home/oliver" == "/home//oliver"  
2) A ./ means current directly, and also does not matter. "home/oliver" == "/home/./oliver"  
3) A ../ moves up to a parent directory. "/home/oliver/.." == "/home"  

In this problem, we're asking that you create the simplest possible path given an input string.

Follow-up:
Support relative paths. A relative path might not start with a leading slash and instead start with just a directory name, or a leading "./" or "../".
 

EXAMPLE(S)
"/a/./b/../../c/." => "/c"  
['',a,.,b,..,..,c,.]
[c] -> /c

"/c/a/.././d" => "/c/d"  
[c,d]

Here, you're drilling two folder levels in: "a" then "b", but then moving up to directories because of ".." so therefore you should end up at /. Then, you move back into c, so the final output is just "/c".
 

FUNCTION SIGNATURE
func simplify(path: String) -> String
'''
def simplify(path):
    path_arr = path.split("/")
    q = []

    for i in range(len(path_arr)):
        if path_arr[i] in {"","."}: 
            continue
        elif path_arr[i] == "..":
            if q:
                q.pop()
        else:  #word or char
            q.append(path_arr[i])
    
    if path_arr[0] == "":
        res = "/" + "/".join(q)
    else:
        res = "/".join(q)
    return res

print(simplify("/a/./b/../../c/.")) # /c
print(simplify("/c/a/.././d")) # /c/d

print(simplify('/foo/bar'))
print(simplify('/foo//bar/'))
print(simplify('foo/bar/')) # foo/bar
print(simplify('/foo/bar/..'))
print(simplify('/foo/../bar/'))
print(simplify('/foo/bar/../baz/./../baz/../biff'))

# # tests for relative paths
print(simplify('./foo/bar/')) 
print(simplify('../foo/bar/'))