from difflib import SequenceMatcher
import datetime
import re
import time


# function for the main menu
def menu():
    width = 27
    print('+=' + '=' * (width) + '=+')
    print("Welcome what would you like to do" + "\n")
    print("1. Spell check a sentence")
    print("2. Spell check a file")
    print("0. Quit the program ")
    print('+=' + '=' * (width) + '=+')


# function for the options when a word is misspelt
def main():
    width = 27
    print('+=' + '=' * (width) + '=+')
    print("\n" + "what would you like to do" + "\n")
    print("1. Ignore the spelling error")
    print("2. Mark the error")
    print("3. Add to the dictionary ")
    print("4. Suggest likely correct spelling")
    print('+=' + '=' * (width) + '=+')


# function for the spellcheck program
def spellcheck():
    # counters
    correct = 0  # variable for correct words
    incorrectwords = 0  # variable for incorrect words
    fdictionary = 0  # variable for words added to the dictionary
    changed = 0  # variable for changed words
    number = 0  # variable for length of sentence
    now = datetime.datetime.today()
    # length of the sentence
    number = len(lst)
    with open("EnglishWords.txt", "r") as file:  # opens the dictionary file as file
        f = file.readlines()  # reads the lines in the file
        output_mark = ""
        checkedoutput = ""
        word_spelt_wrong = ""
        start = time.time()  # the beginning of the timer to time how long the program is run for
        for words in lst:  # for loop going through each word inputted
            if words + "\n" not in f:  # for words not in the dictionary
                print("\n" + "{} this string is misspelt".format(words) + "\n")
                incorrectwords += 1
                input_incorrect = True
                while input_incorrect == True:
                    main()
                    choice = input("Enter your option:  ")
                    if choice == "1":
                        input_incorrect = False
                        print("\n" + "error ignored" + "\n")
                        checkedoutput = checkedoutput + " " + words
                        break
                    if choice == "2":
                        input_incorrect = False
                        word_spelt_wrong = "?" + words + "?"  # marking the incorrect word so it can be clearly seen
                        output_mark = output_mark + " " + word_spelt_wrong
                        checkedoutput = checkedoutput + " " + output_mark
                        print(output_mark)  # printing the marked word so it is visible to the user
                        break
                    if choice == "3":
                        input_incorrect = False
                        r = open("EnglishWords.txt", "a")  # open the dictionary in append mode
                        r.write("\n{}".format(words))  # add the incorrect word into the dictionary at the bottom
                        r.close()  # close the file
                        print("\n" + "The string {} has been added to the dictionary".format(words) + "\n")
                        checkedoutput = checkedoutput + " " + words
                        # update counters
                        fdictionary += 1
                        incorrect = incorrect - 1
                        correct = correct + 1
                        break

                    if choice == "4":
                        input_incorrect = False
                        dictionary = open("EnglishWords.txt", "r")  # open dictionary in read mode
                        suggestedword = ""
                        score = 0
                        for suggest in dictionary:  # for loop to iterate through each word to find any similar
                            find = SequenceMatcher(None, words,
                                                   suggest).ratio()  # forming a ratio between suggested and inputted word
                            if find > score:
                                suggestedword = suggest
                                score = find

                        input_vali = True
                        while input_vali == True:  # while loop to make sure the correct input is given
                            question = input(
                                "Do you want to replace {} with {} ? (yes or no) ".format(words, suggestedword))
                            if question == "yes":
                                input_vali = False
                                words = suggestedword
                                print("\n" + str(words) + " this is now correct!" + "\n")
                                checkedoutput = checkedoutput + " " + words
                                # update counters
                                changed += 1
                                incorrectwords = incorrectwords - 1
                                correct = correct + 1
                                break


                            elif question == "no":
                                input_vali = False
                                print("ok")
                                checkedoutput = checkedoutput + " " + words
                                break  # breaks out of the loop and keeps the original input without suggestions

                            else:
                                print(
                                    "Error input again")  # user inputs a value other than yes or no,looping back to the option again
                        break



            else:
                print("\n" + "{} this is spelt correctly!".format(words) + "\n")
                correct += 1
                checkedoutput = checkedoutput + " " + words

        end = time.time()  # end of timer
        finaltime = end - start  # amount of time the program was run
        format_final_time = time.strftime("%H:%M:%S", time.gmtime(
            finaltime))  # chngeing the format of the timer to something more suitable
        # variables for the counters to place in a file
        v_finaltime = "The time taken to spellcheck: " + str(format_final_time)
        vDate = "Date and Time program was run: " + str(now)
        vnumber = "The total number of words: " + str(number)
        vcorrect = "The total number of words spelt correctly: " + str(correct)
        vincorrect = "The total number of words spelt incorrectly: " + str(incorrectwords)
        vdictionary = "The total number of words added to the dictionary: " + str(fdictionary)
        vchanged = "The total number of words changed: " + str(changed)
        vcheckedoutput = "Spell checked sentence: " + str(checkedoutput)
        vlst = "original sentence: " + str(lst)
        finalsentence = (input(
            "Enter the name of the file you'd like to store the spell checked sentence: "))  # asking for the name of the file to store info
        finalfile = open(finalsentence + ".txt", "w+")  # open and create a file if it does not exist in write mode
        finalfile.write(
            vincorrect + "\n" + vcorrect + "\n" + vdictionary + "\n" + vchanged + "\n" + vnumber + "\n" + vDate + "\n" + v_finaltime + "\n" + vlst + "\n" + vcheckedoutput)
        finalfile.close()

        input_val = True
        while input_val == True:  # while loop to make sure only certain answers are inputted
            option = input("Would you like to continue with the program (yes or no): ")
            if option == "yes":  # loops the program again
                input_val = False
                break
            elif option == "no":  # closes the program
                print("Thanks for using this program. Goodbye.")
                quit()
            else:
                print("Invalid choice")


# --------------------------------------------------------------------------------------#
# MAIN BODY #
while True:
    menu()
    choice = (input("Enter your option:  "))
    if choice == "1":
        # output is changed to all lower case
        string = input("Type your string: ").lower()
        # sentence broken up into words
        lst = [re.sub(r'[^a-zA-Z]+', "", word) for word in string.strip().split()]
        print(lst)
        spellcheck()

    elif choice == "2":
        input_file = True
        while input_file == True:
            filename = input("Enter file name: ")
            try:
                rfile = open(str(filename) + ".txt", "r")  # open file in read mode
            except FileNotFoundError:
                print("File not found.Try again")
                input_val = True
                while input_val == True:  # while loop to make sure only certain answers are inputted
                    option = input("\n" + """Would you like to either:
1.Input a filename again
2.go back to main menu: """)
                    if option == "1":  # loops the program again
                        input_val = False
                        break
                    elif option == "2":  # closes the program
                        input_file = False
                        break
                    else:
                        print("Invalid choice")
            except Exception:
                print("Something went wrong. Try again")
            else:
                input_file == False
                sentence = rfile.read()
                rfile.close()
                print(sentence)  # print what is in the file
                lst = [re.sub(r'[^a-zA-Z]+', "", word.lower()) for word in
                       sentence.strip().split()]  # print after removing special characters and numbers and making it lower case
                print(lst)
                spellcheck()

    elif choice == "0":  # end the program
        print("Thanks for using this program. Goodbye.")
        break

    else:  # prompt the user for a valid choice
        print("Invalid choice")
