#-----------------------------------------------------------------
# StringToMusic class - This class contains the methods used
#                       to convert a string to musical notes
#-----------------------------------------------------------------
class StringToMusic:

    #gd = ""    # Fill string and uncomment print() to test
    #mi = ""    # Fill string and uncomment print() to test

#-----------------------------------------------------------------
# first_key() - Determines first key in musical representation.
#-----------------------------------------------------------------
    def first_key(a_string:str) ->str:
        for elm in a_string:
            if elm == 'A':
                return "A" 
            elif elm == 'B':
                return "B" 
            elif elm == 'C':
                return "C" 
            elif elm == 'D':
                return "D" 
            elif elm == 'E':
                return "E" 
            elif elm == 'F':
                return "F" 
            elif elm == 'G':
                return "G" 
            else:
                ''


#-----------------------------------------------------------------
# string_conversion() - This method inputs a string, then returns
#                       a string of arbitrary chars representing
#                       musical notes for MIDI message creation.
#-----------------------------------------------------------------
    def string_conversion(st:str) ->str:        # Rules
        n = 0
        li = list(st)
        start_key =  "C"
#        start_key = start_key + first_key(st)
        new_st = start_key

        for elm in li:
                                                    # Note
            if elm == 'e' or elm == 'E':            # Most common letters in English
                new_st = new_st + '1'
            elif elm == 't' or elm == 'T':
                new_st = new_st + '3'
            elif elm == 'a' or elm == 'A':
                new_st = new_st + '5'
            elif elm == 'o' or elm == 'O':
                new_st = new_st + '7'
            elif elm == 'i' or elm == 'I':
                new_st = new_st + '2'
            elif elm == 'n' or elm == 'N':
                new_st = new_st + '4'
            elif elm == 's' or elm == 'S':
                new_st = new_st + '6'
                                                # Rest
            elif elm == ' ':
                new_st = new_st + ' '
                                                # Phrase
            elif elm == """
    """:
                new_st = new_st + "*"
                if (new_st[len(new_st)-2]) == '*':     # Key from most common note
                    c = (new_st.count('1',n))
                    d = (new_st.count('2',n))
                    e = (new_st.count('3',n))
                    f = (new_st.count('4',n))
                    g = (new_st.count('5',n))
                    a = (new_st.count('6',n))
                    b = (new_st.count('7',n))

                    if a ==(max(a,b,c,d,e,f,g)):
                        new_st = new_st + ('A')
                    elif b ==(max(a,b,c,d,e,f,g)):
                        new_st = new_st + ('B')
                    elif c ==(max(a,b,c,d,e,f,g)):
                        new_st = new_st + ('C')
                    elif d ==(max(a,b,c,d,e,f,g)):
                        new_st = new_st + ('D')
                    elif e ==(max(a,b,c,d,e,f,g)):
                        new_st = new_st + ('E')
                    elif f ==(max(a,b,c,d,e,f,g)):
                        new_st = new_st + ('F')
                    elif g ==(max(a,b,c,d,e,f,g)):
                        new_st = new_st + ('G')
                    n = len(new_st)
                    new_st = new_st + ' '
            elif elm == '.':
                new_st = new_st + '.'
            elif elm == '!':
                new_st = new_st + '!'
            elif elm == '?':
                new_st = new_st + '?'
            elif elm == ',':
                new_st = new_st + ','
                                                # Note Hold
            else:                                       # all other characters
                if (new_st[len(new_st)-1]) == '1':      # checks last element in new_st
                    new_st = new_st + '-'
                if (new_st[len(new_st)-1]) == '2':
                    new_st = new_st + '-'
                if (new_st[len(new_st)-1]) == '3':
                    new_st = new_st + '-'
                if (new_st[len(new_st)-1]) == '4':
                    new_st = new_st + '-'
                if (new_st[len(new_st)-1]) == '5':
                    new_st = new_st + '-'
                if (new_st[len(new_st)-1]) == '6':
                    new_st = new_st + '-'
                if (new_st[len(new_st)-1]) == '7':
                    new_st = new_st + '-'
                if (new_st[len(new_st)-1]) == '-':
                    new_st = new_st + '-'
                else:
                    new_st = new_st + ' '
        return new_st

#-----------------------------------------------------------------
# Test prints for algorithm
# gd and mi are predefined strings to test with
#-----------------------------------------------------------------
#    print(string_conversion(gd))
#    print(string_conversion(mi))
