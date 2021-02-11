# Decorators =================================================================
# https://gist.github.com/Zearin/2f40b7b9cfc51132851a
# ============================================================================
# To understand decorators,
# you must first understand that functions are objects in Python.
# This has important consequences. Let’s see why with a simple example :

def shout(word='yes'):
    return word.capitalize() + '!'

print(shout())
# outputs : 'Yes!'

# As an object, you can assign the function to a variable like any
# other object

scream = shout

# Notice we don’t use parentheses: we are not calling the function, we are
# putting the function `shout` into the variable `scream`.
# It means you can then call `shout` from `scream`:

print(scream())
# outputs : 'Yes!'

# More than that, it means you can remove the old name `shout`, and
# the function will still be accessible from `scream`

del shout
print(shout())
# NameError: name 'shout' is not defined
print(scream())
# outputs: 'Yes!'

# ============================================================================
# ============================================================================
# Okay! Keep this in mind. We’ll circle back to it shortly.
# Another interesting property of Python functions is
# they can be defined... inside another function!
def talk():
    # You can define a function on the fly in `talk` ...
    def whisper(word='yes'):
        return word.lower() + '...'
    # ... and use it right away!
    print(whisper())

# You call `talk`, that defines `whisper` EVERY TIME you call it, then
# `whisper` is called in `talk`.
talk()
# outputs:
# "yes..."

# But `whisper` DOES NOT EXIST outside `talk`:
print(whisper())
# NameError: name 'whisper' is not defined
# ============================================================================
# ============================================================================
# You’ve seen that functions are objects. Therefore, functions:
# --> can be assigned to a variable
# --> can be defined in another function
# That means that a function can return another function. Have a look!

def getTalk(kind='shout'):

    # We define functions on the fly
    def shout(word='yes'):
        return word.capitalize() + '!'

    def whisper(word='yes'):
        return word.lower() + '...'

    # Then we return one of them
    if kind == 'shout':
        # We don’t use '()'. We are not calling the function;
        # instead, we’re returning the function object
        return shout
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()

# You can see that `talk` is here a function object:
print(talk)
#outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print(talk())
#outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk('whisper')())
#outputs : yes...
# ============================================================================
# ============================================================================
# But wait...there’s more!
# If you can return a function, you can pass one as a parameter:
def doSomethingBefore(func):
    print('I do something before then I call the function you gave me')
    print(func())

doSomethingBefore(scream)
#outputs:
#I do something before then I call the function you gave me
#Yes!
# ============================================================================
# ============================================================================
# Well, you just have everything needed to understand decorators.
# You see, decorators are “wrappers”, which means
# that they let you execute code before and after the function they decorate
# without modifying the function itself.

# Handcrafted decorators -------------------
# How you’d do it manually:
# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original
        # function is called
        print('Before the function runs')

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original
        # function is called
        print('After the function runs')

    # At this point, `a_function_to_decorate` HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before
    # and after. It’s ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don’t want to ever touch again.
def a_stand_alone_function():
    print('I am a stand alone function, don’t you dare modify me')

a_stand_alone_function()
#outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs
# ============================================================================
# ============================================================================
# Now, you probably want that every time you call a_stand_alone_function,
# a_stand_alone_function_decorated is called instead.
# That’s easy, just overwrite a_stand_alone_function
# with the function returned by my_shiny_new_decorator:
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
#outputs:
#Before the function runs
#I am a stand alone function, don’t you dare modify me
#After the function runs

# And guess what? That’s EXACTLY what decorators do!
# ============================================================================
# ============================================================================
# The previous example, using the decorator syntax:

@my_shiny_new_decorator
def another_stand_alone_function():
    print('Leave me alone')

another_stand_alone_function()
#outputs:
#Before the function runs
#Leave me alone
#After the function runs
# Yes, that’s all, it’s that simple. @decorator is just a shortcut to:
# another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
# ============================================================================
# ============================================================================
# Decorators are just a pythonic variant of the decorator design pattern
# (https://en.wikipedia.org/wiki/Decorator_pattern).
# There are several classic design patterns embedded
# in Python to ease development (like iterators).

# ============================================================================
# ============================================================================
# Of course, you can accumulate decorators:
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print('#tomatoes#')
        func()
        print('~salad~')
    return wrapper

def sandwich(food='--ham--'):
    print(food)

sandwich()
#outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>

# Using the Python decorator syntax:

@bread
@ingredients
def sandwich(food='--ham--'):
    print(food)

sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>

# The order you set the decorators MATTERS:

@ingredients
@bread
def strange_sandwich(food='--ham--'):
    print(food)

strange_sandwich()
#outputs:
##tomatoes#
#</''''''\>
# --ham--
#<\______/>
# ~salad~
# ============================================================================
# ============================================================================
# Taking decorators to the next level
# Passing arguments to the decorated function

# It’s not black magic, you just have to let the wrapper
# pass the argument:

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print('I got args! Look:', arg1, arg2)
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


# Since when you are calling the function returned by the decorator, you are
# calling the wrapper, passing arguments to the wrapper will let it pass them to
# the decorated function

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print('My name is', first_name, last_name)


print_full_name('Peter', 'Venkman')
# outputs:
# I got args! Look: Peter Venkman
# My name is Peter Venkman
# ============================================================================
# ============================================================================
# If you’re making general-purpose decorator--one you’ll apply
# to any function or method, no matter its arguments--then
# just use *args, **kwargs:
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('Do I have args?:')
        print(args)
        print(kwargs)
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print('Python is cool, no argument here.')

function_with_no_argument()
# outputs
# Do I have args?:
# ()
# {}
# Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1, 2, 3)
# outputs
# Do I have args?:
# (1, 2, 3)
# {}
# 1 2 3

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus='Why not ?'):
    print('Do {0}, {1} and {2} like platypus? {3}'.format(a, b, c, platypus))

function_with_named_arguments('Bill', 'Linus', 'Steve', platypus='Indeed!')
# outputs
# Do I have args ? :
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!
# ============================================================================
# ============================================================================
# Great, now what would you say about passing arguments to the decorator itself?
# This can get somewhat twisted, since a decorator must accept a function as an argument.
# Therefore, you cannot pass the decorated function’s arguments directly to the decorator.
# Before rushing to the solution, let’s write a little reminder:
# Decorators are ORDINARY functions
def my_decorator(func):
    print('I am an ordinary function')

    def wrapper():
        print('I am function returned by the decorator')
        func()
    return wrapper


# Therefore, you can call it without any '@'
def lazy_function():
    print('zzzzzzzz')


decorated_function = my_decorator(lazy_function)
# outputs: I am an ordinary function

# It outputs 'I am an ordinary function', because that’s just what you do:
# calling a function. Nothing magic.

@my_decorator
def lazy_function():
    print('zzzzzzzz')
# outputs: I am an ordinary function


# It’s exactly the same: my_decorator is called.
# So when you @my_decorator, you are telling Python
# to call the function labelled by the variable “my_decorator”.
# This is important!
# The label you give can point directly to the decorator—or not.
# Let’s get evil :)

def decorator_maker():
    print('I make decorators! I am executed only once: when you make me create a decorator.')

    def my_decorator(func):
        print('I am a decorator! I am executed only when you decorate a function.')

        def wrapped():
            print('I am the wrapper around the decorated function. '
                  'I am called when you call the decorated function. '
                  'As the wrapper, I return the RESULT of the decorated function.')
            return func()

        print('As the decorator, I return the wrapped function.')
        return wrapped

    print('As a decorator maker, I return a decorator')
    return my_decorator


# Let’s create a decorator. It’s just a new function after all.
new_decorator = decorator_maker()


# outputs:
# I make decorators! I am executed only once: when you make me create a decorator.
# As a decorator maker, I return a decorator

# Then we decorate the function

def decorated_function():
    print('I am the decorated function.')


decorated_function = new_decorator(decorated_function)
# outputs:
# I am a decorator! I am executed only when you decorate a function.
# As the decorator, I return the wrapped function

# Let’s call the function:
decorated_function()
# outputs:
# I am the wrapper around the decorated function. I am called when you call the decorated function.
# As the wrapper, I return the RESULT of the decorated function.
# I am the decorated function.
# ============================================================================
# ============================================================================
# No surprise here.
# Let’s do EXACTLY the same thing, but skip all the pesky intermediate variables:
def decorated_function():
    print('I am the decorated function.')
decorated_function = decorator_maker()(decorated_function)
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function.

# Finally:
decorated_function()
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.

# Let’s make it even shorter: -----------------
@decorator_maker()
def decorated_function():
    print('I am the decorated function.')
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function.

#Eventually:
decorated_function()
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.
# ============================================================================
# ============================================================================
# Hey, did you see that? We used a function call with the @ syntax! :-)
# So, back to decorators with arguments.
# If we can use functions to generate the decorator on the fly,
# we can pass arguments to that function, right?
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print('I make decorators! And I accept arguments:', decorator_arg1, decorator_arg2)

    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        # If you are not comfortable with closures, you can assume it’s ok,
        # or read: http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print('I am the decorator. Somehow you passed me arguments:', decorator_arg1, decorator_arg2)

        # Don’t confuse decorator arguments and function arguments!
        def wrapped(function_arg1, function_arg2):
            print('I am the wrapper around the decorated function.\n'
                  'I can access all the variables\n'
                  '\t- from the decorator: {0} {1}\n'
                  '\t- from the function call: {2} {3}\n'
                  'Then I can pass them to the decorated function'
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments('Leonard', 'Sheldon')
def decorated_function_with_arguments(function_arg1, function_arg2):
    print('I am the decorated function and only knows about my arguments: {0}'
          ' {1}'.format(function_arg1, function_arg2))


decorated_function_with_arguments('Rajesh', 'Howard')
# outputs:
# I make decorators! And I accept arguments: Leonard Sheldon
# I am the decorator. Somehow you passed me arguments: Leonard Sheldon
# I am the wrapper around the decorated function.
# I can access all the variables
#	- from the decorator: Leonard Sheldon
#	- from the function call: Rajesh Howard
# Then I can pass them to the decorated function
# I am the decorated function and only knows about my arguments: Rajesh Howard
