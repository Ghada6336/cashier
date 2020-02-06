def main():
        Item=""
        basket=[]
        while Item !="done" :
                
               
                Item = input("Item (enter \"done\" when finished):")
                if Item == "done":
                        break
                
                price=float(input("Price:"))
                quantity=int(input("Quantity:"))
               
                case={"Item":Item,"Price":price,"Quantity":quantity}
                basket.append(case)
        print(basket)
               
        print ("-------------")
        print ("receipt")
        print ("-------------")
        
        lst=[]
        for x in basket:
               print( x["Quantity"]," ",x["Item"]," ",x["Price"],"KD")
               price= x["Price"]* x["Quantity"]
               print(price)
               lst.append(price)
               
               
                       
                       
       
               
        print ("-------------")
        print("total price=",sum(lst))
        
        
               
                       
                
         

       
        
                        
                
                 
                
                  
          

if __name__ == '__main__':
	main()
