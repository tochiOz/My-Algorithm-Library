# learning functions
# 0(1) 
# Time complexity:
def get_single_item(items):
    return items[0];

# Space Complexity
def sum_numbers(items): # this returns a number way lesser than in space than an array
    result = 0;
    for x in items:
        result += x;

    return result

# 0(n): its this same as 0(1), only that while 0(1) runs once, it can run a number of n times
# Time complexity:
def get_total(items):
    sum = 0
    for i in items:
        sum += i
    return sum

def has_duplicate(items):
    seen = set();
    for i in range(len(items)):
        if items[i] in seen:
            return True
        seen.add(items[i])
    return False        

def has_duplicates(items):
    addedToArray = set()
    for x in items:
        if x in addedToArray:
            return True

        addedToArray.add(x)
    return False;

# Space Complexity
def has_duplicate(items): # remember even if it just returned a boolean, remember it created a set {}/[] while processing
    seen = set();
    for i in range(len(items)):
        if items[i] in seen:
            return True
        seen.add(items[i])
    return False

def doubled(items): # created a new list as return value
    newList = []
    for x in items:
        newList.append(x * 2)

    return newList

# 0(n2): is a loop inside a loop
# Time complexity:
def has_duplicate(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False;

# Space Complexity