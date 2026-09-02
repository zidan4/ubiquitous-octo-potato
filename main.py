def greetings( name="You" ):
  return f"hallo {name}"

print(greetings("alex"))

def info( *args, **kwargs ):
  print(f"args: {args}")
  print(f"kwargs: {kwargs}")

info(1, 2, 3, name="alex", age=30)


courses = [ "python", "java", "javascript" ]
students = { "alex": 30, "bob": 24, "charlie": 28 }

def info2( *args, **kwargs ):
  print( args )
  print( kwargs )

info2( *courses, **students )


letters = ["a", "b", "c", "d", "e"]
print(letters.count("a"))
print( len( letters ))
print( letters.index("c"))
print( letters[0])