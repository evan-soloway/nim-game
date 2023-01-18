import random
import sys

nim = open('Nim Game.html', 'w', 'r')

style = '''<style> body { color: blue; } h1 { color: brown;font-family: Comic Sans MS, serif; }</style>'''

nim.write('<html>')
nim.write(style)

def main():

     nim.open('r')
     game()

     body1 = gui()
     body2 = nim_arrangement()
     
     write(body1, body2)
     
     nim.write('</html>')
     
     
def gui():

     body = '''<html lang="en">
               <div><head><h1>"Nim to Win"</h1></head></div>'''
     return body

def nim_arrangement():
     arrangement = '''<body><em><b><p>'''+r1+'''</p><p>'''+r2+'''</p>
     <p>'''+r3+'''</p><p>'''+r4+'''</p></b></em><body>'''
     
     body = "<div>" + arrangement + '''</div>'''
     return body

def game():

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
                                   break

                              print("\nnumber of rows:", len(rows))

                              # Computer turn

                              random_num = random.randint(0,len(rows)-1)

                              comp_selected_row = rows[random_num]
                              
                              comp_selected_row_length = len(comp_selected_row)
                              
                              print ("comp selected row index:", random_num)
                              print("comp selected row length:", comp_selected_row_length)
                              
                              comp_num_select = random.randint(1,comp_selected_row_length) + 1

                              print("comp num removal:", comp_num_select)
                              
                              rows[random_num] = ["+"] * (comp_selected_row_length - comp_num_select)

                              print("\nThe computer removed", comp_num_select, "from row", random_num + 1, ".")

                              if [] in rows:
                                   rows.remove([])
                              
                              num_exception = True

                              break
                         break
                    break

          cont = input("\nDo you want to play again? ")

def write(gui_body, arrangement_body):
     writing = [gui_body, arrangement_body]
     for x in range (len(writing)):
          nim.write(writing[x])

main()

nim.close()


     
