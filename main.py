from lib.menu_driven import Productmanagmentlib

def main():
    while True:
        print('\n----product management menu----')
        print('1.add product\n2.display all product\n3.update product\n'
        '4.search product by id'
        '\n5.disable product'
        '\n6.apply gst by id'
        '\n 7.exit')
        choice=input('enter your choice:')
        if choice=='1':
            Productmanagmentlib.add_product()

        elif choice=='2':
            Productmanagmentlib.display_all()
        
        elif choice=='3':
            Productmanagmentlib.update_product()

        elif choice=='4':
            Productmanagmentlib.find_by_id()
        elif choice=='5':
            Productmanagmentlib.disable_product()

        elif choice=='6':
            Productmanagmentlib.apply_gst_to_product()
            
        elif choice=='7':
            break
        else:
            print('invalid choice,try again!')


if __name__=='__main__':
    main()
