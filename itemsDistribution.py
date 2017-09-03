#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sai B

"""
import csv
import math, traceback
from itertools import filterfalse

def main():
    try:
        itemNameDict = {}
        itemPriceDict = {}
        itemsFileName = input("Enter your file name including extension: ")
        targetPrice = 0
        targetPrice = readItems(itemsFileName, targetPrice, itemNameDict, itemPriceDict)
        if(targetPrice < 0):
            print("Target Price cannot be negative.")
        elif(targetPrice != None):
            print("\nTARGET PRICE: $%.2f" %(targetPrice))
            printItemRecords(itemNameDict, itemPriceDict)
            printItemCombinations(targetPrice, itemNameDict, itemPriceDict)
    except Exception:
            print("Error occured. Check Input.")
            print(traceback.format_exc())

def readItems(itemsFileName, targetPrice, itemNameDict, itemPriceDict) :
    flag = 0
    try:
        with open(itemsFileName, 'r') as f:
            filt_f = filterfalse(lambda line: line.startswith('\n'), f)
            itemsReader = csv.reader(filt_f)
            
            for row in itemsReader :
                if(flag == 0):
                    (target, tPrice) = row
                    targetPrice = float(tPrice.replace("$", ""))
                else:
                    (itemName, itemPrice) = row
                    newPrice = itemPrice.replace("$", "")
                    if float(newPrice) <= 0:
                        print (itemName,"has an invalid price: ",itemPrice)
                    else:
                        itemId = int(flag)
                        itemName = str(itemName)
                        itemPrice = float(newPrice)
                        itemNameDict[itemId] = itemName
                        itemPriceDict[itemId] = itemPrice
                flag=flag+1
        f.close()
        return targetPrice
    except FileNotFoundError:
        print("File not found. Please enter the correct name <filename>.csv")
    except ValueError:
        print("Data in the file is not as expected. Refer to input specification.")
    except Exception:
        print("Error occured. Check Input.")
        print(traceback.format_exc())

def printItemCombinations(targetPrice, itemNameDict, itemPriceDict):
    try:
        priceList = list(itemPriceDict.values())
        itemCombinations = 0
        m = len(priceList)
        n = int(math.pow(2, m))
        print("\nCOMBINATION OF ITEMS:")
        for i in range(1, n):
            order = bin(i)[2:].zfill(m)
            modified_order=[int(element) for  element in order]
            sum = 0
            for j in range(0, m):
                if(modified_order[j]==1):
                    sum = sum + priceList[j]
            sum = round(sum, 2)
            if(sum == targetPrice):
                itemCombinations=itemCombinations+1
                if(itemCombinations==1):
                    print("---------------------------------")
                    print("NAME                   PRICE")
                    print("-------                -----")
                if(itemCombinations>0):
                    print("Combination #",itemCombinations)
                    print("----------------")
                for j in range(0, m):
                    if(modified_order[j]==1):
                        print("{0:22s} ${1:4.2f}".format(itemNameDict[j+1], itemPriceDict[j+1]))
                print("---------------------------------")
        if(itemCombinations==0):
            print("NO COMBINATION OF ITEMS IS EQUAL TO TARGET PRICE")
    except Exception:
        print("Error occured. Check Input.")
        print(traceback.format_exc())
                    
def printItemRecords(itemNameDict, itemPriceDict) :
    try:
        print("\nITEMS AVAILABLE TO CHOOSE FROM:")
        print("---------------------------------")
        print("NAME                   PRICE")
        print("--------               ------")
        for i in itemNameDict:
            print("{0:22s} ${1:4.2f}".format(itemNameDict[i], itemPriceDict[i]))
        print("---------------------------------")
    except Exception:
        print("Error occured. Check Input.")
        print(traceback.format_exc())
        
if __name__ == "__main__":
    main()