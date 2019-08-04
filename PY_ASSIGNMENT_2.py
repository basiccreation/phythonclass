# Software Discount program.
# main accepts user input as quantity (int) and
# prints a quote with the total retail price, total discount and final price

def main():
    # Global variable
    line_divider = "_____________________________"
    
    # Print welcome
    welcome_paragraph1 = "The retail price for the software is $99."
    welcome_paragraph2 = "Discounts are \ngiven as listed in the table below:"
    print("\r",welcome_paragraph1,welcome_paragraph2)
    
    # Content for discount table
    discount_table_header = "QUANTITY DISCOUNT"
    discount_10_19 = "10 - 19 pcs.\t20%"
    discount_20_49 = "20 - 49 pcs.\t30%"
    discount_50_99 = "50 - 99 pcs.\t40%"
    discount_100_up = "100 pcs. up\t50%"

    # Print discount table
    print("\n",
          discount_table_header,"\n",
          line_divider,"\n",
          discount_10_19,"discount\n",
          discount_20_49,"discount\n",
          discount_50_99,"discount\n",
          discount_100_up,"discount")

    # Get the quantity the customer wants as integer
    quantity = int(input('\nHow many packages would you like to buy? '))
    
    # Calculate price without discount
    retail_unit_price = 99
    retail_total = 0
    retail_total = retail_unit_price * quantity
    
    # Calculate the discount
    discount_percentage = 0
    discount_total = 0

    if(quantity > 99):
        discount_percentage = 50
        discount_total = int(retail_total * discount_percentage / 100)
    elif(quantity > 49):
        discount_percentage = 40
        discount_total = int(retail_total * discount_percentage / 100)
    elif(quantity > 19):
        discount_percentage = 30
        discount_total = int(retail_total * discount_percentage / 100)
    elif(quantity > 9):
        discount_percentage = 20
        discount_total = int(retail_total * discount_percentage / 100)
    else:
        discount_percentage = 0
        discount_total = 0

    # Calculate the final price
    final_price = 0
    final_price = retail_total - discount_total
    
    # Print the receipt including quantity, discount and final price
    print("\n",
          "QUOTE FOR",quantity,"PACKAGES:\n",
          line_divider,"\n",
          quantity,"pcs @ $99.00:\t",format(retail_total,',.2f'),"\n",
          "Discount is",discount_percentage,"%:\t",
          format(discount_total,',.2f'),"\n",
          "Total Amount You Pay:\t",format(final_price,',.2f'),"\r")


# Call the main function
main()

"""
--------- OUTPUT -----------


============ RESTART: /Users/piasmith/Desktop/PY_ASSIGNMENT_2.py ============
 The retail price for the software is $99. Discounts are 
given as listed in the table below:

 QUANTITY DISCOUNT 
 _____________________________ 
 10 - 19 pcs.	20% discount
 20 - 49 pcs.	30% discount
 50 - 99 pcs.	40% discount
 100 pcs. up	50% discount

How many packages would you like to buy? 100

 QUOTE FOR 100 PACKAGES:
 _____________________________ 
 100 pcs @ $99.00:	 9,900.00 
 Discount is 50 %:	 4,950.00 
 Total Amount You Pay:	 4,950.00 
 >>> 
============ RESTART: /Users/piasmith/Desktop/PY_ASSIGNMENT_2.py ============
 The retail price for the software is $99. Discounts are 
given as listed in the table below:

 QUANTITY DISCOUNT 
 _____________________________ 
 10 - 19 pcs.	20% discount
 20 - 49 pcs.	30% discount
 50 - 99 pcs.	40% discount
 100 pcs. up	50% discount

How many packages would you like to buy? 5

 QUOTE FOR 5 PACKAGES:
 _____________________________ 
 5 pcs @ $99.00:	 495.00 
 Discount is 0 %:	 0.00 
 Total Amount You Pay:	 495.00 
>>> 
============ RESTART: /Users/piasmith/Desktop/PY_ASSIGNMENT_2.py ============
 The retail price for the software is $99. Discounts are 
given as listed in the table below:

 QUANTITY DISCOUNT 
 _____________________________ 
 10 - 19 pcs.	20% discount
 20 - 49 pcs.	30% discount
 50 - 99 pcs.	40% discount
 100 pcs. up	50% discount

How many packages would you like to buy? 50

 QUOTE FOR 50 PACKAGES:
 _____________________________ 
 50 pcs @ $99.00:	 4,950.00 
 Discount is 40 %:	 1,980.00 
 Total Amount You Pay:	 2,970.00 
>>> 
============ RESTART: /Users/piasmith/Desktop/PY_ASSIGNMENT_2.py ============
 The retail price for the software is $99. Discounts are 
given as listed in the table below:

 QUANTITY DISCOUNT 
 _____________________________ 
 10 - 19 pcs.	20% discount
 20 - 49 pcs.	30% discount
 50 - 99 pcs.	40% discount
 100 pcs. up	50% discount

How many packages would you like to buy? 20

 QUOTE FOR 20 PACKAGES:
 _____________________________ 
 20 pcs @ $99.00:	 1,980.00 
 Discount is 30 %:	 594.00 
 Total Amount You Pay:	 1,386.00 
>>> 
============ RESTART: /Users/piasmith/Desktop/PY_ASSIGNMENT_2.py ============
 The retail price for the software is $99. Discounts are 
given as listed in the table below:

 QUANTITY DISCOUNT 
 _____________________________ 
 10 - 19 pcs.	20% discount
 20 - 49 pcs.	30% discount
 50 - 99 pcs.	40% discount
 100 pcs. up	50% discount

How many packages would you like to buy? 10

 QUOTE FOR 10 PACKAGES:
 _____________________________ 
 10 pcs @ $99.00:	 990.00 
 Discount is 20 %:	 198.00 
 Total Amount You Pay:	 792.00 
>>> 
============ RESTART: /Users/piasmith/Desktop/PY_ASSIGNMENT_2.py ============
 The retail price for the software is $99. Discounts are 
given as listed in the table below:

 QUANTITY DISCOUNT 
 _____________________________ 
 10 - 19 pcs.	20% discount
 20 - 49 pcs.	30% discount
 50 - 99 pcs.	40% discount
 100 pcs. up	50% discount

How many packages would you like to buy? 5

 QUOTE FOR 5 PACKAGES:
 _____________________________ 
 5 pcs @ $99.00:	 495.00 
 Discount is 0 %:	 0.00 
 Total Amount You Pay:	 495.00 
>>> 
============ RESTART: /Users/piasmith/Desktop/PY_ASSIGNMENT_2.py ============
 The retail price for the software is $99. Discounts are 
given as listed in the table below:

 QUANTITY DISCOUNT 
 _____________________________ 
 10 - 19 pcs.	20% discount
 20 - 49 pcs.	30% discount
 50 - 99 pcs.	40% discount
 100 pcs. up	50% discount

How many packages would you like to buy? 0

 QUOTE FOR 0 PACKAGES:
 _____________________________ 
 0 pcs @ $99.00:	 0.00 
 Discount is 0 %:	 0.00 
 Total Amount You Pay:	 0.00 
>>> 
----------------------------
"""
