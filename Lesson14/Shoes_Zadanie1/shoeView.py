class ShoeView:
    def display_shoes(self,shoes):
        print('\n Shoes:')
        for shoe in shoes:
            print(shoe)
    def display_price(self,price):
        print(f"\n The total price is : {price:.2f} $")
    def problem(self,msg,shoe):
        print('\n Shoes:')
        print(f'{shoe.id} {shoe.type} {msg}')