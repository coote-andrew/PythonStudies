#inventory.py

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}


inventoryy = {'gold coin':42, 'rope':1}
inventori = {'gold coin':41, 'rope':1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
ratLoot = ['gold coin', 'bronze skull']

def displayInventory(inventory):
    print('Inventory:')
    item_total= 0
    for k,v in inventory.items():
        print(str(k) + ': ' + str(v))
        item_total = item_total + v
    print("total number of items: " + str(item_total))


displayInventory(stuff)
print('')
print('')
print('')


def addToInventory(invent, addedItems):
    if isinstance(addedItems, list):
        for item in addedItems:
            invent.setdefault(item, 0)
            invent[item] = invent[item] + 1
    elif isinstance(addedItems, dict):
        for k, v in addedItems.items():
            print('added ' + str(v) + ' ' + str(k) + ' to inventory')
            invent.setdefault(k,0)
            invent[k] = invent[k] + v


addToInventory(inventoryy, dragonLoot)
addToInventory(inventoryy, inventori)

displayInventory(inventoryy)
