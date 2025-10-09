#Task 4b King Letter
'''
Task 4b King Letter (2marks)

Add to the code from part 1 to change the output when a number is 
greater than 100 to show for example:

=========================
How old are you? 111
You already got your letter 11 years ago
========================= 

'''
def main():
    x="Task4b"
    #===============================
    # Write your code here
    age = int(input("How old are you? "))
    letter = 100
    print("Years until your letter...")
    nage = letter - age
    if nage < 0:
        new_nage = nage * -1
        print(f"You already got your letter {new_nage} years ago")
    else:
        print(nage)
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
