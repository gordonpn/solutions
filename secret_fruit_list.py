from typing import List


def matchSecretLists(
    secretFruitList: List[List[str]], customerPurchasedList: List[str]
) -> bool:
    customer_item = 0
    while customer_item < len(customerPurchasedList):
        curr_item = customer_item
        for sub_list in secretFruitList:
            for index, secret_item in enumerate(sub_list):
                if secret_item == "anything":
                    curr_item += 1
                elif secret_item == customerPurchasedList[curr_item]:
                    if index == len(sub_list) - 1:
                        return True
                    curr_item += 1
                else:
                    curr_item = 0
                    break
            if curr_item == len(customerPurchasedList) - 1:
                break
        customer_item += 1
    return False


secret1 = [["orange", "mango"], ["watermelon", "mango"]]
customer1 = ["orange", "mango", "strawberry", "watermelon", "mango"]

secret2 = [["watermelon", "anything", "mango"]]
customer2 = ["watermelon", "orange", "mango"]

secret3 = [["watermelon", "anything", "mango"]]
customer3 = ["watermelon", "apple", "orange", "mango"]

secret4 = [["apple", "apple"]]
customer4 = ["apple", "apple"]

secret5 = [["anything", "apple"], ["banana", "anything", "banana"]]
customer5 = [
    "orange",
    "grapes",
    "apple",
    "orange",
    "orange",
    "banana",
    "apple",
    "banana",
    "banana",
]

secret6 = [["apple"]]
customer6 = ["apple"]

print(matchSecretLists(secret1, customer1))  # True
print(matchSecretLists(secret2, customer2))  # True
print(matchSecretLists(secret3, customer3))  # False
print(matchSecretLists(secret4, customer4))  # True
print(matchSecretLists(secret5, customer5))  # True
print(matchSecretLists(secret6, customer6))  # True
