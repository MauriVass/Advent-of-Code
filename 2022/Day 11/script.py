class Monkey:
    def __init__(self):
        self.items = []
        self.operator = ''
        self.factor = None
        self.test = 3
        self.divisor = []
        self.test_results = []
        self.inspected_items = 0

    def setOperation(self, operator, factor):
        self.operator = operator
        self.factor = factor

    def setDivisor(self, divisor):
        self.divisor = divisor

    def setTest(self, value):
        self.test = value

    def addTest_result(self, test_result):
        self.test_results.append(test_result)

    def getCounter(self):
        return self.inspected_items

    def executeOperation(self, value):
        if (self.factor == None):
            factor = value
        else:
            factor = self.factor
        if (self.operator == '+'):
            return value + factor
        elif (self.operator == '*'):
            return value * factor

    def skipTurn(self):
        return len(self.items) == 0

    def getItemsLength(self):
        return len(self.items)

    def simianThinking(self, pt):
        self.inspected_items += 1
        item = self.items.pop(0)
        new_worry_level = int(self.executeOperation(item) / self.test) if pt == 1 else self.executeOperation(
            item) % self.test
        if (new_worry_level % self.divisor == 0):
            next_monkey = 0
        else:
            next_monkey = 1
        return new_worry_level, self.test_results[next_monkey]

    def addItem(self, item):
        self.items.append(item)


f = open('input.txt')
# f = open('example.txt')

monkeys = []
counter = 0
lcd = 1
for line in f.readlines():
    line = line[:-1]
    if (counter == 0):
        m = Monkey()
    elif (counter == 1):
        items_part = line.split(':')
        items = [m.addItem(int(i)) for i in items_part[1].split(',')]
    elif (counter == 2):
        operation_part = line.split('=')[-1]
        factor = None
        if (operation_part.find('+') > 0):
            operator = '+'
            elements_operation = operation_part.split(operator)
            if (elements_operation[-1] != ' old'):
                factor = int(elements_operation[-1])
        elif (operation_part.find('*') > 0):
            operator = '*'
            elements_operation = operation_part.split(operator)
            a = elements_operation[-1] != ' old'
            if (elements_operation[-1] != ' old'):
                factor = int(elements_operation[-1])
        elif (operation_part.find('-') > 0):  # not present actually
            operator = '-'
            elements_operation = operation_part.split('-')
            factor = elements_operation[-1]
            function = lambda x: x - factor
        elif (operation_part.find('/') > 0):
            operator = '/'
            elements_operation = operation_part.split('/')
            factor = elements_operation[-1]
            function = lambda x: x / factor
        m.setOperation(operator, factor)
    elif (counter == 3):
        divisor = int(line.split('by')[-1])
        m.setDivisor(divisor)
        lcd *= divisor
    elif (counter == 4):
        monkey = int(line.split('monkey')[-1])
        monkey_true = monkey
        m.addTest_result(monkey_true)
    elif (counter == 5):
        monkey = int(line.split('monkey')[-1])
        monkey_false = monkey
        m.addTest_result(monkey_false)
        monkeys.append(m)
    counter += 1
    if (counter == 7):
        counter = 0
f.close()

pt = 2
n_rounds = 20 if pt == 1 else 10000
if (pt == 2):
    for m in monkeys:
        m.setTest(lcd)
for r in range(n_rounds):
    for m in monkeys:
        if (m.skipTurn() == False):
            for t in range(m.getItemsLength()):
                item, monkey = m.simianThinking(pt)
                monkeys[monkey].addItem(item)
    if (r > 0 and r % 1000 == 0):
        print(f'== After round: {r} ==')
        for i, m in enumerate(monkeys):
            print(f'Monkey {i} inspected items: {m.getCounter()}')
        print('---   ---   ---')
    is_he_worried = False

maxs = [0, 0]
for m in monkeys:
    counter_items = m.getCounter()
    if (counter_items > maxs[0]):
        tmp = maxs[0]
        maxs[0] = counter_items
        if (tmp > maxs[1]):
            maxs[1] = tmp
    elif (counter_items > maxs[1]):
        maxs[1] = counter_items
print(maxs[0] * maxs[1])  # pt1 62491, pt2 17408399184
