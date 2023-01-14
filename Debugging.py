import random, sys

cont = "Yes"

while cont == "Yes" or cont == "yes":

     r1 = ["+"]*7
     r2 = ["+"]*5
     r3 = ["+"]*3
     r4 = ["+"]*1

     rows = [r1,r2,r3,r4]

     while rows != []:
          
          num_exception = False
          row_exception = False

          count = 0

          while row_exception == False:

               for x in range (len(rows)):
                    print('\n'," "*x, *rows[x])

               row_select = int(input("\nSelect row to remove from (1 through " + str(len(rows)) + "): "))-1

               num_exception == True
               
               if len(rows[row_select]) == 0:
                    print("\nPlease select a row which is not empty.")
                    count += 1
                    row_exception == False


               while num_exception == False:

                    if count > 3:
                         for x in range (len(rows)):
                              print('\n'," "*x, *rows[x])

                    print("\nHow many to remove? (1 through ", len(rows[row_select]), "): ", sep='',end='')

                    num_select = int(input())

                    if num_select > len(rows[row_select]) or num_select < 1:
                         
                         print("\nPlease type a valid number.")
                         num_exception == False

                    else:
                         rows[row_select] = ["+"]*(len(rows[row_select]) - num_select)

                         if [] in rows:
                              rows.remove([])

                         if rows == []:
                              print("Congratulations! You won!")
                              break
                              

                         print("\nnumber of rows:", len(rows))

                         # Computer turn

                         random_num = random.randint(0,len(rows)-1)

                         comp_selected_row = rows[random_num]
                         
                         comp_selected_row_length = len(comp_selected_row)
                         
                         print ("comp selected row index:", random_num)
                         print("comp selected row length:", comp_selected_row_length)
                         
                         comp_num_select = random.randint(1,comp_selected_row_length)

                         print("comp num removal:", comp_num_select)
                         
                         rows[random_num] = ["+"] * (comp_selected_row_length - comp_num_select)

                         print("\nThe computer removed", comp_num_select, "card from row", random_num + 1, ".")

                         if [] in rows:
                              rows.remove([])

                         if rows == []:
                              print("Sorry! The computer won.")
                              break
                         
                         num_exception = True

                         break
                    break
               break

     cont = input("\nDo you want to play again? ")     



               
     



                    

     

          

     
     

