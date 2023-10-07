#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Purchaseable:
    def purchase(slef,quantity,price_per_unit):
        total_cost=quantity*price_per_unit
        return total_cost
   
class Spendable:
    def calculate_total_spent(self,purchase):
        total_spent=sum(purchase)
        return total_spent
   
class Discountable:
    def apply_discount(self,total_cost,discount_percentage):
        discounted_price=total_cost*(1-discount_percentage/100)
        return discounted_price
   
    
   
class Inventory:
    def __init__(self):
        self.books={}
        
    def add_book(self,book1):
        self.books[book1.title] = book1
            
    def display_books(self,book1):
        for book1 in self.books.values():
            print(book1.display_info())
            
    def display_select_books(self,book1):
        for book1 in self.books.values():
            print(book1.display_select_info())
            
    def purchase_books(self,book1):
        selected_books = []
        total_price=0
        options=[1,2]
        while True:
            for option in options:
                option=input("\n請輸入操作:(1.購物2.結帳)")
                
                if option=='1':
                    book_name = input("請輸入書籍名稱 : ")
                    
                    if book_name in self.books and self.books[book_name].stock > 0:
                        selected_books.append(book_name)
                        purchase_quantity = int(input("請輸入購買數量: "))
                        if purchase_quantity <= self.books[book_name].stock:
                            total_price += purchase_quantity * self.books[book_name].price
                            self.books[book_name].stock -= purchase_quantity
                            print("購買成功!")
                            
                if option=='2':

                    
                    
                    print("書籍資訊:")
                    
                    self.display_select_books(book1)
                    
                    print(f"總消費金額:{total_price}")
                    discounted_cost=total_price*(1-discount_percentage/100)
                    print(f"折扣後價格:{discounted_cost}")
                    print("\n更新後庫存:")
                    self.display_books(book1)
                    
                

                

            
    


 
   
class Book(Purchaseable,Spendable,Discountable,Inventory):
    def __init__(self,isbn,title,author,price,stock):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.price=price
        self.stock=stock
       
    def display_info(self):
        return f"Title:{self.title},Author:{self.author},price:{self.price},stock:{self.stock}"
    
    def display_select_info(self):
        return f"Title:{self.title},Author:{self.author},price:{self.price}"

   
    


discount_percentage=int(input("請輸入折扣百分比:"))
inventory= Inventory()

while True:
    choise=input("\n請輸入使用者身分:(1.店家2.消費者)")
    if choise=='1':
        book1=Book(input("請輸入書籍isbn:"),input("請輸入書籍名稱:"),input("請輸入書籍作者:"),float(input("請輸入書籍價格:")),int(input("請輸入庫存數量:")))
        inventory.add_book(book1)
        unit_price=book1.price
        discounted_price=book1.apply_discount(book1.price,discount_percentage)
        print("書籍資訊:")
        inventory.display_books(book1)
        print(f"總價折扣百分比:{discount_percentage}%")
    if choise=='2':
        
        inventory.purchase_books(book1)


# In[ ]:




