class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value
    def getCost(self):

        return self.calories
    def density(self):

        return self.getValue()/self.getCost()
    def __str__(self):

        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def maxValue(toConsider:list , available:int, memo = {}):
    if (len(toConsider), available) in memo:
        result = memo[ (len(toConsider), available)]

    if toConsider == [] or available == 0:
        result =  (0,())

    elif toConsider[0].getCost() > available:
        result = maxValue(toConsider[1:], available, memo)

    else:
        next_item = toConsider[0]
        withVal, withToTake  = maxValue(toConsider[1:],available-next_item.getCost(), memo)
        withVal += next_item.getValue()
        withoutVal , withoutToTake = maxValue(toConsider[1:],available, memo)

        if withVal > withoutVal :
            result = (withVal, withToTake + (next_item,) )

        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider),available)] = result
    return result


def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxValue(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testMaxVal(foods, 750)
